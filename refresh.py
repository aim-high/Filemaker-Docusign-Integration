# Purpose: Uses refresh token to request access token and stores new token in 
# access_token.txt
# Dependencies: Must have valid refresh token to request new access token.
# Created: 10-25-2019 by Erica Ching (eching@aimhigh.org)
# Modified: 02-03-2020 by Erica

#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests
import json
import datetime

def dayOfMonth(num):
	# must convert to int otherwise < 10 will look like '0#'
	day = int(datetime.datetime.now().strftime("%d"))
	if (day == num):
		return True
	else:
		return False

firstDay = dayOfMonth(1) # First day of month
if (firstDay):
	with open("refresh_token.txt") as f:
		first_line = f.readline().strip()
	refreshToken = first_line
	print("Renewing refresh token for new month")
else:
	refreshToken = "{REFRESH_TOKEN}"
	print("Using this month's refresh token.")


# GET HTTP request using refresh token
headers = {'Authorization': 'Basic {BASE64_COMBINATION_OF_INTEGRATION_AND_SECRET_KEYS}'}
payload = {'grant_type':'refresh_token', 'refresh_token': refreshToken }
refreshr = requests.post('https://account.docusign.com/oauth/token', data=payload, \
headers=headers)

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
