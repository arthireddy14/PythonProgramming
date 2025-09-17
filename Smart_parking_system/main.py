# from Vehicle_class import Bike,Car,Suv,Truck
# from Parking_spot import ParkingSpot
# from Parking_lot import ParkingLot
# from Payment_class import CardPayment,CashPayment,UPIPayment
# if __name__ == "__main__":
    
#     lot = ParkingLot()
#     lot.add_spot(ParkingSpot(1, "S"))
#     lot.add_spot(ParkingSpot(2, "M"))
#     lot.add_spot(ParkingSpot(3, "L"))
#     lot.add_spot(ParkingSpot(4, "XL"))

   
#     v1 = Bike("BIKE123", "Alice")
#     v2 = Car("CAR456", "Bob", seats=5)
#     v3 = Suv("SUV789", "Charlie", wheels4=True)
#     v4 = Truck("TRUCK321", "David", maxload=5000)

#     vehicles = [v1, v2, v3, v4]

    
#     for v in vehicles:
#         v.display()

    
#     lot.park_vehicle(v1)
#     lot.park_vehicle(v2)
#     lot.park_vehicle(v3)
#     lot.park_vehicle(v4)

#     print("\n--- Parking Lot Status ---")
#     lot.show_spots()

#     # Unpark and Pay
#     print("\n--- Unparking Process ---")
#     fee = lot.unpark_vehicle(v2, hrs=3)  # Car parked for 3 hours

#     # Payment
#     if fee > 0:
#         payment_method = UPIPayment()
#         payment_method.process_payment(fee)
# main.py
from Vehicle_class import Bike, Car, SUV, Truck
from Parking_spot import ParkingSpot
from Parking_lot import ParkingLot
from Payment_class import CardPayment,CashPayment,UPIPayment

if __name__ == "__main__":
    lot = ParkingLot()
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "L"))
    lot.add_spot(ParkingSpot(4, "XL"))

    v1 = Bike("BIKE123", "Alice")
    v2 = Car("CAR456", "Bob", seats=5)
    v3 = SUV("SUV789", "Charlie")
    v4 = Truck("TRUCK321", "David", max_load_capacity=5000)

    for v in (v1, v2, v3, v4):
        v.display()

    lot.park_vehicle(v1)
    lot.park_vehicle(v2)
    lot.park_vehicle(v3)
    lot.park_vehicle(v4)

    print("\n--- SPOT STATUS ---")
    lot.show_spots()

    # Unpark v2 (Car) after 3 hours
    fee = lot.unpark_vehicle(vehicle=v2, hours=3)
    print("Returned fee:", fee, type(fee))

    if fee and fee > 0:
        payment = UPIPayment()
        payment.process_payment(fee)
    else:
        print("No payment required or vehicle not found.")
