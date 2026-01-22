import requests

geturl = "http://127.0.0.1:5000/users"
response1 = requests.get(geturl)
print("-----GET USERS------")
print(response1.status_code)
print(response1.json())


geturl_id = "http://127.0.0.1:5000/users/1"
reponse2 = requests.get(geturl_id)
print("-----GET USERS BY ID------")
print(reponse2.status_code)
print(reponse2.json())


posturl = "http://127.0.0.1:5000/users"

body1 = {
    "name":"varma"
}

response3 = requests.post(posturl, json=body1)
print("-----POST USER------")
print(response3.status_code)
print(response3.json())
print("-----AFTER POST USERS------")
print(response1.json())

puturl = "http://127.0.0.1:5000/users/3"
body2 = {
    "name":"spoorthi"
}
response4 = requests.put(puturl, json=body2)
print("-----PUT USER------")
print(response4.status_code)
print(response4.json())

patchurl = "http://127.0.0.1:5000/users/2"
body3 = {"name":"varma"}

response5 = requests.patch(patchurl, json=body3)
print("-----PATCH USER------")
print(response5.status_code)
print(response5.json())

deleteurl = "http://127.0.0.1:5000/users/1"
response6 = requests.delete(deleteurl)
print("-----DELETE USER------")
print(response6.status_code)
print(response6.json())
