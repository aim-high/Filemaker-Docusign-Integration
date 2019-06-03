# AUTHORIZATION CODE GRANT 
# 
# Get Authorization Code First - input the following in a browser
# https://account.docusign.com/oauth/auth?response_type=code&scope=signature%20extended&client_id=[INTEGRATOR KEY]]&state=YOUR_CUSTOM_STATE&redirect_uri=https://127.0.0.1:3000
#
# Sample Response: 
# http://example.com/callback/?code=eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQkAAAABAAYABwAAhbSd_bXVSAgAABE75f211UgCAIh5T0YjCJpArIp4HuVWq3oVAAEAAAAYAAEAAAAFAAAADQAkAAAANWMyYjhkN2UtODNjMy00OTQwLWFmNWUtY2RhOGE1MGRkNzNmMAAAhbSd_bXVSBIAAQAAAAsAAABpbnRlcmFjdGl2ZQ.4bVZOQFSAy0rcDs-0-c0zyLVB4n9wi9fb9UJTmrQZE0JgMKDddOMnb9n-wmHSZqrcl-RVlyXNnLNFd41GIePp6wBiMZ9EOgCIzGFnw3KduIJTPb9LdN__ATM5y0y5Iy2ruWLd56IgVgMX58n5hsvOcTJTIIteI7MIGY-1q3Bjf8Q9stdz5Ag8dT9o1RUlmoZX-XMWOYA0UoEEiI4sILa-DZtTyZH3O5Gm-Cy23aqmIttUFLB8mylbUnGjZxS5EJXV7KUptT9vZNUqayVRo05dkuprSKM1v3li27SPw8fKHrdsa9WKvhWFAw8ojoTu6qeqxJ9v6D81QFsje43QVZ_gw&state=a39fh23hnf23

import requests

headers = {'Authorization': 'Basic BASE64_COMBINATION_OF_INTEGRATOR_AND_SECRET_KEYS'}
payload = {'grant_type':'authorization_code', 'code': 'YOUR_AUTH_CODE_SEE_ABOVE_SAMPLE'}'
r = requests.post('https://account.docusign.com/oauth/token', data=payload, headers=headers)

print(r.content)