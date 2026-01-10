def apply_band_rule(value, bands):
    for band in bands:
        min_v = band.get("min", float("-inf"))
        max_v = band.get("max", float("inf"))
        if min_v <= value <= max_v:
            return band.get("adjustment", 0)
    return 0

def clamp(value, min_v, max_v):
    return max(min_v, min(value, max_v))

def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / 12 / 100
    if monthly_rate == 0:
        return round(principal / tenure_months, 2)

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** tenure_months
        / ((1 + monthly_rate) ** tenure_months - 1)
    )
    return round(emi, 2)

def price_loan(application: dict, product: dict) -> dict:
    base_rate = product["interest_rates"]["base_rate"]
    rate = base_rate

    adjustments = []

    csr = product["common_soft_rules"]
    tsr = product["type_specific_soft_rules"]
    loan_type = product["product_info"]["product_type"]
    details = application["loan_specific_details"]["details"]

    # ================= COMMON SOFT RULES =================

    # Employer category
    if csr.get("employer_category", {}).get("enabled"):
        employer = application.get("employment", {}).get("salaried_details", {}).get("employer_type")
        adj = csr["employer_category"]["adjustments"].get(employer)
        if adj is not None:
            rate += adj
            adjustments.append({"rule": "employer_category", "impact": adj})

    # Credit score band
    if csr.get("cibil_score_band", {}).get("enabled"):
        score = application["credit_profile"]["credit_score"]
        adj = apply_band_rule(score, csr["cibil_score_band"]["bands"])
        rate += adj
        adjustments.append({"rule": "credit_score_band", "impact": adj})

    # FOIR comfort
    if csr.get("foir_comfort", {}).get("enabled"):
        foir = application["computed_metrics"]["foir"]
        adj = apply_band_rule(foir, csr["foir_comfort"]["bands"])
        rate += adj
        adjustments.append({"rule": "foir", "impact": adj})

    # Location tier
    if csr.get("location_tier", {}).get("enabled"):
        tier = f"tier_{application['personal_info']['city_tier']}"
        adj = csr["location_tier"]["adjustments"].get(tier)
        if adj is not None:
            rate += adj
            adjustments.append({"rule": "location_tier", "impact": adj})

    # Banking relationship
    if csr.get("banking_relationship", {}).get("enabled"):
        bank = application.get("banking_relationship", {}).get("primary_bank", {})
        if bank.get("has_salary_account"):
            adj = csr["banking_relationship"]["has_salary_account"]
            rate += adj
            adjustments.append({"rule": "salary_account", "impact": adj})

        if bank.get("average_monthly_balance", 0) >= csr["banking_relationship"]["high_average_balance"]["threshold"]:
            adj = csr["banking_relationship"]["high_average_balance"]["adjustment"]
            rate += adj
            adjustments.append({"rule": "high_avg_balance", "impact": adj})

    # Gender benefit
    if csr.get("gender", {}).get("enabled"):
        if application["personal_info"].get("gender") == "female":
            adj = csr["gender"]["female_primary_applicant"]
            rate += adj
            adjustments.append({"rule": "female_primary", "impact": adj})

    # Loan amount bracket
    if csr.get("loan_amount_bracket", {}).get("enabled"):
        amount = application["loan_request"]["requested_amount"]
        adj = apply_band_rule(amount, csr["loan_amount_bracket"]["bands"])
        rate += adj
        adjustments.append({"rule": "loan_amount", "impact": adj})

    # ================= TYPE-SPECIFIC SOFT RULES =================

    # ---------- HOME ----------
    if loan_type == "home":

        # First home buyer
        if tsr.get("first_home_buyer", {}).get("enabled") and details.get("is_first_home"):
            if application["loan_request"]["requested_amount"] <= tsr["first_home_buyer"]["max_loan_amount_for_benefit"]:
                adj = tsr["first_home_buyer"]["discount"]
                rate += adj
                adjustments.append({"rule": "first_home_buyer", "impact": adj})

        # LTV penalty
        if tsr.get("ltv_penalty", {}).get("enabled"):
            adj = apply_band_rule(details["ltv_ratio"], tsr["ltv_penalty"]["bands"])
            rate += adj
            adjustments.append({"rule": "ltv_penalty", "impact": adj})

        # Property characteristics
        pc = tsr.get("property_characteristics", {})
        if pc.get("enabled"):

            # Property age
            adj = apply_band_rule(details["property_age_years"], pc["property_age"])
            rate += adj
            adjustments.append({"rule": "property_age", "impact": adj})

            # Construction status
            cs = pc["construction_status"].get(details.get("construction_status"))
            if cs is not None:
                rate += cs
                adjustments.append({"rule": "construction_status", "impact": cs})

            # Builder reputation
            builder_tier = details.get("builder", {}).get("tier")
            adj = pc["builder_reputation"].get(builder_tier)
            if adj is not None:
                rate += adj
                adjustments.append({"rule": "builder_reputation", "impact": adj})

    # ---------- PERSONAL ----------
    elif loan_type == "personal":

        if tsr.get("loan_purpose", {}).get("enabled"):
            purpose = details.get("purpose_category")
            adj = tsr["loan_purpose"]["purposes"].get(purpose)
            if adj is not None:
                rate += adj
                adjustments.append({"rule": "loan_purpose", "impact": adj})

        if tsr.get("urgency", {}).get("enabled"):
            adj = tsr["urgency"].get(application["loan_request"]["urgency"])
            if adj is not None:
                rate += adj
                adjustments.append({"rule": "urgency", "impact": adj})

        if tsr.get("collateral_offered", {}).get("enabled"):
            collateral = details.get("collateral", {}).get("type", "none")
            adj = tsr["collateral_offered"].get(collateral)
            if adj is not None:
                rate += adj
                adjustments.append({"rule": "collateral", "impact": adj})

    # ---------- EDUCATION ----------
    elif loan_type == "education":

        if tsr.get("institution_tier", {}).get("enabled"):
            adj = tsr["institution_tier"].get(details["institution"]["tier"])
            rate += adj
            adjustments.append({"rule": "institution_tier", "impact": adj})

        if tsr.get("course_type", {}).get("enabled"):
            adj = tsr["course_type"].get(details["course"]["category"])
            rate += adj
            adjustments.append({"rule": "course_type", "impact": adj})

        if tsr.get("destination_country", {}).get("enabled"):
            adj = tsr["destination_country"].get(details["institution"]["country"])
            rate += adj
            adjustments.append({"rule": "destination_country", "impact": adj})

        if tsr.get("scholarship", {}).get("enabled"):
            adj = tsr["scholarship"].get(details["financials"]["scholarship_type"])
            rate += adj
            adjustments.append({"rule": "scholarship", "impact": adj})

        if tsr.get("academic_performance", {}).get("enabled"):
            adj = tsr["academic_performance"].get(details["academic_background"]["performance_category"])
            rate += adj
            adjustments.append({"rule": "academic_performance", "impact": adj})

    # ================= AGGREGATION & ROUNDING =================

    agg = product["soft_rules_aggregation"]
    total_adj = rate - base_rate
    total_adj = clamp(total_adj, agg["max_negative_adjustment"], agg["max_positive_adjustment"])
    rate = base_rate + total_adj

    # Clamp product limits
    rate = clamp(rate, product["interest_rates"]["min_rate"], product["interest_rates"]["max_rate"])

    # Proper rounding
    rounding = agg["rounding"]
    rate = round(round(rate / rounding) * rounding, 2)

    # ================= EMI =================

    emi = calculate_emi(
        application["loan_request"]["requested_amount"],
        rate,
        application["loan_request"]["preferred_tenure_months"]
    )

    return {
        "base_rate": base_rate,
        "final_rate": rate,
        "emi": emi,
        "rate_adjustments": [a for a in adjustments if a["impact"] != 0]
    }
