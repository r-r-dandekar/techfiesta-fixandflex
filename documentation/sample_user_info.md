## Sample User Information

User information is to be stored in a JSON object such as the one given below. The key names should exactly match these. 
As of now, the keys and information that will be available is not final, so not all the keys present in the sample will 
be guaranteed to be present in the actual data.

```
{
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
    "applicable": false,
    "businessType": null,
    "businessName": null,
    "yearsInBusiness": null,
    "annualTurnover": null,
    "monthlyProfit": null,
    "gstRegistered": null,
    "itrFiledYears": null
  },
  
  "creditProfile": {
    "creditScore": 760,
    "panNumber": "ABCDE1234F",
    "hasDefaultHistory": false,
    "bankruptcyHistory": false
  },
  
  "existingObligations": {
    "loans": [
      {
        "loanType": "car_loan",
        "lender": "HDFC Bank",
        "outstandingAmount": 250000,
        "monthlyEMI": 12000,
        "remainingTenureMonths": 24,
        "isRegular": true
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
    "ownedProperty": false,
    "propertyValue": 0,
    "ownedVehicles": true,
    "vehicleValue": 600000
  },
  
  "bankingRelationship": {
    "hasSalaryAccount": true,
    "salaryBank": "HDFC",
    "accountAgeMonths": 60,
    "averageMonthlyBalance": 75000,
    "existingCustomer": false,
    "existingLoanWith": null
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
      "isFirstHome": true,
      "downPaymentAvailable": 800000,
      "hasCoApplicant": true,
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
      "hasTradeIn": false,
      "tradeInValue": 0
    },
    
    "personalDetails": {
      "purpose": "home_renovation",
      "purposeDescription": "Kitchen and bathroom upgrade",
      "isUrgent": false,
      "hasCollateral": false
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
      "hasAdmissionLetter": true,
      "hasScholarship": false,
      "scholarshipAmount": 0,
      "coApplicantAvailable": true,
      "coApplicantRelation": "father",
      "coApplicantAge": 58,
      "coApplicantIncome": 80000,
      "coApplicantEmployment": "salaried"
    }
  },
  
  "lifeContext": {
    "marriagePlannedMonths": null,
    "childrenPlannedMonths": 24,
    "jobChangeLikely": false,
    "relocationLikely": false,
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
    "referralCode": null,
    "utmSource": "google",
    "utmMedium": "cpc",
    "sessionDurationSeconds": 420,
    "pagesVisited": 8,
    "calculatorUsed": true
  }
}
```

### Example: 
Currently, no guarantee that data will be available about whether the user has any major expenses planned. 
However, if this data _is_ collected, it will necessarily be stored in lifeContext.majorExpensesPlanned