from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from pydantic import BaseModel
from core.sample_eligible_engine import evaluate_hard_rules
from core.sample_price_engine import price_loan   # Phase-2 engine we discussed
from utils.database import get_db_wrapper
from core.loan_scheme import LoanScheme
from core.rules.ruleset import RuleSet

from utils.database import get_db, get_db_wrapper, Database
from utils.logs import *


load_dotenv()

app = Flask(__name__)
CORS(app)

loan_schemes = []

db_wrapper = get_db_wrapper()

@app.route("/")
def home():
    return jsonify({
        'message': 'Loan Eligibility API',
        'status': 'running'
    })

# @app.route("/testing_credit_floor")
# def testing():
#     from core.user import User
#     from core.rules import CreditScoreFloor
#
#     u = User()
#     u.set_sample_info()
#     r1 = CreditScoreFloor("R1", 700)
#     r2 = CreditScoreFloor("R2", 900)
#     log_info(f"Rule 1 satisfied: {r1.satisfied(u)}")
#     log_info(f"Rule 2 satisfied: {r2.satisfied(u)}")
#
#     return "<p>Testing, be sure to check the terminal!</p>"
@app.route("/api/phase1/eligibility", methods=["POST"])
def phase1_eligibility():
    payload = request.json
    application = payload["user_application"]
    loan_type = payload["loan_type"]

    products = db_wrapper.fetch_loan_schemes_by_type(loan_type)
    results = []
    for product in products:
        result = evaluate_hard_rules(application, product)
        results.append({
            "product_id": product["product_id"],
            "eligible": result["eligible"],
            "failed_hard_rules": result["failed_hard_rules"]
        })

    return jsonify({
        "application_id": application["application_id"],
        "loan_type": loan_type,
        "results": results
    })
@app.route("/api/phase2/eligibility-and-pricing", methods=["POST"])
def phase2_eligibility_and_pricing():
    payload = request.json

    application = payload["user_application"]
    loan_type = payload["loan_type"]

    db_wrapper = get_db_wrapper()

    # Fetch active loan schemes by type
    products = db_wrapper.fetch_loan_schemes_by_type(loan_type)

    results = []

    for product in products:
        # ---------------- PHASE 1: HARD RULES ----------------
        eligibility_result = evaluate_hard_rules(application, product)

        response_item = {
            "product_id": product.get("product_id"),
            "lender_id": product.get("lender_id"),
            "product_name": product.get("product_info", {}).get("name"),
            "eligible": eligibility_result["eligible"],
            "failed_hard_rules": eligibility_result["failed_hard_rules"]
        }

        # ---------------- PHASE 2: PRICING ----------------
        if eligibility_result["eligible"]:
            pricing = price_loan(application, product)

            response_item["pricing"] = {
                "base_rate": pricing["base_rate"],
                "final_rate": pricing["final_rate"],
                "emi": pricing["emi"],
                "rate_adjustments": pricing["rate_adjustments"],
                "tenure_months": application["loan_request"]["preferred_tenure_months"],
                "loan_amount": application["loan_request"]["requested_amount"]
            }
        else:
            response_item["pricing"] = None

        results.append(response_item)

    return jsonify({
        "application_id": application["application_id"],
        "loan_type": loan_type,
        "results": results
    })

@app.route('/health')
def health():
    """Check MongoDB connection"""
    try:
        db = get_db()
        db.command('ping')
        
        collections = db.list_collection_names()
        
        return jsonify({
            'status': 'healthy',
            'database': 'connected',
            'collections': collections,
            'db_name': db.name
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'database': 'disconnected',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
    

# @app.route("/insert_test_scheme_data")
# def insert_test_scheme_data():
#     from core.rules import CreditScoreFloor, FOIR
#     rules = [FOIR(rule_id="R1", max_foir=0.5, emi=500), CreditScoreFloor(rule_id="R2", min_score=700)]
#     rule_set = RuleSet(hard_rules=rules, soft_rules=[])
#     loan_scheme = LoanScheme(loan_id="scheme1", rule_set=rule_set, name="SchemeName", description="SomeDescription")
#
#     try:
#         db_wrapper.insert_loan_scheme(loan_scheme)
#     except Exception as e:
#         return f"Oops! Something went wrong! {str(e)}"
#     return "<p>Seems to have worked!</p>"



@app.route("/get_all_scheme_data")
def get_all_scheme_data():
    try:
        load_loan_schemes()
        for loan_scheme in loan_schemes:
            for rule in loan_scheme.rule_set:
                print(rule)
    except Exception as e:
        return f"Oops! Something went wrong! {str(e)}"
    return "<p>Testing, be sure to check the terminal!</p>"


def load_loan_schemes():
    loan_schemes = db_wrapper.fetch_all_loan_schemes()