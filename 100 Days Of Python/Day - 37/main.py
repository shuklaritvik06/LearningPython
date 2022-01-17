import requests
import datetime as dt
import os

# URL= "https://pixe.la/v1/users"
# data={
#     "token":os.environ.get("TOKEN"),
#     "username":os.environ.get("USERNAME"),
#     "agreeTermsOfService":"yes", 
#     "notMinor":"yes"
# }
# mres= requests.post(url=URL,json=data)
# print(mres.text)




# NEW_URL = f"https://pixe.la/v1/users/{os.environ.get('USERNAME')}/graphs"
# headers={
#     "X-USER-TOKEN":os.environ.get("TOKEN")
#     }
# graph_config={
#     "id":"test-graph",
#     "name":"Python Projects",
#     "unit":"commit",
#     "type":"int",
#     "color":"ajisai",
#     "isSecret":True,
#     "publishOptionalData":True
# }
# response = requests.post(url=NEW_URL,json=graph_config,headers=headers)
# response.raise_for_status()
# print(response.text)



# URL= f"https://pixe.la/v1/users/{os.environ.get('USERNAME')}/graphs/test-graph"
# date = dt.datetime.today().strftime("%Y%m%d")
# pixel_update = {
#     "date": date,
#     "quantity": "16"
# }
# headers={
#     "X-USER-TOKEN":os.environ.get("TOKEN")
# }
# response = requests.post(URL,json=pixel_update,headers=headers)
# print(response.text)


# date = dt.datetime.today().strftime("%Y%m%d")
# URL=f"https://pixe.la/v1/users/{os.environ.get('USERNAME')}/graphs/test-graph/{date}"
# pixel_putreq = {
#     "date": date,
#     "quantity": "18"
# }
# headers={
#     "X-USER-TOKEN":os.environ.get("TOKEN")
# }
# response = requests.put(URL,json=pixel_putreq,headers=headers)
# print(response.text)


date = dt.datetime.today().strftime("%Y%m%d")
URL=f"https://pixe.la/v1/users/{os.environ.get('USERNAME')}/graphs/test-graph/{date}"
headers={
    "X-USER-TOKEN":os.environ.get("TOKEN")
}
response = requests.delete(URL,headers=headers)
print(response.text)