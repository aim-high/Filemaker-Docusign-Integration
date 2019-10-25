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



# SAMPLE 
POST https://account-d.docusign.com/oauth/token
Authorization: Basic BASE64_COMBINATION_OF_INTEGRATION_AND_SECRET_KEYS

grant_type=refresh_token&refresh_token=YOUR_REFRESH_TOKEN

curl --header "Authorization: Basic MjMwNTQ2.....Y4MmM3YmYyNzZlOQ==" --data "grant_type=refresh_token&refresh_token=ey4fd.....3d31d` --request POST https://account-d.docusign.com/oauth/token
