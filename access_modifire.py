class NewSchool:
    def __init__(self,name,age,Gender):
        self.__name = name
        self._age = age
        self.__gender = Gender
    def Display(self):
        print(self._age,self.__gender,self.__name)
sc1 = NewSchool("Tirtha","45","Male")


sc1.Display()