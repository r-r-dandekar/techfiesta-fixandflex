## Sample User Information

User information is to be stored in a JSON object such as the one given below. The key names should exactly match these. 
As of now, the keys and information that will be available is not final, so not all the keys present in the sample will 
be guaranteed to be present in the actual data.

```
{
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
        "applicable": false,
        "business_type": null,
        "business_name": null,
        "years_in_business": null,
        "annual_turnover": null,
        "monthly_profit": null,
        "gst_registered": null,
        "itr_filed_years": null
    },
    "credit_profile": {
        "credit_score": 760,
        "pan_number": "ABCDE1234F",
        "has_default_history": false,
        "bankruptcy_history": false
    },
    "existing_obligations": {
        "loans": [
            {
                "loan_type": "car_loan",
                "lender": "HDFC Bank",
                "outstanding_amount": 250000,
                "monthly_emi": 12000,
                "remaining_tenure_months": 24,
                "is_regular": true
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
                "is_monthly": true
            }
        ],
        "total_monthly_emi": 12000,
        "total_credit_card_payment": 3500
    },
    "assets": {
        "savings_balance": 450000,
        "fixed_deposits": 200000,
        "investments": 300000,
        "owned_property": false,
        "property_value": 0,
        "owned_vehicles": true,
        "vehicle_value": 600000
    },
    "banking_relationship": {
        "has_salary_account": true,
        "salary_bank": "HDFC",
        "account_age_months": 60,
        "average_monthly_balance": 75000,
        "existing_customer": false,
        "existing_loan_with": null
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
            "is_first_home": true,
            "down_payment_available": 800000,
            "has_co_applicant": true,
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
            "has_trade_in": false,
            "trade_in_value": 0
        },
        "personal_details": {
            "purpose": "home_renovation",
            "purpose_description": "Kitchen and bathroom upgrade",
            "is_urgent": false,
            "has_collateral": false
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
            "has_admission_letter": true,
            "has_scholarship": false,
            "scholarship_amount": 0,
            "co_applicant_available": true,
            "co_applicant_relation": "father",
            "co_applicant_age": 58,
            "co_applicant_income": 80000,
            "co_applicant_employment": "salaried"
        }
    },
    "life_context": {
        "marriage_planned_months": null,
        "children_planned_months": 24,
        "job_change_likely": false,
        "relocation_likely": false,
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
        "referral_code": null,
        "utm_source": "google",
        "utm_medium": "cpc",
        "session_duration_seconds": 420,
        "pages_visited": 8,
        "calculator_used": true
    }
}
```

### Example: 
Currently, no guarantee that data will be available about whether the user has any major expenses planned. 
However, if this data _is_ collected, it will necessarily be stored in lifeContext.majorExpensesPlanned