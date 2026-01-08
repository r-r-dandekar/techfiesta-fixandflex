from core.loan_scheme import LoanScheme
from core.rules.ruleset import RuleSet

def test_basic_emi_calculation():
    rule_set = RuleSet()
    
    scheme = LoanScheme(
        loan_id="HDFC_HOME_001",
        rule_set=rule_set,
        name="HDFC Home Loan",
        description="Premium home loan from HDFC Bank"
    )
    
    if not scheme.load_from_db():
        print("Error: Could not load loan product from database")
        return
    
    print("="*70)
    print("DATABASE DETAILS")
    print("="*70)
    print(f"Product: {scheme.product_name}")
    print(f"Lender: {scheme.lender_id}")
    print(f"Type: {scheme.product_type} - {scheme.product_subtype}")
    print(f"Base Rate: {scheme._get_base_rate()}%")
    print(f"Rate Type: {scheme.interest_rates.get('rate_type')}")
    
    principal = 3000000
    tenure = 240
    
    print("\n" + "="*70)
    print(f"CALCULATION FOR RS.{principal:,} OVER {tenure} MONTHS")
    print("="*70)
    
    emi = scheme.calculate_emi(principal, tenure)
    total_interest = scheme.calculate_total_interest(principal, tenure)
    total_payment = scheme.calculate_total_payment(principal, tenure)
    
    print(f"\nLoan Amount: Rs.{principal:,}")
    print(f"Tenure: {tenure//12} years ({tenure} months)")
    print(f"Interest Rate: {scheme._get_base_rate()}% per annum")
    print(f"\nMonthly EMI: Rs.{emi:,.2f}")
    print(f"Total Interest: Rs.{total_interest:,.2f}")
    print(f"Total Payment: Rs.{total_payment:,.2f}")
    
    processing_fee = scheme._calculate_processing_fee(principal)
    total_cost = total_payment + processing_fee
    print(f"Processing Fee: Rs.{processing_fee:,.2f}")
    print(f"Total Cost: Rs.{total_cost:,.2f}")


def test_loan_validation():
    rule_set = RuleSet()
    
    scheme = LoanScheme(
        loan_id="HDFC_HOME_001",
        rule_set=rule_set,
        name="HDFC Home Loan",
        description="Premium home loan"
    )
    
    scheme.load_from_db()
    
    print("\n" + "="*70)
    print("VALIDATION TESTS")
    print("="*70)
    
    test_amounts = [400000, 3000000, 60000000]
    
    for amount in test_amounts:
        is_valid, message = scheme.validate_loan_amount(amount)
        status = "PASS" if is_valid else "FAIL"
        print(f"\nAmount Rs.{amount:,}: [{status}] {message}")
    
    test_tenures = [48, 240, 400]
    
    for tenure in test_tenures:
        is_valid, message = scheme.validate_tenure(tenure)
        status = "PASS" if is_valid else "FAIL"
        print(f"Tenure {tenure} months: [{status}] {message}")


def test_tenure_comparison():
    rule_set = RuleSet()
    
    scheme = LoanScheme(
        loan_id="HDFC_HOME_001",
        rule_set=rule_set,
        name="HDFC Home Loan",
        description="Premium home loan"
    )
    
    scheme.load_from_db()
    
    principal = 3000000
    
    print("\n" + "="*70)
    print(f"TENURE COMPARISON FOR RS.{principal:,}")
    print("="*70)
    print(f"\n{'Years':<8} {'Months':<10} {'EMI':<15} {'Interest':<15} {'Total':<15}")
    print("-"*70)
    
    comparisons = scheme.compare_tenures(principal)
    
    for comp in comparisons:
        years = comp['tenureYears']
        months = comp['tenureMonths']
        emi = comp['monthlyEMI']
        interest = comp['totalInterest']
        total = comp['totalPayment']
        
        print(f"{years:<8.1f} {months:<10} Rs.{emi:<13,.0f} Rs.{interest:<13,.0f} Rs.{total:<13,.0f}")


def test_amortization_schedule():
    rule_set = RuleSet()
    
    scheme = LoanScheme(
        loan_id="HDFC_HOME_001",
        rule_set=rule_set,
        name="HDFC Home Loan",
        description="Premium home loan"
    )
    
    scheme.load_from_db()
    
    principal = 3000000
    tenure = 240
    
    print("\n" + "="*70)
    print("AMORTIZATION SCHEDULE - FIRST 12 MONTHS")
    print("="*70)
    print(f"\n{'Month':<8} {'EMI':<15} {'Principal':<15} {'Interest':<15} {'Balance':<15}")
    print("-"*70)
    
    schedule = scheme.get_amortization_schedule(principal, tenure)
    
    for month_data in schedule[:12]:
        month = month_data['month']
        emi = month_data['emi']
        principal_pay = month_data['principal']
        interest_pay = month_data['interest']
        balance = month_data['balance']
        
        print(f"{month:<8} Rs.{emi:<13,.2f} Rs.{principal_pay:<13,.2f} Rs.{interest_pay:<13,.2f} Rs.{balance:<13,.2f}")


def test_max_loan_calculation():
    rule_set = RuleSet()
    
    scheme = LoanScheme(
        loan_id="HDFC_HOME_001",
        rule_set=rule_set,
        name="HDFC Home Loan",
        description="Premium home loan"
    )
    
    scheme.load_from_db()
    
    print("\n" + "="*70)
    print("MAXIMUM LOAN CALCULATION")
    print("="*70)
    
    affordable_emis = [20000, 30000, 40000, 50000]
    tenure = 240
    
    print(f"\nFor tenure of {tenure} months ({tenure//12} years):")
    print(f"\n{'Affordable EMI':<20} {'Maximum Loan':<20}")
    print("-"*40)
    
    for emi in affordable_emis:
        max_loan = scheme.calculate_max_loan_amount(emi, tenure)
        print(f"Rs.{emi:<18,} Rs.{max_loan:<18,.0f}")


def test_complete_summary():
    rule_set = RuleSet()
    
    scheme = LoanScheme(
        loan_id="HDFC_HOME_001",
        rule_set=rule_set,
        name="HDFC Home Loan",
        description="Premium home loan"
    )
    
    scheme.load_from_db()
    
    principal = 3000000
    tenure = 240
    
    print("\n" + "="*70)
    print("COMPLETE LOAN SUMMARY")
    print("="*70)
    
    summary = scheme.get_loan_summary(principal, tenure)
    
    print(f"\nProduct ID: {summary['productId']}")
    print(f"Lender: {summary['lenderId']}")
    print(f"Product Name: {summary['productName']}")
    print(f"Loan Type: {summary['loanType']} - {summary['loanSubtype']}")
    
    print(f"\nLoan Amount: Rs.{summary['principal']:,}")
    print(f"Interest Rate: {summary['interestRate']}% {summary['rateType']}")
    print(f"Tenure: {summary['tenureYears']} years ({summary['tenureMonths']} months)")
    
    print(f"\nMonthly EMI: Rs.{summary['monthlyEMI']:,}")
    print(f"Total Interest: Rs.{summary['totalInterest']:,}")
    print(f"Processing Fee: Rs.{summary['processingFee']:,}")
    print(f"Total Payment: Rs.{summary['totalPayment']:,}")
    print(f"Total Cost: Rs.{summary['totalCost']:,}")
    
    print(f"\nInterest as % of Principal: {summary['interestPercentage']:.2f}%")
    print(f"Principal as % of Total: {summary['principalPercentage']:.2f}%")


def run_all_tests():
    print("\nSTARTING LOAN CALCULATOR TESTS")
    print("="*70)
    
    test_basic_emi_calculation()
    test_loan_validation()
    test_tenure_comparison()
    test_amortization_schedule()
    test_max_loan_calculation()
    test_complete_summary()
    
    print("\n" + "="*70)
    print("ALL TESTS COMPLETED")
    print("="*70)


if __name__ == "__main__":
    run_all_tests()
