import requests
url   = 'http://example.tld'
payload = { 'key' : 'val' }
headers = {}
res = requests.post(url, data=payload, headers=headers)
print (res)
