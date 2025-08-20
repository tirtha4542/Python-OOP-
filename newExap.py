class Bankaccount:

    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    def diposit(self,amount):
        if amount>0:
            self.__balance +=amount
            print(f"the Diposit amount is {amount}.newBalance = {self.__balance}")
        else:
            print("invalis amount")
    def withdraw(self,amount):
        if amount>0 and amount<self.__balance:
            self.__balance -= amount
            print(f"the Withdraw amount is {amount}.newBalance = {self.__balance}")
        else:
            print("invalis amount")

acc = Bankaccount(owner="Tirtha Bepary", balance=10000)

acc.withdraw(1010)
