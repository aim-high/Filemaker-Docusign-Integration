# AUTHORIZATION CODE GRANT 
# 
# Get Authorization Code First - input the following in a browser
# https://account.docusign.com/oauth/auth?response_type=code&scope=signature%20extended&client_id=[INTEGRATOR KEY]]&state=YOUR_CUSTOM_STATE&redirect_uri=https://127.0.0.1:3000
#
# Sample Response: 
# http://example.com/callback/?code=YOUR_AUTH_CODE
import requests

headers = {'Authorization': 'Basic BASE64_COMBINATION_OF_INTEGRATOR_AND_SECRET_KEYS'}
payload = {'grant_type':'authorization_code', 'code': 'YOUR_AUTH_CODE_SEE_ABOVE_SAMPLE'}'
r = requests.post('https://account.docusign.com/oauth/token', data=payload, headers=headers)

print(r.content)
