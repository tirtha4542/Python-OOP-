class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
cat = Animal("cat",34)
cat.set_name("Dog")
print(cat.get_name())
cat.set_age(18)
print(cat.get_age())
