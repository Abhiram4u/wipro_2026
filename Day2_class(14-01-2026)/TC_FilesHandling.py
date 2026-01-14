file = open("file.txt","r")
content = file.readline()
content1 = file.readlines()

print(content)
print(content1)
file.close()

file = open("file.txt","w")
file.write("\n Hello World this is new line")
file.close()

file = open("file.txt","a")
file.write("\n Hello World this is new line append mode")
file.close()
