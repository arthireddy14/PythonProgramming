from Vehicle_class import Bike,Car,SUV,Truck
# class ParkingSpot:
#     def __init__(self,spotid,size):
#         self.spotid=spotid
#         # self.__isoccupied=False
#         self.__size=size
#         self.__vehicle=None
#         # self.__startime=None
    
#     def get_size(self):
#         return self.__size
#     def set_size(self,size):
#         self.__size=size
#     def isoccpied(self):
#         return self.__isoccupied
        
        
#     def assign_vehicle(self,vehicle):
#         # if not self.__isoccupied:
#         #     self.__startime=time.time()
#         #     hrs=max(1,)
#         if self.__vehicle is not None:
#             print(f"Spot {self.spotid} already occupied!")
#             return False

#         if self.is_vehicle_fit(vehicle):
#             self.__vehicle = vehicle
#             vehicle.park()
#             print(f"Vehicle {vehicle.get_license()} parked at Spot {self.spotid}")
#             return True
#         else:
#             print(f"Vehicle {vehicle.get_license()} does not fit in Spot {self.spotid}")
#             return False
        
#     def remove_vehicle(self):
#         # if self.__is_occupied:
#         #     end_time = time.time()
#         #     hrs = max(1, int((end_time - self.__start_time) // 3600) + 1)  # at least 1 hour
#         #     fee = self.__vehicle.calculate_parking_fee(hrs)
#         #     v = self.__vehicle
#         #     print(f"Vehicle {v.get_license_plate()} unparked from Spot {self.__spot_id} after {hours} hours. Fee = ₹{fee}")
#         #     self.__vehicle = None
#         #     self.__is_occupied = False
#         #     self.__start_time = None
#         #     return fee
#         # else:
#         #     print("Spot is empty.")
#         #     return 0
#         if self.__vehicle is None:
#             print(f"Spot {self.spotid} is already empty!")
#             return None
#         vehicle = self.__vehicle
#         self.__vehicle = None
#         return vehicle

#     def is_vehicle_fit(self, vehicle):
#         size_map = {
#             "S": [Bike],
#             "M": [Bike, Car],
#             "L": [Bike, Car, Suv],
#             "XL":[Bike, Car, Suv, Truck]
#         }
#         return type(vehicle) in size_map[self.__size]
#     def show_status(self):
#         if self.__vehicle:
#             return f"Spot {self.spotid} [{self.__size}] - Occupied by {self.__vehicle.get_license()}"
#         else:
#             return f"Spot {self.spotid} [{self.__size}] - Empty"
    


class ParkingSpot:
    def __init__(self, spot_id: int, size: str):
        self.spot_id = spot_id
        self.__size = size.upper()   # 'S', 'M', 'L', 'XL'
        self.__vehicle = None

    def is_empty(self) -> bool:
        return self.__vehicle is None

    def get_vehicle(self):
        return self.__vehicle

    def assign_vehicle(self, vehicle) -> bool:
        if not self.is_empty():
            # already occupied
            return False
        if not self.is_vehicle_fit(vehicle):
            return False
        # assign
        self.__vehicle = vehicle
        vehicle.park()
        return True

    def remove_vehicle(self):
        if self.__vehicle is None:
            return None
        v = self.__vehicle
        self.__vehicle = None
        return v

    def is_vehicle_fit(self, vehicle) -> bool:
        # allowed types per size
        size_map = {
            "S": (Bike,),
            "M": (Bike, Car),
            "L": (Bike, Car, SUV),
            "XL": (Bike, Car, SUV, Truck)
        }
        allowed = size_map.get(self.__size, ())
        return isinstance(vehicle, allowed)

    def show_status(self) -> str:
        if self.__vehicle:
            return f"Spot {self.spot_id} [{self.__size}] - Occupied ({self.__vehicle.get_license_plate()})"
        else:
            return f"Spot {self.spot_id} [{self.__size}] - Empty"
