from abc import ABC,abstractmethod

class DemoInterface(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def display2(self):
        pass

class cow(DemoInterface):
    def __init__(self,age,weight):
        self.age = age
        self.weight = weight
    def display(self):
        print("Thi is my oldage Display method")

        print(self.age,self.weight)

    def display2(self):
        print("this is Display2")
cow1 = cow(23,1000)
cow1.display()