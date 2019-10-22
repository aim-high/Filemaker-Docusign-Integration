POST https://account-d.docusign.com/oauth/token
Authorization: Basic BASE64_COMBINATION_OF_INTEGRATION_AND_SECRET_KEYS

grant_type=refresh_token&refresh_token=YOUR_REFRESH_TOKEN

curl --header "Authorization: Basic MjMwNTQ2.....Y4MmM3YmYyNzZlOQ==" --data "grant_type=refresh_token&refresh_token=ey4fd.....3d31d` --request POST https://account-d.docusign.com/oauth/token
r = requests.post('https://account.docusign.com/oauth/token', data=payload, headers=headers)
