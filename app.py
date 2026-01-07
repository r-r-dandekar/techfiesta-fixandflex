from flask import Flask, jsonify
from flask_cors import CORS
from utils.database import get_db
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

loan_schemes = []

@app.route("/")
def home():
    return jsonify({
        'message': 'Loan Eligibility API',
        'status': 'running'
    })

@app.route("/testing")
def testing():
    from core.user import User
    from core.rules import CreditScoreFloor

    u = User()
    u.set_sample_info()
    r1 = CreditScoreFloor("R1", "CreditFloor", 700)
    r2 = CreditScoreFloor("R2", "CreditFloor", 900)
    print(f"Rule 1 satisfied: {r1.satisfied(u)}")
    print(f"Rule 2 satisfied: {r2.satisfied(u)}")

    return "<p>Testing, be sure to check the terminal!</p>"

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
    

@app.route("/test_foir")
def test_foir():
    from core.user import User
    from core.rules import FOIR

    u = User()
    u.set_sample_info()
    r1 = FOIR("R1", "FOIR", 0.5)
    r2 = FOIR("R2", "FOIR", 0.1)
    print(f"Rule 1 satisfied: {r1.satisfied(u)}")
    print(f"Rule 2 satisfied: {r2.satisfied(u)}")

    return "<p>Testing, be sure to check the terminal!</p>"
