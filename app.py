from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    

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