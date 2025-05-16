from flask import Flask, render_template, request
from modules import port_scanner, brute_force
from modules import directory_fuzzer
from modules import xss_scanner
from modules import whois_lookup
from modules import sql_injection

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    host = request.form["host"]
    start_port = int(request.form["start_port"])
    end_port = int(request.form["end_port"])
    results = port_scanner.scan_ports(host, start_port, end_port)
    return render_template("index.html", port_results=results)

@app.route("/brute", methods=["POST"])
def brute():
    target = request.form["target"]
    usernames = request.form["usernames"].split(",")
    passwords = request.form["passwords"].split(",")
    results = brute_force.brute_force(target, usernames, passwords)
    return render_template("index.html", brute_results=results)

@app.route("/fuzz", methods=["POST"])
def fuzz():
    base_url = request.form["base_url"]
    wordlist = request.form["wordlist"].split(",")
    results = directory_fuzzer.fuzz_directories(base_url, wordlist)
    return render_template("index.html", fuzz_results=results)

@app.route("/xss_scan", methods=["POST"])
def xss_scan():
    url = request.form["url"]
    results = xss_scanner.scan_url_for_xss(url)
    return render_template("index.html", xss_results=results)

@app.route("/whois", methods=["POST"])
def whois():
    domain = request.form["domain"]
    result = whois_lookup.lookup_domain(domain)
    return render_template("index.html", whois_result=result)

@app.route("/sqli", methods=["POST"])
def sqli():
    url = request.form["url"]
    results = sql_injection.test_sql_injection(url)
    return render_template("index.html", sqli_results=results)


if __name__ == "__main__":
    app.run(debug=True)
