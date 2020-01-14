# Purpose: Uses refresh token to request access token and stores new token in access_token.txt
# Dependencies: Must have valid refresh token to request new access token.
# Created: 10-25-2019 by Erica Ching (eching@aimhigh.org)
# Modified: 01-14-2020 by Erica

#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests
import json
import datetime

refreshToken = "{REFRESH_TOKEN}"

# GET HTTP request using refresh token
headers = {'Authorization': 'Basic {BASE64_COMBINATION_OF_INTEGRATION_AND_SECRET_KEYS}'}
payload = {'grant_type':'refresh_token', 'refresh_token': refreshToken }
refreshr = requests.post('https://account.docusign.com/oauth/token', data=payload, headers=headers)

r = json.loads(r.content)
now = datetime.datetime.now()

# write access token and timestamp to access_token.txt
writefile = open("access_token.txt", "w")
writefile.write(r["access_token"])
writefile.close()

with open("access_token.txt", mode="a") as file:
    file.write("\n\nScript run at %s.\n" % datetime.datetime.now())


# write access token and timestamp to refresh_token.txt
writefile = open("refresh_token.txt", "w")
writefile.write(r["refresh_token"])
writefile.close()

with open("refresh_token.txt", mode="a") as file:
    file.write("\n\nScript run at %s.\n" % datetime.datetime.now())


# Under construction: will refresh access token every 8 hours
#expires = r["expires_in"]
#now = datetime.datetime.now()
#add_sec = now + datetime.timedelta(seconds=expires)

#print('Current local date and time: ', now)
#print('Will run again at: ', add_sec)
