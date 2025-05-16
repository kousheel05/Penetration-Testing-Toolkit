import requests

def fuzz_directories(base_url, wordlist):
    found = []
    for word in wordlist:
        url = f"{base_url.rstrip('/')}/{word.strip()}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code in [200, 301, 302]:
                found.append({
                    "url": url,
                    "status_code": response.status_code
                })
        except requests.RequestException:
            continue
    return found
