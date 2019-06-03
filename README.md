# Filemaker-Docusign-Integration

Filemaker and Docusign Integration

Previous State: Aim High has staff database and uses Docusign to send HR paperwork to summer employees. During hiring season, HR department uses Docusign Retrieve to export envelope tabs and exports peron's data from Filemaker. Using VLookup, they combine both exports to submit to IRS.

Goal: Share resources between Filemaker and Docusign. Namely, pull Docusign data into database such as envelope status. In the future, would like to stop using Docusign web application and instead do all things Docusign from Filemaker.


Sources: 
https://developers.docusign.com/esign-rest-api
https://community.filemaker.com/thread/97349

---- BELOW NEEDS EDITS ------
Sample command to get going (replace bolded text with your Docusign Developer credentials)

curl -i -H "Accept: application/json" -H 'X-DocuSign-Authentication:{"Username": "{youremail@mail.com}","Password": "{yourpassword}", "IntegratorKey": "{IntegratorKey}"}' -X GET https://demo.docusign.net/restapi/v2/accounts/{APIaccountID}

# FileMaker Pro Advanced
Download BaseElements Plugin Filemaker 17 from here: https://baseelementsplugin.zendesk.com/hc/en-us/articles/115002990887-BaseElements-Plugin and use this forum to install: https://community.filemaker.com/thread/186607

Video set up help:
https://community.filemaker.com/external-link.jspa?url=https%3A%2F%2Fwww.filemakermagazine.com%2Fvideos%2Ffilemaker-rest-using-baseelements-plugin

Create custom functions in Filemaker Pro Advanced:
File > Manage > Custom Functions

endPointTest () = "https://demo.docusign.net/restapi/v2/accounts/{AccountID}"
DocusignKeyTest() = "{\"Username\": \"{youremail@mail.com}\",\"Password\": \"{yourpassword}\", \"IntegratorKey\": \"{integratorkey}\"}"
listStatus() = "https://demo.docusign.net/restapi/v2/accounts/{AccountID}/envelopes/status"
