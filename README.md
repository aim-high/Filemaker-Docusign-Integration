# Aim High - Docusign-Filemaker Integration

**Disclaimer:** Still updating files for new feature requests.

**Previously:** Aim High has staff database and uses Docusign's web app to send HR paperwork to summer employees. During hiring season, HR department periodically uses Docusign's Retrieve to export envelope data. Then they use Excel's VLOOKUP to combine Docusign's data and staff data from our Filemaker database. This file is then used to compile HR forms to be sent to the IRS.

**Integration Goal:** Share resources between Filemaker and Docusign. Have ability to send Docusign envelopes to staff and get Docusign's envelope data and status into the Filemaker database. 

### Current Integration Solution
**eSignature API v2.1 ([Polling API](https://developers.docusign.com/esign-rest-api/code-examples/polling-for-envelope-status))**
* Authorization Code Grant

### Requirements
* Filemaker Pro Advanced 17
* [python3](https://www.python.org/downloads/)
* [selenium](https://pypi.org/project/selenium/), [requests](https://pypi.org/project/requests/) modules
* [Mozilla's geckodriver](https://github.com/mozilla/geckodriver)

### Assumptions:
You have a basic understanding of HTTP requests and familiarity with Docusign's REST API. You are somewhat comfortable using or learning Python, bash scripting, and Filemaker scripting. 
	
### Filemaker
* Create a dedicated set of fields for Docusign-related data. These fields may include envelope tab data (status, envelopeID, etc.).
* Created a layout where users initiate actions by clicking a button. I created 3 buttons: sending Docusign envelopes, getting tab data from envelopes, and getting an OAuth token.

### Authentication for Authorization Code Grant
Demo (sandbox endpoints) - ```https://demo.docusign.net/...```
Live (production endpoint) - ```https://{server}.docusign.net/...```
Examine getDocusignToken.sh and initiateOAuth.py. Fill in your credentials where indicated and run on the command line ```source getDocusignToken.sh```.

Enter your Docusign credentials in the opened Firefox browser. If successful, initiateOAuth.py will read the returned authcode and will use it to request both a refresh and access token.
initiateOAuth.py prints refresh and access tokens on terminal.

Tip: While you're using your demo sandbox environment, you can use [Docusign's OAuth Token Generator](https://developers.docusign.com/oauth-token-generator) to get the main components running.


Familiarize yourself with [cron](https://crontab.guru/) to get access token using valid refresh token.
To edit your crontab: on your command line for Mac OS X type 
```crontab -e```
If you need more help type ```man crontab```

It might look like this:
```
0    9    *    *    1-5     cd {absolute path for directory that houses refresh.py} && python3 refresh.py >> ~/cron.log 2>&1
0   16    *    *    1-5     echo "Access token has expired. Run refresh.py manually to update or wait till 9am M-F" > {absolute path to access_token.txt}
```
The first line tells cron to run refresh.py Monday thru Friday at 9am. Recall that refresh.py updates access_token.txt with a valid access token and timestamp when run.
The second line tells cron to overwrite access_token.txt with an expiration message. Tokens expire every 8 hours so cron runs this job at 5pm Monday thru Friday.

Docusign's refresh token expires every 30 days. Set a monthly reminder via cron to stay on top of things!
```
0	9	1	*	*	echo "Please get new refresh token." >> {absolute path to access_token.txt}
```

### Sending Docusign envelopes via Filemaker
[under construction]
[Learn more about REST API Templates](https://developers.docusign.com/esign-rest-api/guides/features/templates)
[Learn more about sending an envelope via your app](https://developers.docusign.com/esign-rest-api/code-examples/code-example-embedded-sending)
See sendEnvelopeFromTemplate.txt in Filemaker Scripts folder for my implementation.
```
# Create JSON object to populate Docusign tabs with Filemaker fields
Set Variable [$post_data ; Value: JSONSetElement ($$json ; 
["accountId" ; $accountID ; JSONString ];
["emailSubject" ; "Aim High Compliance Documents"; JSONString]; 
["templateId" ; $templateId ; JSONString];
["templateRoles[0]email"; $email ; JSONString];
["templateRoles[0]name"; $name ; JSONString];
["templateRoles[0]roleName"; "Staff" ; JSONString];
["templateRoles[0]tabs.textTabs[0]tabLabel"; "status_I9" ; JSONString];
["templateRoles[0]tabs.textTabs[0]value"; $status_I9 ; JSONString];
["templateRoles[0]tabs.textTabs[1]tabLabel"; "status_LiveScan" ; JSONString];
["templateRoles[0]tabs.textTabs[1]value"; $status_LiveScan ; JSONString];
...
["status"; "sent" ; JSONString])
```
HTTP POST request
```
Set Variable [$url ; Value: {YOUR_DOCUSIGN_ENDPOINT}/v2.1/accounts/{ACCOUNTID}/envelopes ]
Insert from URL [ Select ; With dialog: Off ; DocusignResult; $url; cURL options: "-X POST -H \"Authorization: Bearer " & $token & "\" -H \"Content-Type: application/json\"" & "-d @$post_data" ]
```

Don't forget to save your envelopeID and status!
```
# Set envelopeID and envelopeStatus fields
Set Field [ DocusignEnvelopeID ; JSONGetElement (DocusignResult ; "envelopeId")]
Set Field [ DocusignEnvelopeStatus ; JSONGetElement (DocusignResult ; "status")]
```

### Polling Docusign tabs into Filemaker fields
Implemented in Filemaker\ Scripts > getFormData.txt using Docusign eSignature REST API [EnvelopeFormData: GET](https://developers.docusign.com/esign-rest-api/reference/Envelopes/EnvelopeFormData/get).
My HTTP GET request in Filemaker looks like this:
```
Set Variable [ $get_data ; Value: DocusignResult]
Set Variable [ $url ; Value: "https://demo.docusign.net/restapi/v2.1/accounts/[ACCOUNT_ID]/envelopes/[ENVELOPE_ID]/form_data"]
Insert from URL [ Select ; With dialog: Off ; DocusignResult ; $url ; cURL options: "-X GET -H \"Authorization: Bearer [TOKEN] -H \"Content-Type: application/json\"" & "-d @$get_data"]
```

Since templates are separated out by staff's PositionType, create JSON object using Filemaker's built in JSONSetElement.
[Filemaker's JSONSetElement](https://fmhelp.filemaker.com/help/17/fmp/en/index.html#page/FMP_Help%2Fjsonsetelement.html%23)
```
JSONSetElement ( json ; keyOrIndexOrPath ; value ; type )
```
Sample JSONSetElement filled with Docusign's formData:
```
JSONSetElement ( $$JSON ; 
[ JSONGetElement ( DocusignResult ; "formData[0]name") ; JSONGetElement ( DocusignResult ; "formData[0]value" ) ; 1 ];
[ JSONGetElement ( DocusignResult ; "formData[1]name") ; JSONGetElement ( DocusignResult ; "formData[1]value" ) ; 1 ];
[ JSONGetElement ( DocusignResult ; "formData[2]name") ; JSONGetElement ( DocusignResult ; "formData[2]value" ) ; 1 ];
[ JSONGetElement ( DocusignResult ; "formData[3]name") ; JSONGetElement ( DocusignResult ; "formData[3]value" ) ; 1 ]
)
```
The above code shows the first 4 name-value pairs being grouped into a JSON object.
With the created JSON object, you can parse the returned JSON with the Docusign tab's name (as opposed to its position).
```
Set Field [ DocusignSN ; JSONGetElement (DocusignResult ; "SSN")]
```
The above example would set your DocusignSN Filemaker field to the value of Docusign's SSN tab.

###### Template changes
If there's any addition/subtraction of tabs in your template envelope, you **must** adjust the JSONSetElement statement to create your JSON Object accordingly.
* Troubleshooting: Every tab name label must not be empty! Otherwise your JSON object will not be created.


#### Resources
[Docusign REST API Documentation](https://developers.docusign.com/esign-rest-api)

[Filemaker Pro 17 Advanced Documentation](https://fmhelp.filemaker.com/help/17/fmp/en/#page/FMP_Help%2Findex.html)

[Stackoverflow](https://stackoverflow.com/questions/tagged/docusignapi)

[REST API: SDKs](https://developers.docusign.com/esign-rest-api/sdk-tools)

[OAuth Token Generator for Sandbox](https://developers.docusign.com/oauth-token-generator)

#### Other ways to Implement 
[Download BaseElements Plugin Filemaker 17](https://baseelementsplugin.zendesk.com/hc/en-us/articles/115002990887-BaseElements-Plugin) and [use this forum to install](https://community.filemaker.com/thread/186607)

[BaseElements Plugin Set up Video](https://community.filemaker.com/external-link.jspa?url=https%3A%2F%2Fwww.filemakermagazine.com%2Fvideos%2Ffilemaker-rest-using-baseelements-plugin)

Sample command to get going (replace with your Docusign Developer credentials)

curl -i -H "Accept: application/json" -H 'X-DocuSign-Authentication:{"Username": "{youremail@mail.com}","Password": "{yourpassword}", "IntegratorKey": "{IntegratorKey}"}' -X GET https://demo.docusign.net/restapi/v2/accounts/{ACCOUNTID}

Create custom functions in Filemaker Pro Advanced:
File > Manage > Custom Functions

endPointTest () = "https://demo.docusign.net/restapi/v2/accounts/{AccountID}"
DocusignKeyTest() = "{\"Username\": \"{youremail@mail.com}\",\"Password\": \"{yourpassword}\", \"IntegratorKey\": \"{integratorkey}\"}"
listStatus() = "https://demo.docusign.net/restapi/v2/accounts/{AccountID}/envelopes/status"