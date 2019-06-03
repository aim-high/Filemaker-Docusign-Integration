# AUTHORIZATION CODE GRANT
#
# Run after obtaining Access and Refresh Token by running getAccessToken.py

import requests

headers = {'Authorization': 'Basic BASE64_COMBINATION_OF_INTEGRATOR_AND_SECRET_KEYS'}
payload = {'grant_type':'refresh_token', 'refresh_token': 'REFRESH_TOKEN'}
r = requests.post('https://account.docusign.com/oauth/token', data=payload, headers=headers)

print(r.content)