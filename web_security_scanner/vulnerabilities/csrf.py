import requests

def test_csrf(url):
    csrf_token_missing_url = f"{url}/submit?user_id=1"
    response = requests.get(csrf_token_missing_url)
    if response.status_code == 200:
        return "Vulnerable"
    return "Not Vulnerable"
