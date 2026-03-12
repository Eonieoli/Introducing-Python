import requests

resp = requests.get('http://example.com')
print(resp)
print(resp.status_code)
print(resp.text[:50])