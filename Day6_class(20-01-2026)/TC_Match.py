import re
text = "pythonispowerful"

result = re.match("python", text)

if result:
    print("match found")
else:
    print("no match found")


searchresult = re.search("powerful", text)
print(searchresult.group())
print(searchresult.start())
print(searchresult.end())

email = "admin@gmail.com"
if re.search(r"[a-zA-Z]+@",email):
    print("valid start")

mobile = "84988098"
resu = re.search(r"^[0-9].+",mobile)
print(resu)

print(re.fullmatch(r"\d{10}","1234567890"))

print(re.findall(r"\d+","price 50 and 100"))

for n in re.finditer(r"\d+","A1,B333,C444"):
    print(n.group(),n.start(),n.end())

print(re.search(r"\d+","Age is 25"))
print(re.search(r"^a.*c$","akbnnc"))

m = re.search(r"\w+(?=@)","test@gmail.com")
print(m.group())

print(re.search("python","Python",re.I))

text4 = "one\ntwo\nthree"
print(re.findall(r"^t\w+",text4,re.M))
