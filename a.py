from abc import ABC,abstractmethod
class absclass(ABC):
    def print(self,name):
        print("Name:"+name)
    @abstractmethod
    def abb(self):
        print("inside absc class")
class test(absclass):
    def abb(self):
        print("hidden")

a=test()
a.abb()
a.print("kushal")
