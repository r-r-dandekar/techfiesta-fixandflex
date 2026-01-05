class User:

    # This is a dictionary containing the user's details in the format given at: documenation/sample_user_info.md
    info: dict

    # For testing, to set the user's info to the sample data (copied from documenation/sample_user_info.md)
    def set_sample_info(self):
        self.info = {
            "applicationId": "APP_2024_001234",
            "timestamp": "2024-01-04T10:30:00Z",
            
            "personalInfo": {
                "age": 32,
                "dateOfBirth": "1992-05-15",
                "gender": "male",
                "maritalStatus": "married",
                "dependents": 1,
                "education": "graduate",
                "pincode": "411001",
                "city": "Pune",
                "state": "Maharashtra",
                "cityTier": 1
            },
            
            "employment": {
                "type": "salaried",
                "employerName": "Infosys Ltd",
                "employerType": "MNC",
                "industry": "IT",
                "yearsInCurrentJob": 5.5,
                "totalWorkExperience": 8,
                "monthlyGrossSalary": 125000,
                "monthlyNetSalary": 95000,
                "otherMonthlyIncome": 5000
            },
            
            "businessInfo": {
                "applicable": False,
                "businessType": None,
                "businessName": None,
                "yearsInBusiness": None,
                "annualTurnover": None,
                "monthlyProfit": None,
                "gstRegistered": None,
                "itrFiledYears": None
            },
            
            "creditProfile": {
                "creditScore": 760,
                "panNumber": "ABCDE1234F",
                "hasDefaultHistory": False,
                "bankruptcyHistory": False
            },
            
            "existingObligations": {
                "loans": [
                {
                    "loanType": "car_loan",
                    "lender": "HDFC Bank",
                    "outstandingAmount": 250000,
                    "monthlyEMI": 12000,
                    "remainingTenureMonths": 24,
                    "isRegular": True
                }
                ],
                "creditCards": [
                {
                    "bank": "ICICI",
                    "creditLimit": 200000,
                    "currentOutstanding": 35000,
                    "monthlyMinPayment": 3500
                }
                ],
                "totalMonthlyEMI": 12000,
                "totalCreditCardPayment": 3500
            },
            
            "assets": {
                "savingsBalance": 450000,
                "fixedDeposits": 200000,
                "investments": 300000,
                "ownedProperty": False,
                "propertyValue": 0,
                "ownedVehicles": True,
                "vehicleValue": 600000
            },
            
            "bankingRelationship": {
                "hasSalaryAccount": True,
                "salaryBank": "HDFC",
                "accountAgeMonths": 60,
                "averageMonthlyBalance": 75000,
                "existingCustomer": False,
                "existingLoanWith": None
            },
            
            "loanRequest": {
                "loanType": "home",
                "requestedAmount": 3000000,
                "preferredTenureMonths": 240,
                "urgency": "moderate",
                "ratePreference": "floating",
                "prepaymentImportance": "high"
            },
            
            "loanSpecificDetails": {
                "homeDetails": {
                "propertyValue": 3800000,
                "propertyType": "apartment",
                "propertyAge": 0,
                "propertyLocation": "Pune, Hinjewadi Phase 2",
                "constructionStatus": "ready_to_move",
                "builderName": "Kolte Patil",
                "carpetAreaSqFt": 850,
                "isFirstHome": True,
                "downPaymentAvailable": 800000,
                "hasCoApplicant": True,
                "coApplicantRelation": "spouse",
                "coApplicantIncome": 45000,
                "coApplicantCreditScore": 720
                },
                
                "carDetails": {
                "vehicleType": "new",
                "manufacturer": "Hyundai",
                "model": "Creta SX",
                "variant": "Petrol AT",
                "onRoadPrice": 1800000,
                "exShowroomPrice": 1650000,
                "registrationCharges": 150000,
                "vehicleAge": 0,
                "kmsDriven": 0,
                "downPaymentAvailable": 300000,
                "hasTradeIn": False,
                "tradeInValue": 0
                },
                
                "personalDetails": {
                "purpose": "home_renovation",
                "purposeDescription": "Kitchen and bathroom upgrade",
                "isUrgent": False,
                "hasCollateral": False
                },
                
                "educationDetails": {
                "courseLevel": "postgraduate",
                "courseName": "MBA",
                "specialization": "Finance",
                "institutionName": "XLRI Jamshedpur",
                "institutionRanking": "premier",
                "institutionType": "private",
                "country": "india",
                "courseDurationMonths": 24,
                "totalCourseFees": 2500000,
                "yearOfAdmission": 2024,
                "hasAdmissionLetter": True,
                "hasScholarship": False,
                "scholarshipAmount": 0,
                "coApplicantAvailable": True,
                "coApplicantRelation": "father",
                "coApplicantAge": 58,
                "coApplicantIncome": 80000,
                "coApplicantEmployment": "salaried"
                }
            },
            
            "lifeContext": {
                "marriagePlannedMonths": None,
                "childrenPlannedMonths": 24,
                "jobChangeLikely": False,
                "relocationLikely": False,
                "majorExpensesPlanned": [
                {
                    "type": "vehicle_purchase",
                    "timelineMonths": 36,
                    "estimatedAmount": 1200000
                }
                ]
            },
            
            "preferences": {
                "financialLiteracy": "medium",
                "riskAppetite": "moderate",
                "preferredTenureFlexibility": "moderate",
                "prepaymentIntention": "yes_if_bonus",
                "communicationPreference": "email"
            },
            
            "metadata": {
                "source": "web_application",
                "referralCode": None,
                "utmSource": "google",
                "utmMedium": "cpc",
                "sessionDurationSeconds": 420,
                "pagesVisited": 8,
                "calculatorUsed": True
            }
        }