class Animal():
    name = ""
    age = 0
    weight = 0

    def Display(self):
        print(self.name, self.age, self.weight)
class Cat(Animal):
    def mao(self):
        print("mao")
cat1 = Cat()
cat1.name="billi"
cat1.age = 20
cat1.weight = 80
cat1.Display()
cat1.mao()

