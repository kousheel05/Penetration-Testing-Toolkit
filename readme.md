# PENETRATION TESTING TOOLKIT

*COMAPNY*: CODTECH IT SOLUTIONS

*NAME*: MADIPADIGA KOUSHEEL

*INTERN ID*: CT04DL611

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4WEEKS

*MENTOR*: NEELA SANTOSH 

# PENETRATION TESTING TOOLKIT DESCRIPTION
This Penetration Testing Toolkit is a modular, web-based ethical hacking and security testing tool developed using Python (Flask) for the backend and HTML/CSS for the frontend. The application provides a central interface for performing common penetration testing techniques such as port scanning, brute-force testing, directory fuzzing, XSS scanning, SQL injection testing, and WHOIS lookups.
The toolkit is aimed at cybersecurity learners, ethical hackers, developers, and system administrators who want to audit and secure their networks or web applications. It abstracts complex concepts into easy-to-use web forms, returning practical insights in real-time. Below is a breakdown of the toolkit’s internal logic, functionality, and usage.

# MODULE BREAKDOWN AND LOGIC
1.Port Scanner
Logic: Uses Python’s socket library to attempt TCP connections to each port in a given range on a target host. If a connection is successful, the port is marked as open.
Use Case: Identifying open ports helps detect services like FTP (port 21), SSH (port 22), HTTP (port 80) that may expose vulnerabilities.

2.Brute Force Simulator
Logic: Accepts lists of usernames and passwords and attempts all combinations. It simulates a brute-force attack by comparing each combination to a pre-defined valid pair (admin:admin).
Use Case: Helps developers understand the importance of strong passwords and rate-limiting authentication systems.

3.Directory Fuzzer
Logic: Takes a base URL and a list of common paths (admin, login, uploads, etc.). It appends each path to the base and performs an HTTP GET request. If the status code is 200 (OK), 301 (Redirect), or 403 (Forbidden), it’s considered a found directory.
Use Case: Helps uncover hidden web resources that might expose sensitive files or admin panels.

4.XSS Scanner
Logic: Injects various JavaScript payloads (like <script>alert(1)</script>) into a URL’s query string and checks if the payload is reflected in the server response. This is a simple reflected XSS detection mechanism.
Use Case: Detects whether a site is vulnerable to XSS attacks that can allow an attacker to execute scripts in the context of another user’s browser, potentially stealing cookies or session tokens.

5.SQL Injection Tester
Logic: Appends known SQL injection payloads (e.g., ' OR 1=1--) to query parameters in the URL. It scans the returned HTML for SQL error patterns like syntax error, mysql, or sqlite.
Use Case: Helps identify whether user input in the application is improperly sanitized, allowing attackers to manipulate the database and potentially extract or delete sensitive data.

6.WHOIS Lookup
Logic: Uses the python-whois library to retrieve domain registration information, such as registrar, creation date, expiry date, nameservers, and admin contact details.
Use Case: Useful in reconnaissance to discover ownership, domain history, and potential registration expiration that could be exploited by attackers.

# FRONTEND $ ROUTING
app.py: Flask app that defines routes for each module (/scan_ports, /brute_force, /fuzz, /xss_scan, /sqli, /whois).
templates/index.html: Renders all input forms and results using Jinja2 templating.
static/style.css: Dark-themed CSS styling for a modern hacker-style UI.


# APPLICABILITY IN REAL WORLD SCENARIOS
This toolkit is ideal for:
Training labs: Simulating attacks on controlled environments (e.g., DVWA, OWASP Juice Shop).
Web application testing: Spotting XSS or SQLi before malicious actors do.
Internal audits: Quickly scanning ports and services in local or remote infrastructures.
Reconnaissance: Gathering public information on targets via WHOIS.
It can also be expanded by adding tools like:
Hash cracker
Subdomain enumerator
CSRF detector
SSRF scanner
Report generator (PDF/HTML)

# OUTPUTS
![Image](https://github.com/user-attachments/assets/9d0f3992-4a4e-4f42-8a2e-e4eeeee8986c)

![Image](https://github.com/user-attachments/assets/a4f89281-6d4f-48b1-8fc6-8e521e81a56c)

![Image](https://github.com/user-attachments/assets/9054034d-4622-4d31-be0c-599763426cbd)

![Image](https://github.com/user-attachments/assets/97fb6b24-c28d-419b-8ed3-0e31431daf7c)

![Image](https://github.com/user-attachments/assets/29942fac-4658-4950-afb4-983cb9a91fc0)

![Image](https://github.com/user-attachments/assets/bbc99c5c-bfb7-4efc-95fe-8982d8dd4839)


