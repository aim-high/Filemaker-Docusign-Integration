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

browser = webdriver.Firefox()
browser.get('https://account.docusign.com/oauth/auth?response_type=code&scope=signature%20extended&client_id=3a1a96f5-2ef2-43b6-b756-1723fa5385ab&state=bobby%20newport&redirect_uri=https://127.0.0.1:3000')

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

headers = {'Authorization': 'Basic [PASTE YOURS HERE]'}
payload = {'grant_type':'authorization_code', 'code': authcode }
r = requests.post('https://account.docusign.com/oauth/token', data=payload, headers=headers)

#print(r.content)
accessCode = r.content

# Parse json to get access token
j = json.loads(accessCode)

# Prints Access Token on Terminal.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("  Copy and Paste token into Filemaker:\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print (j["access_token"])
