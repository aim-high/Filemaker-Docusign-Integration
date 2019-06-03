# USER INFO ENDPOINT REFERENCE
#
# Returns account info and baseURI needed to use Docusign API.
#
# Reference: https://developers.docusign.com/esign-rest-api/guides/authentication/user-info-endpoints

import requests

headers = {'Authorization': 'Bearer ACCESS_TOKEN'}
#payload = {'grant_type':'authorization_code', 'code': ''}

r = requests.get('https://account.docusign.com/oauth/userinfo', headers=headers)

print(r.content)