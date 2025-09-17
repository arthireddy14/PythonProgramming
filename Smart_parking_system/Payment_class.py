from abc import ABC,abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass


# class CashPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Paid ₹{amount} in Cash")


# class CardPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Paid ₹{amount} via Card")


# class UPIPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Paid ₹{amount} via UPI")


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: int):
        pass

class CashPayment(Payment):
    def process_payment(self, amount: int):
        print(f"Paid ₹{amount} in Cash")

class CardPayment(Payment):
    def process_payment(self, amount: int):
        print(f"Paid ₹{amount} via Card")

class UPIPayment(Payment):
    def process_payment(self, amount: int):
        print(f"Paid ₹{amount} via UPI")
