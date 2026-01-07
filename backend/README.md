# techfiesta-fixandflex


## Installation

Currently, we're using Python 3.10.12. We might change it later depending on the needs of our libraries

Please create a virtual environment while installing!
```
python -m venv venv
```
Or, for Linux,
```
virtualenv venv
```

Activate your virtual environment (don't skip this step!)
For Windows cmd:
```
./venv/Scripts/activate
```
For Linux:
```
source venv/bin/activate
```

Then install requirements:
```
pip install -r requirements.txt
```

You will also need to store a valid Gemini API key in a file called .env in the following format:
```
GEMINI_API_KEY='<your-key-here>'
MONGODB_URI='....'
```
Contact Harshad if you don't know what to put for MONGODB_URI

## TO-DO

### Secondary Research
 - Get info about platforms like paisa-bazaar

### High-Level Design
 - Finalize structure and flow of recommendation engine
 - _The entire front-end_

### Implementation
 - Integration of MongoDB
 - Finish the basic class structure of rules and users
 - Implement some basic rules


## Tech Stack

Back-End  : Flask
Front-End : React
Database  : MongoDB