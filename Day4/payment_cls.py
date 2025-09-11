class Payment:
    def pay_amt(self,amt):
        print("This is Payment class ",amt)
        
class cashpay(Payment):
    def pay_amt(self,amt):
        print("Payment through cash ",amt)
        
class cardpay(Payment):
    def pay_amt(self,amt):
        print("This is card payment ",amt)

class upipay(Payment):
    def pay_amt(self,amt):
        print("This is upi payment ",amt)
        
payments = [Payment(),cashpay(), cardpay(), upipay()]
 
for p in payments:
    p.pay_amt(1000)
