# Aim High - Docusign-Filemaker Integration

**Disclaimer:** Still updating files for new feature requests.

**Previously:** Aim High has staff database and uses Docusign's web app to send HR paperwork to summer employees. During hiring season, HR department periodically uses Docusign's Retrieve to export envelope data. Then they use Excel's VLOOKUP to combine Docusign's data and staff data from our Filemaker database. This file is then used to compile HR forms to be sent to the IRS.

**Integration Goal:** Share resources between Filemaker and Docusign. Have ability to send Docusign envelopes to staff and get Docusign's envelope data and status into the Filemaker database. 

## Requirements
	* Filemaker Pro Advanced 17
	  * BaseElements Plugin for Filemaker 17
	* python3
	* selenium, requests modules
	* geckodriver exec

## Assumptions:
Whoever is following this has a basic understanding of HTTP requests and familiarity with Docusign's REST API (or able to understand documentation). You are somewhat comfortable using Python, bash scripting, and Filemaker scripting, 

## Current Integration Solution:
	* eSignature API v2.1 (Polling API)
	  * Authorization Code Grant
	
## Filemaker
* Create a dedicated set of fields for Docusign-related data. These fields may include envelope tab data (status, envelopeID, etc.).
* Created a layout where users initiate actions by clicking a button. I created 3 buttons: sending Docusign envelopes, getting tab data from envelopes, and getting an OAuth token.


# Authentication
Authorization Code Grant
Examine getDocusignToken.sh and initiateOAuth.py. Fill in your credentials where indicated and run on the command line ```source getDocusignToken.sh```.

Enter your Docusign credentials in the opened Firefox browser. If successful, initiateOAuth.py will read the returned authcode and will use it to request both a refresh and access token.
initiateOAuth.py prints refresh and access tokens on terminal.


Familiarize yourself with [cron](https://crontab.guru/) to get access token using valid refresh token.
To edit your crontab: on your command line for Mac OS X type 
```crontab -e```
If you need more help type ```man crontab```

It might look like this:
```
0    9    *    *    1-5     cd [absolute path for directory that houses refresh.py] && python3 refresh.py >> ~/cron.log 2>&1
0   16    *    *    1-5     echo "Access token has expired. Run refresh.py manually to update or wait till 9am M-F" > /Users/erica/Desktop/access_token.txt
```
The first line tells cron to run refresh.py Monday thru Friday at 9am. Recall that refresh.py updates access_token.txt with a valid access token and timestamp when run.
The second line tells cron to overwrite access_token.txt with an expiration message. Tokens expire every 8 hours so cron runs this job at 5pm Monday thru Friday.

Docusign's refresh token expires every 30 days. Set a monthly reminder via cron to stay on top of things!
```
0	9	1	*	*	echo "Please get new refresh token." >> /Users/erica/Desktop/access_token.txt
```

## Resources
[Docusign REST API Documentation](https://developers.docusign.com/esign-rest-api)

## Other ways to Implement 
[Download BaseElements Plugin Filemaker 17](https://baseelementsplugin.zendesk.com/hc/en-us/articles/115002990887-BaseElements-Plugin) and [use this forum to install](https://community.filemaker.com/thread/186607)

[BaseElements Plugin Set up Video](https://community.filemaker.com/external-link.jspa?url=https%3A%2F%2Fwww.filemakermagazine.com%2Fvideos%2Ffilemaker-rest-using-baseelements-plugin)

