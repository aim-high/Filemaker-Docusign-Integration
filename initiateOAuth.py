# Purpose: Called by bash script getDocusignToken.sh. initiateOAuth.py opens a Firefox 
#	window to request an access code.The user has 15 seconds to authenticate themselves 
#	with Docusign. Once successful, the browser redirects user with a uri that contains 
#	the access code. When the countdown is done, this program captures the current 
#	window's url containing the access code. Next, initiateOAuth.py requests the OAuth 
#	token from Docusign. If successful, Docusign returns an access token and refresh token.
# Output: Access token to be copied and pasted in Filemaker's DocusignToken field. 
# Created by: Erica Ching (eching@aimhigh.org) on 10-17-2019
  
from selenium import webdriver
import time
import requests
import json
import os

# Get Authorization Code First - input the following in a browser
# Sample Response: 
# http://example.com/callback/?code=YOUR_AUTH_CODEbrowser = webdriver.Firefox()
browser.get('https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id=7c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&state=a39fh23hnf23&redirect_uri=http://example.com/callback/')
print("You have 15 seconds to authenticate...")
def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(timeformat, end='\r')
		time.sleep(1)
		t -= 1
	print('Copying access code from current Url...\n')
countdown(15)

redirect = browser.current_url
# print(redirect)

rlength = len(redirect)
# print(rlength)

start = 29
end = rlength - 22

# print('Requesting OAuth token using access code...\n')
authcode = redirect[start:end]
# print(redirect[start:end])

headers = {'Authorization': 'Basic {BASE64_COMBINATION_OF_INTEGRATION_AND_SECRET_KEYS}}
payload = {'grant_type':'authorization_code', 'code': authcode }
r = requests.post('https://account.docusign.com/oauth/token', data=payload, headers=headers)

#print(r.content)
OAuthTokens = r.content

# Parse json to get access token
j = json.loads(OAuthTokens)

# Prints Access Token on Terminal.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("  Copy and Paste token into Filemaker:\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(j["access_token"])


print("\n\nRefresh Token:")
refreshToken = j["refresh_token"]

# Run after obtaining Access and Refresh Token
headers = {'Authorization': 'Basic [BASE64_COMBINATION_OF_INTEGRATION_AND_SECRET_KEYS]}
payload = {'grant_type':'refresh_token', 'refresh_token': refreshToken }
r = requests.post('https://account.docusign.com/oauth/token', data=payload, headers=headers)
