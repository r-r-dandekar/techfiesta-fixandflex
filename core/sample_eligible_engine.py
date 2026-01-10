def evaluate_hard_rules(application, product):
    failures = []

    loan_type = product["product_info"]["product_type"]

    # ---------------- COMMON HARD RULES ----------------

    credit_rule = product["common_hard_rules"]["credit_score"]
    score = application["credit_profile"]["credit_score"]
    min_score = credit_rule["min_score"]

    if application.get("co_applicant", {}).get("applicable"):
        min_score = credit_rule.get("min_score_with_co_applicant", min_score)

    if score < min_score:
        failures.append({
            "rule": "credit_score",
            "reason": f"{score} < {min_score}"
        })

    foir_rule = product["common_hard_rules"]["foir"]
    foir = application["computed_metrics"]["foir"]
    income = application["computed_metrics"]["monthly_income_total"]

    max_foir = foir_rule["max_foir"]
    if income >= foir_rule["high_income_threshold"]:
        max_foir = foir_rule["max_foir_high_income"]

    if foir > max_foir:
        failures.append({
            "rule": "foir",
            "reason": f"{foir} > {max_foir}"
        })

    age_rule = product["common_hard_rules"]["age"]
    emp_type = application["employment"]["type"]
    maturity_age = application["computed_metrics"]["age_at_loan_maturity"]


    if loan_type != "education":
        if emp_type in age_rule["max_age_at_maturity"]:
            max_age = age_rule["max_age_at_maturity"][emp_type]

            if maturity_age > max_age:
                failures.append({
                    "rule": "age",
                    "reason": f"{maturity_age} > {max_age}"
                })

    # ---------------- TYPE SPECIFIC HARD RULES ----------------

    details = application["loan_specific_details"]["details"]

    if loan_type == "home":
        ltv_rule = product["type_specific_hard_rules"]["ltv"]
        ltv = details["ltv_ratio"]
        is_first = details["is_first_home"]

        max_ltv = ltv_rule["max_ltv_first_home_buyer"] if is_first else ltv_rule["max_ltv"]
        if ltv > max_ltv:
            failures.append({"rule": "ltv", "reason": f"{ltv} > {max_ltv}"})

        dp_rule = product["type_specific_hard_rules"]["down_payment"]
        if details["down_payment_percent"] < (
            dp_rule["min_down_payment_percent_first_home"] if is_first else dp_rule["min_down_payment_percent"]
        ):
            failures.append({"rule": "down_payment", "reason": "Insufficient down payment"})

        prop_rule = product["type_specific_hard_rules"]["property"]
        if details["legal_status"] != prop_rule["legal_status_required"]:
            failures.append({"rule": "property_legal", "reason": "Legal status invalid"})

        if details["property_age_years"] > prop_rule["max_property_age_years"]:
            failures.append({"rule": "property_age", "reason": "Property too old"})

    elif loan_type == "personal":
        ratio_rule = product["type_specific_hard_rules"]["loan_amount_income_ratio"]
        annual_income = application["computed_metrics"]["monthly_income_total"] * 12
        if application["loan_request"]["requested_amount"] / annual_income > ratio_rule["max_loan_to_annual_income"]:
            failures.append({"rule": "loan_income_ratio", "reason": "Exceeded ratio"})

        tenure_rule = product["type_specific_hard_rules"]["min_loan_tenure"]
        if application["loan_request"]["preferred_tenure_months"] < tenure_rule["min_tenure_months"]:
            failures.append({"rule": "tenure", "reason": "Tenure too short"})

    elif loan_type == "education":
        course = details["course"]
        course_rule = product["type_specific_hard_rules"]["course_eligibility"]

        if course["level"] not in course_rule["allowed_course_levels"]:
            failures.append({"rule": "course_level", "reason": "Course level not allowed"})

        institution = details["institution"]
        if not institution["accredited"]:
            failures.append({"rule": "institution", "reason": "Institution not accredited"})

        admission = details["admission"]
        if not admission["has_admission_letter"]:
            failures.append({"rule": "admission", "reason": "Admission letter missing"})

        co_rule = product["type_specific_hard_rules"]["co_applicant"]
        if not application["co_applicant"]["applicable"]:
            failures.append({"rule": "co_applicant", "reason": "Co-applicant mandatory"})

    return {
        "eligible": len(failures) == 0,
        "failed_hard_rules": failures
    }
