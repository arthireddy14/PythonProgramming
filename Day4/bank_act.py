class Bankacct:
    def __init__(self,bal=0):
        self.__bal=bal
    def deposit(self,amt):
        self.__bal=self.__bal+amt
        print("Amt ",amt," deposited successfully ")
    def withdraw(self,amt):
        if(self.__bal>amt):
            self.__bal=self.__bal-amt
            print("Amt ",amt," withdrawn successfully")
        else:
            print("Insufficient balance")
    def get_balanace(self):
        print("Current balance is ",self.__bal)
# class Bank1(Bankacct):
#     def get_balanace(self):
#         print("Cur balance is ",self.__bal)
    
        
b1=Bankacct(500)
b1.deposit(5000)
b1.withdraw(7000)
b1.get_balanace()
# b2=Bank1()
# b2.get_balanace()        
        