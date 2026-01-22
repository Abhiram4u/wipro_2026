import requests

url = "https://api.restful-api.dev/objects"

response = requests.get(url)
print("__________GET1____________")
print(response.status_code)
print(response.json())


url1 = "https://api.restful-api.dev/objects?id=3&id=5&id=10"
r1 = requests.get(url1)
print("__________GET2____________")
print(r1.status_code)
print(r1.json())


url2 = "https://api.restful-api.dev/objects/7"
r2 = requests.get(url2)
print("__________GET3____________")
print(r2.status_code)
print(r2.json())


posturl = "https://api.restful-api.dev/objects"

body1 = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

r4 = requests.post(url, json=body1)
print("__________POST____________")
print(r4.status_code)
print(r4.json())

puturl = "https://api.restful-api.dev/objects/ff8081819782e69e019be4043c212e73"
body2 = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
r5 = requests.put(puturl,json=body2)
print("__________PUT____________")
print(r5.status_code)
print(r5.json())

patchurl = "https://api.restful-api.dev/objects/ff8081819782e69e019be4043c212e73"
body3 = {
   "name": "Apple MacBook Pro 16 (Updated Name)"
}
r6 = requests.patch(patchurl,json=body3)
print("__________PATCH_____________")
print(r6.status_code)
print(r6.json())

deleteurl = "https://api.restful-api.dev/objects/ff8081819782e69e019be4060ed32e85"

r7 = requests.delete(deleteurl)

print("__________DELETE____________")
print(r7.status_code)
print(r7.json())




