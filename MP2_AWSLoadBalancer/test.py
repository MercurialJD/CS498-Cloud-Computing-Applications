import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
		'ip_address1': '3.92.206.227:5000',
		'ip_address2': '34.229.49.55:5000',
		'load_balancer' : 'MP2-LB-1947117426.us-east-1.elb.amazonaws.com',
		'submitterEmail': 'jundas2@illinois.edu',
		'secret': 'l38X8KwOIygXM15m'
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)