# -*- coding:utf-8 -*-

# Pi will send its IP address to predix

import websocket, requests, time
#
# """
# init
# UAA ID : root
# UAA secret:CTC1349sso~
# UAA token: "eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiJiZmEzZDk2MWZmNTA0ODg1ODhlMzVkZmU0ZGM2NTZjYyIsInN1YiI6ImFkbWluIiwic2NvcGUiOlsidWFhLmFkbWluIiwiem9uZXMuY2FjZjliNjQtMmRkYS00MDAyLWFjMjAtMDQ2NGRjY2Y2NjU2LmFkbWluIl0sImNsaWVudF9pZCI6ImFkbWluIiwiY2lkIjoiYWRtaW4iLCJhenAiOiJhZG1pbiIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiY2ZkODVkNjAiLCJpYXQiOjE0OTc1MzkxNTgsImV4cCI6MTQ5NzU4MjM1OCwiaXNzIjoiaHR0cHM6Ly9jYWNmOWI2NC0yZGRhLTQwMDItYWMyMC0wNDY0ZGNjZjY2NTYucHJlZGl4LXVhYS5ydW4uYXdzLXVzdzAyLXByLmljZS5wcmVkaXguaW8vb2F1dGgvdG9rZW4iLCJ6aWQiOiJjYWNmOWI2NC0yZGRhLTQwMDItYWMyMC0wNDY0ZGNjZjY2NTYiLCJhdWQiOlsiem9uZXMuY2FjZjliNjQtMmRkYS00MDAyLWFjMjAtMDQ2NGRjY2Y2NjU2IiwidWFhIiwiYWRtaW4iXX0.CZM1r2Czwl-54VsOrv_E7MQ0B3Nxlt7aX4F4pMkGUcsy8LqRJWXT1HJacgfZKbzVoXvYhhMZTk05GvJsh-0NmJQ10ygP2DWBZaGmy5qIw9rUNTYyu-T0SXKdzOY2kodsv7Z6xctmYfrxeuq8rSi66kC9hFqJsuFesN57RrkTkTQIztEO8V1jzdFSB8BRSg0hvy5s66iVh9bW7VbEkSFiQ04KYQVUYf1ec6mXHMoraWUsEBpNqymi6aS2klKW5NEb0yPb7PmpTsYUK082TRRv0YetPJ-WvXM56IJPZDuPWEjvOOQ87_vY0eRKlmdkoTlHMd7oKHFzALnOvDHbHFiX3g"
# UUA_for_hello ID:cacf9b64-2dda-4002-ac20-0464dccf6656
# TimeSeries_for_hello ID：0abc2787-7870-4fea-b452-878ba6dd188e
# Websocket for timeseries mircoservies:
# url ='wss://gateway-predix-data-services.run.aws-usw02-pr.ice.predix.io/v1/stream/messages'
# """

# 使用socket向UAA服务器发送requests，得到token
uaaRequestData ={'grant_type':'client_credentials','client_id':'root','client_secret':'CTC1349sso~','response_type':'token'}
uaaurl ='https://cacf9b64-2dda-4002-ac20-0464dccf6656.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'
response = requests.post(uaaurl, data=uaaRequestData)

access_token =response.json()['access_token']
print(access_token)

# 获取系统的时间，作为传感器数据的时间戳
messageID = int(time.time() * 1000)

# 生成消息内容-tags
tags = """{

 "messageId": """ + str(messageID) +""",

 "body": [

    {

     "name": "Pi's IP address",

     "datapoints": [

       [

         """ + str(messageID) + """,

         99.99,

         3

       ]

     ]

    }

  ]

}"""

print(tags)


# 生成消息内容-header，里面包括了

url ='wss://gateway-predix-data-services.run.aws-usw02-pr.ice.predix.io/v1/stream/messages'
headers = {"Authorization":"Bearer " + access_token, "predix-zone-id": "0abc2787-7870-4fea-b452-878ba6dd188e","Origin": "http://localhost"}
# print(headers)

# 用WebSocket发送headers
ws = websocket.WebSocket()
ws.connect(url, header=headers)
print("Sending data")

# 用WebSocket发送tags
ws.send(tags)
print("Sent")

# 获取receiving
print("Receiving...")

result = ws.recv()

print("Received '%s'" % result)

ws.close()
