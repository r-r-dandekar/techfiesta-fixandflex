class User:

    # This is a dictionary containing the user's details in the format given at: documenation/sample_user_info.md
    info: dict

    # For testing, to set the user's info to the sample data (copied from documenation/sample_user_info.md)
    def set_sample_info(self):
        self.info = {
    "application_id": "APP_2024_001234",
    "timestamp": "2024-01-04T10:30:00Z",
    "personal_info": {
        "age": 32,
        "date_of_birth": "1992-05-15",
        "gender": "male",
        "marital_status": "married",
        "dependents": 1,
        "education": "graduate",
        "pincode": "411001",
        "city": "Pune",
        "state": "Maharashtra",
        "city_tier": 1
    },
    "employment": {
        "applicable": True,
        "type": "salaried",
        "employer_name": "Infosys Ltd",
        "employer_type": "MNC",
        "industry": "IT",
        "years_in_current_job": 5.5,
        "total_work_experience": 8,
        "monthly_gross_salary": 125000,
        "monthly_net_salary": 95000,
        "other_monthly_income": 5000
    },
    "business_info": {
        "applicable": False,
        "business_type": None,
        "business_name": None,
        "years_in_business": None,
        "annual_turnover": None,
        "monthly_profit": None,
        "gst_registered": None,
        "itr_filed_years": None,
        "shares_owned_fraction": None
    },
    "credit_profile": {
        "credit_score": 760,
        "pan_number": "ABCDE1234F",
        "has_default_history": False,
        "bankruptcy_history": False
    },
    "existing_obligations": {
        "loans": [
            {
                "loan_type": "car_loan",
                "lender": "HDFC Bank",
                "outstanding_amount": 250000,
                "monthly_emi": 12000,
                "remaining_tenure_months": 24,
                "is_regular": True
            }
        ],
        "credit_cards": [
            {
                "bank": "ICICI",
                "credit_limit": 200000,
                "current_outstanding": 35000,
                "monthly_min_payment": 3500
            }
        ],
        "other": [
            {
                "title": "Rent",
                "amount": 20000,
                "is_monthly": True
            }
        ],
        "total_monthly_emi": 12000,
        "total_credit_card_payment": 3500
    },
    "assets": {
        "savings_balance": 450000,
        "fixed_deposits": 200000,
        "investments": 300000,
        "owned_property": False,
        "property_value": 0,
        "owned_vehicles": True,
        "vehicle_value": 600000
    },
    "banking_relationship": {
        "has_salary_account": True,
        "salary_bank": "HDFC",
        "account_age_months": 60,
        "average_monthly_balance": 75000,
        "existing_customer": False,
        "existing_loan_with": None
    },
    "loan_request": {
        "loan_type": "home",
        "requested_amount": 3000000,
        "preferred_tenure_months": 240,
        "urgency": "moderate",
        "rate_preference": "floating",
        "prepayment_importance": "high"
    },
    "loan_specific_details": {
        "home_details": {
            "property_value": 3800000,
            "property_type": "apartment",
            "property_age": 0,
            "property_location": "Pune, Hinjewadi Phase 2",
            "construction_status": "ready_to_move",
            "builder_name": "Kolte Patil",
            "carpet_area_sq_ft": 850,
            "is_first_home": True,
            "down_payment_available": 800000,
            "has_co_applicant": True,
            "co_applicant_relation": "spouse",
            "co_applicant_income": 45000,
            "co_applicant_credit_score": 720
        },
        "car_details": {
            "vehicle_type": "new",
            "manufacturer": "Hyundai",
            "model": "Creta SX",
            "variant": "Petrol AT",
            "on_road_price": 1800000,
            "ex_showroom_price": 1650000,
            "registration_charges": 150000,
            "vehicle_age": 0,
            "kms_driven": 0,
            "down_payment_available": 300000,
            "has_trade_in": False,
            "trade_in_value": 0
        },
        "personal_details": {
            "purpose": "home_renovation",
            "purpose_description": "Kitchen and bathroom upgrade",
            "is_urgent": False,
            "has_collateral": False
        },
        "education_details": {
            "course_level": "postgraduate",
            "course_name": "MBA",
            "specialization": "Finance",
            "institution_name": "XLRI Jamshedpur",
            "institution_ranking": "premier",
            "institution_type": "private",
            "country": "india",
            "course_duration_months": 24,
            "total_course_fees": 2500000,
            "year_of_admission": 2024,
            "has_admission_letter": True,
            "has_scholarship": False,
            "scholarship_amount": 0,
            "co_applicant_available": True,
            "co_applicant_relation": "father",
            "co_applicant_age": 58,
            "co_applicant_income": 80000,
            "co_applicant_employment": "salaried"
        }
    },
    "life_context": {
        "marriage_planned_months": None,
        "children_planned_months": 24,
        "job_change_likely": False,
        "relocation_likely": False,
        "major_expenses_planned": [
            {
                "type": "vehicle_purchase",
                "timeline_months": 36,
                "estimated_amount": 1200000
            }
        ]
    },
    "preferences": {
        "financial_literacy": "medium",
        "risk_appetite": "moderate",
        "preferred_tenure_flexibility": "moderate",
        "prepayment_intention": "yes_if_bonus",
        "communication_preference": "email"
    },
    "metadata": {
        "source": "web_application",
        "referral_code": None,
        "utm_source": "google",
        "utm_medium": "cpc",
        "session_duration_seconds": 420,
        "pages_visited": 8,
        "calculator_used": True
    }
}