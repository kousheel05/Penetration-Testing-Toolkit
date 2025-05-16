import requests

# Common simple XSS payloads to test
XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"'><script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>",
]

def scan_url_for_xss(url):
    vulnerable = []
    for payload in XSS_PAYLOADS:
        # Append payload as a query parameter "test"
        test_url = url
        if "?" in url:
            test_url += f"&test={payload}"
        else:
            test_url += f"?test={payload}"

        try:
            resp = requests.get(test_url, timeout=3)
            # Basic reflected check: payload is in response content
            if payload in resp.text:
                vulnerable.append({
                    "url": test_url,
                    "payload": payload
                })
        except requests.RequestException:
            continue

    return vulnerable
