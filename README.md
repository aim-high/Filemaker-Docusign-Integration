# Filemaker-Docusign-Integration

Filemaker and Docusign Integration

Previously: Aim High has staff database and uses Docusign's web app to send HR paperwork to summer employees. During hiring season, HR department periodically uses Docusign's Retrieve to export envelope data. Then they use Excel's VLOOKUP to combine Docusign's data and staff data from our Filemaker database. This file is then used to compile HR forms to be sent to the IRS.

Integration Goal: Share resources between Filemaker and Docusign. Have ability to send Docusign envelopes to staff and get Docusign's envelope data and status into the Filemaker database. 

Resources: 
https://developers.docusign.com/esign-rest-api
https://community.filemaker.com/thread/97349

---- BELOW NEEDS EDITS ------

Sample command to get going (replace bolded text with your Docusign Developer credentials)

curl -i -H "Accept: application/json" -H 'X-DocuSign-Authentication:{"Username": "{youremail@mail.com}","Password": "{yourpassword}", "IntegratorKey": "{IntegratorKey}"}' -X GET https://demo.docusign.net/restapi/v2/accounts/{APIaccountID}

# FileMaker Pro 17 Advanced
Download BaseElements Plugin Filemaker 17 from here: https://baseelementsplugin.zendesk.com/hc/en-us/articles/115002990887-BaseElements-Plugin and use this forum to install: https://community.filemaker.com/thread/186607

Video set up help:
https://community.filemaker.com/external-link.jspa?url=https%3A%2F%2Fwww.filemakermagazine.com%2Fvideos%2Ffilemaker-rest-using-baseelements-plugin

Create custom functions in Filemaker Pro Advanced:
File > Manage > Custom Functions

endPointTest () = "https://demo.docusign.net/restapi/v2/accounts/{AccountID}"
DocusignKeyTest() = "{\"Username\": \"{youremail@mail.com}\",\"Password\": \"{yourpassword}\", \"IntegratorKey\": \"{integratorkey}\"}"
listStatus() = "https://demo.docusign.net/restapi/v2/accounts/{AccountID}/envelopes/status"
