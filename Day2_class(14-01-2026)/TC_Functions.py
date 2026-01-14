def add(a,b):
    print(a+b)
add(10,20)

def sub(a,b):
    return a-b,a,b
print(sub(100,50))

def hello(greeting="Hello",name="abhi"):
    print(greeting,name)
hello()
hello("greeting","abhi")

def print_param(*params):
    print(params)
print_param(1,2,3)
print_param('abhi')

def print_param(**params):
    print(params)
print_param(x=1,y=2,z=3)


