from core.rules.ruleset import RuleSet
from pydantic import BaseModel
from typing import Optional, Dict, List
import math

class LoanScheme(BaseModel):
    loan_id: str
    rule_set: RuleSet
    name: str
    description: str
    
    product_id: Optional[str] = None
    lender_id: Optional[str] = None
    product_name: Optional[str] = None
    product_type: Optional[str] = None
    product_subtype: Optional[str] = None
    interest_rates: Optional[Dict] = None
    fees_and_charges: Optional[Dict] = None
    loan_limits: Optional[Dict] = None
    tenure_options: Optional[Dict] = None
    common_hard_rules: Optional[Dict] = None
    type_specific_hard_rules: Optional[Dict] = None
    common_soft_rules: Optional[Dict] = None
    type_specific_soft_rules: Optional[Dict] = None
    
    # Allows using custom python classes as field types
    class Config:
        arbitrary_types_allowed = True
    
    def load_from_db(self):
        from utils.database import get_db
        
        db = get_db()
        loan_products = db['loan_products']
        
        product = loan_products.find_one({
            '$or': [
                {'product_id': self.loan_id},
                {'lender_id': self.loan_id}
            ]
        })
        
        if product:
            self.product_id = product.get('product_id')
            self.lender_id = product.get('lender_id')
            self.product_name = product.get('product_name')
            self.product_type = product.get('product_type')
            self.product_subtype = product.get('product_subtype')
            self.interest_rates = product.get('interest_rates', {})
            self.fees_and_charges = product.get('fees_and_charges', {})
            self.loan_limits = product.get('loan_limits', {})
            self.tenure_options = product.get('tenure_options', {})
            self.common_hard_rules = product.get('common_hard_rules', {})
            self.type_specific_hard_rules = product.get('type_specific_hard_rules', {})
            self.common_soft_rules = product.get('common_soft_rules', {})
            self.type_specific_soft_rules = product.get('type_specific_soft_rules', {})
            
            return True
        return False
    
    def _get_base_rate(self) -> float:
        if not self.interest_rates:
            return 0.0
        return float(self.interest_rates.get('base_rate', 0.0))
    
    def _calculate_processing_fee(self, principal: float) -> float:
        if not self.fees_and_charges:
            return 0.0
        
        fee_percent = self.fees_and_charges.get('processing_fee_percent', 0.0)
        fee_min = self.fees_and_charges.get('processing_fee_min', 0.0)
        fee_max = self.fees_and_charges.get('processing_fee_max', float('inf'))
        
        calculated_fee = principal * (fee_percent / 100)
        fee = max(calculated_fee, fee_min)
        fee = min(fee, fee_max)
        
        return round(fee, 2)
    
    def calculate_emi(
        self, 
        principal: float, 
        tenure_months: int, 
        custom_rate: Optional[float] = None
    ) -> float:
        rate = custom_rate if custom_rate is not None else self._get_base_rate()
        
        P = float(principal)
        R = rate / 12 / 100
        N = int(tenure_months)
        
        if R == 0:
            return round(P / N, 2)
        # Standard bank formula: 
        # EMI = [P × R × (1+R)^N] / [(1+R)^N - 1]
        emi = (P * R * math.pow(1 + R, N)) / (math.pow(1 + R, N) - 1)
        return round(emi, 2)
    
    def calculate_total_interest(
        self, 
        principal: float, 
        tenure_months: int, 
        custom_rate: Optional[float] = None
    ) -> float:
        emi = self.calculate_emi(principal, tenure_months, custom_rate)
        total_payment = emi * tenure_months
        total_interest = total_payment - principal
        return round(total_interest, 2)
    
    def calculate_total_payment(
        self, 
        principal: float, 
        tenure_months: int, 
        custom_rate: Optional[float] = None
    ) -> float:
        emi = self.calculate_emi(principal, tenure_months, custom_rate)
        return round(emi * tenure_months, 2)
    
    # calls all calculation methods and bundles result into dictionary
    def get_loan_summary(
        self, 
        principal: float, 
        tenure_months: int, 
        custom_rate: Optional[float] = None
    ) -> Dict:
        rate = custom_rate if custom_rate is not None else self._get_base_rate()
        
        emi = self.calculate_emi(principal, tenure_months, custom_rate)
        total_interest = self.calculate_total_interest(principal, tenure_months, custom_rate)
        total_payment = self.calculate_total_payment(principal, tenure_months, custom_rate)
        processing_fee = self._calculate_processing_fee(principal)
        
        return {
            'productId': self.product_id,
            'lenderId': self.lender_id,
            'productName': self.product_name,
            'loanType': self.product_type,
            'loanSubtype': self.product_subtype,
            'schemeName': self.name,
            'description': self.description,
            'principal': principal,
            'interestRate': rate,
            'rateType': self.interest_rates.get('rate_type') if self.interest_rates else None,
            'tenureMonths': tenure_months,
            'tenureYears': round(tenure_months / 12, 1),
            'monthlyEMI': emi,
            'totalInterest': total_interest,
            'totalPayment': total_payment,
            'processingFee': processing_fee,
            'totalCost': round(total_payment + processing_fee, 2),
            'interestPercentage': round((total_interest / principal) * 100, 2),
            'principalPercentage': round((principal / total_payment) * 100, 2)
        }
    
    # Shows how each EMI splits into Principal + Interest
    # Pattern -> early months have more interest, later months have more principal
    def get_amortization_schedule(
        self, 
        principal: float, 
        tenure_months: int, 
        custom_rate: Optional[float] = None
    ) -> List[Dict]:
        rate = custom_rate if custom_rate is not None else self._get_base_rate()
        R = rate / 12 / 100
        
        emi = self.calculate_emi(principal, tenure_months, custom_rate)
        balance = float(principal)
        schedule = []
        
        for month in range(1, tenure_months + 1):
            interest_payment = balance * R
            principal_payment = emi - interest_payment
            balance = balance - principal_payment
            
            if balance < 0:
                balance = 0
            
            schedule.append({
                'month': month,
                'emi': round(emi, 2),
                'principal': round(principal_payment, 2),
                'interest': round(interest_payment, 2),
                'balance': round(balance, 2)
            })
        
        return schedule
    
    # uses available_tenure from DB
    def compare_tenures(
        self, 
        principal: float, 
        tenure_options: Optional[List[int]] = None
    ) -> List[Dict]:
        if tenure_options is None and self.tenure_options:
            tenure_options = self.tenure_options.get('available_tenures', [])
        
        if not tenure_options:
            tenure_options = [60, 120, 180, 240, 300, 360]
        
        comparisons = []
        for tenure in tenure_options:
            summary = self.get_loan_summary(principal, tenure)
            comparisons.append(summary)
        
        return comparisons
    
    def calculate_max_loan_amount(
        self, 
        max_emi: float, 
        tenure_months: int,
        custom_rate: Optional[float] = None
    ) -> float:
        rate = custom_rate if custom_rate is not None else self._get_base_rate()
        R = rate / 12 / 100
        N = tenure_months
        
        if R == 0:
            max_loan = max_emi * N
        else:
            max_loan = max_emi * (math.pow(1 + R, N) - 1) / (R * math.pow(1 + R, N))
        
        if self.loan_limits:
            max_allowed = self.loan_limits.get('max_loan_amount', float('inf'))
            max_loan = min(max_loan, max_allowed)
        
        return round(max_loan, 2)
    
    def validate_loan_amount(self, amount: float) -> tuple:
        if not self.loan_limits:
            return True, "No limits defined"
        
        min_amount = self.loan_limits.get('min_loan_amount', 0)
        max_amount = self.loan_limits.get('max_loan_amount', float('inf'))
        
        if amount < min_amount:
            return False, f"Minimum loan amount is ₹{min_amount:,.0f}"
        if amount > max_amount:
            return False, f"Maximum loan amount is ₹{max_amount:,.0f}"
        
        return True, "Valid loan amount"
    
    def validate_tenure(self, tenure_months: int) -> tuple:
        if not self.tenure_options:
            return True, "No tenure limits defined"
        
        min_tenure = self.tenure_options.get('min_tenure_months', 0)
        max_tenure = self.tenure_options.get('max_tenure_months', float('inf'))
        available = self.tenure_options.get('available_tenures', [])
        
        if tenure_months < min_tenure:
            return False, f"Minimum tenure is {min_tenure} months ({min_tenure//12} years)"
        if tenure_months > max_tenure:
            return False, f"Maximum tenure is {max_tenure} months ({max_tenure//12} years)"
        
        if available and tenure_months not in available:
            return False, f"Available tenures: {available} months"
        
        return True, "Valid tenure"
