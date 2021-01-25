import requests

headers ={}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExOTM2OTYzLCJqdGkiOiIwZTY3YjMwODExYmI0YmIyOTA5ZTFkOWQ0NjJhYWU1MiIsInVzZXJfaWQiOjJ9.8n7Cld3WKnYe1ETxBR0Cr3cd7VipSTiLB1YI-JiJQ-0'

r = requests.get('http://127.0.0.1:8000/api/ifsc/HDFC0000053',headers=headers)
r2 = requests.get('http://127.0.0.1:8000/api/branches/Bangalore/HDFC Bank',headers=headers)
print(r.text)
print(r2.text)
