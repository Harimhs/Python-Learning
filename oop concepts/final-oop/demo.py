from abc import ABC, abstractmethod

class Students(ABC):

    @abstractmethod
    def sub(self,num1,num2):
        pass
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def add(self, num, num1):
        return self.age + num + num1
    
    def add(self, num1):
        return self.age + num1

class subject(Students):

    
    def sub(self,num1,num2):
        return num1-num2

    @staticmethod
    def mul(num1,num2):
        return num1*num2
    
    def add(self,num1):
        return self.age-num1
    
s1=subject("naveen",21)
print(subject.mul(7,3))
print(s1.sub(12,32))
print(s1.add(12))

    