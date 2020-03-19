import requests

r = requests.get("https://bjmdata.com")
print(r.status_code)
print(r.ok)
