import json, requests

refreshToken = ""

headers = {'Authorization': 'Basic {BASE64_COMBINATION_OF_INTEGRATION_AND_SECRET_KEYS}'}
payload = {'grant_type':'refresh_token', 'refresh_token': refreshToken }
refreshr = requests.post('https://account.docusign.com/oauth/token', data=payload, headers=headers)

newOAuthTokens = refreshr.content
newj = json.loads(newOAuthTokens)
# Prints Access Token on Terminal.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("  Copy and Paste token into Filemaker:\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(j["access_token"])
