class Calculator:
    def calculate(self,a,b):
        print("calculator: adding two numbers")
        return a+b
class AdvancedCalculator(Calculator):
    def calculate(self,a,b):
        print("Advanced calculator: multiply two numbers")
        return a*b
class Number:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return Number(self.value + other.value)
    def display(self):
        print("valus: ",self.value)

if __name__ == "__main__":
    print("__method overriding__")
    calc = Calculator()
    adv_calc = AdvancedCalculator()

    print(calc.calculate(10,20))
    print(adv_calc.calculate(10,20))

    print("\n---operator overloading---")
    n1 = Number(10)
    n2 = Number(20)

    n3 = n1 + n2
    n3.display()