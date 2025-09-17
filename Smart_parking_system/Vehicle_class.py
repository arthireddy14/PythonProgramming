# import time
# class Vehicle:
#     def __init__(self,license,oname):
#         self.__license=license
#         self.__oname=oname
#         self.entry_time=None
#     def get_license(self):
#         return self.__license
#     def set_license(self,license):
#         self.__license=license
#     def get_oname(self):
#         return self.__oname
#     def set_oname(self,oname):
#         self.__oname=oname
#     def park(self):
#         self.entry_time=time.time()
#     def unpark(self):
#         if self.entry_time:
#             hrs=time.time()-self.entry_time/3600
#             return max(1,int(hrs))
#         return 0
        
#     def display(self):
#         print("Vehicle details License No.:{self.__license} Owner name : {self.__oname}")
#     def cal_parkfee(self,hours):
#         return 0
    
# class Bike(Vehicle):
#     def __init__(self, license, oname,helmetrq=True):
#         super().__init__(license,oname)
#         self.helmetrq=helmetrq
    
#     def display(self):
#         print("Bike license no. ",self.get_license())
#         print("Bike owner name ",self.get_oname())
#         print("Bike helmet ",self.helmetrq)
#     def cal_parkfee(self,hours):
#         print("Bill is ",20*hours)
        

# class Car(Vehicle):
#     def __init__(self, license, oname,seats):
#         super().__init__(license,oname)
#         self.seats=seats
        
#     def display(self):
#         print("Car license ",self.get_license())
#         print("Car owner name ",self.get_oname())
#         print("Seats in car ",self.seats)
#     def cal_parkfee(self,hours):
#         print("Bill is ",50*hours)
        
        

# class Suv(Vehicle):
#     def __init__(self, license, oname,wheels4):
#         super().__init__(license,oname)
#         self.wheels4=wheels4
#     def display(self):
#         print("Suv license ",self.get_license())
#         print("Suv owner name ",self.get_oname())
#         print("wheels in suv ",self.wheels4)
#     def cal_parkfee(self,hours):
#         print("Bill is ",70*hours)
        
        
# class Truck(Vehicle):
#     def __init__(self, license, oname,maxload):
#         super().__init__(license,oname)
#         self.maxload=maxload
#     def display(self):
#         print("Truck license ",self.get_license())
#         print("Truck owner name ",self.get_oname())
#         print("Max load in Truck ",self.maxload)
#     def cal_parkfee(self,hours):
#         print("Bill is ",100*hours)

# vehicle.py
import time

class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate
        self.__owner_name = owner_name
        self.entry_time = None

    # getters / setters
    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, name):
        self.__owner_name = name

    def park(self):
        self.entry_time = time.time()

    def unpark_time_hours(self):
        """Return integer hours parked (round up to at least 1)."""
        if not self.entry_time:
            return 0
        seconds = time.time() - self.entry_time
        hours = int(seconds // 3600)
        if seconds % 3600:
            hours += 1
        return max(1, hours)

    def display(self):
        print(f"Vehicle {self.__license_plate} (Owner: {self.__owner_name})")

    def calculate_parking_fee(self, hours: int) -> int:
        return 0


class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike | {self.get_license_plate()} | Owner: {self.get_owner_name()} | Helmet: {self.helmet_required}")

    def calculate_parking_fee(self, hours: int) -> int:
        return int(20 * hours)


class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"Car  | {self.get_license_plate()} | Owner: {self.get_owner_name()} | Seats: {self.seats}")

    def calculate_parking_fee(self, hours: int) -> int:
        return int(50 * hours)


class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV  | {self.get_license_plate()} | Owner: {self.get_owner_name()} | 4WD: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours: int) -> int:
        return int(70 * hours)


class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity=1000):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck| {self.get_license_plate()} | Owner: {self.get_owner_name()} | MaxLoad: {self.max_load_capacity}kg")

    def calculate_parking_fee(self, hours: int) -> int:
        return int(100 * hours)

        