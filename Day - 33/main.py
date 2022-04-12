#  json.load -> load the json data from the file
#  json.dump -> write the json data into the file
#  json.loads -> convert the valid json string to python dict
#  json.dumps -> dict to json


'''
Http Status Codes

1. 1XX -> Something is happening
2. 2xx -> Successful
3. 3xx -> Permission denied
4. 4xx -> You screwed up
5. 5xx -> Server side screwed up

'''

import requests
import json


# data = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if data.status_code == 200:
# #     print(data.status_code)
# # else:
# #     print("Something else: ",data.status_code)
# data.raise_for_status()
# data = json.loads(data.text)
# print(data["iss_position"]["latitude"])



# OR

data = requests.get("http://api.open-notify.org/iss-now.json")
data = data.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
position = (latitude,longitude)
print(position)