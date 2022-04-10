class Base1():
    def __init__(self):
        self.str1="First"
        print("BAse1")
class Base2():
    def __init__(self):
        self.str2="Secound"
        print("Base2")

class Child(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

    def Dispaly(self):
        print(self.str1,self.str2)


a=Child()
a.Dispaly()
