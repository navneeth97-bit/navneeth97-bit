import requests

def test_xss(url):
    payloads = ["<script>alert('XSS')</script>", "<img src='x' onerror='alert(1)'>"]
    for payload in payloads:
        test_url = f"{url}?q={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            return "Vulnerable"
    return "Not Vulnerable"
