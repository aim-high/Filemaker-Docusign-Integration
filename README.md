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
	* eSignature API v2.1
	  * Authorization Code Grant
	
## Filemaker
-Create a dedicated set of fields for Docusign-related data. These fields may nclude envelope tab data (status, envelopeID, etc.).
-Created a layout where users initiate actions by clicking a button. I created 3 buttons: sending Docusign envelopes, getting tab data from envelopes, and getting an OAuth token.


# Authentication
```


```



## Resources: 
[Docusign REST API Documentation](https://developers.docusign.com/esign-rest-api)
Download BaseElements Plugin Filemaker 17 from [here](https://baseelementsplugin.zendesk.com/hc/en-us/articles/115002990887-BaseElements-Plugin and use this forum to install: https://community.filemaker.com/thread/186607)

[Video](https://community.filemaker.com/external-link.jspa?url=https%3A%2F%2Fwww.filemakermagazine.com%2Fvideos%2Ffilemaker-rest-using-baseelements-plugin) set up

