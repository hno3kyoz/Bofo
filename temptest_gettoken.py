#

import time

messageID = long(time.time() * 1000)
print(messageID)



# import requests
#
# data = {'grant_type':'client_credentials','client_id':'root','client_secret':'CTC1349sso~','response_type':'token'}
#
# uaa = 'https://cacf9b64-2dda-4002-ac20-0464dccf6656.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'
#
# response = requests.post(uaa, data=data)
#
# access_token = response.json()['access_token']
#
# print(access_token)