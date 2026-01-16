from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass
    @abstractmethod
    def loan(self):
        pass
class Sbi(Bank):

    def interest(self):
        print("interest is 6%")

    def loan(self):
        print("loan is available")
s = Sbi()
s.interest()
s.loan()