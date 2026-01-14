class mydescriptor:
    def __get__(self,instance,owner):
        print("getting value")
        return instance._x

    def __set__(self,obj,value):
        print("setting value")
        obj._x = value

class Test:
    x = mydescriptor()
t = Test()
t.x = 10
print(t.x)