class Car:
    def __init__(self,make,model,year):
        self.make  = make
        self.model = model
        self.year = year
    def Display(self):
        print(self.model,self.year,self.make)
car1 = Car("bmw","c12",1999)
car1.Display()




