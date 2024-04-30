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
