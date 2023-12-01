import requests
from datetime import datetime 

pixela_endpoint="https://pixe.la/v1/users"

TOKEN="kjgr55tfdst99thh"
USER="mohaum"
GRAPH_ID="graph1"

user_params={

    "token":TOKEN,
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USER}/graphs"

graph_config={
    "id":"graph1",
    "name":"Running Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"

}

headers={

    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"
today=datetime.now()


print(today)
graph_post={

    "date":today.strftime("%Y%m%d"),
    "quantity":"3.3",
    
}


# response=requests.post(url=pixel_creation_endpoint,json=graph_post,headers=headers)
# print(response.text)

pixel_put_endpoint=f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data={

    "quantity":"7.5"
}
response=requests.put(url=pixel_put_endpoint,json=graph_post,headers=headers)
print(response.text)


