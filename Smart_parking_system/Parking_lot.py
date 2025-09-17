from Parking_spot import ParkingSpot

# class ParkingLot:
#     def __init__(self):
#         self.spots = []

#     def add_spot(self, spot):
#         self.spots.append(spot)

#     def show_spots(self):
#         for spot in self.spots:
#             print(spot.show_status())

#     def park_vehicle(self, vehicle):
#         for spot in self.spots:
#             if spot.assign_vehicle(vehicle):
#                 return
#         print("No suitable spot available!")
#     def unpark_vehicle(self, vehicle, hrs):
#         for spot in self.spots:
#             if spot.show_status().find(vehicle.get_license()) != -1:
#                 removed = spot.remove_vehicle()
#                 if removed:
#                     fee = removed.cal_parkfee(hrs)
#                     print(f"Unparked {vehicle.get_license()} from Spot {spot.spotid}. Fee: ₹{fee}")
#                     return fee
#         print("Vehicle not found in lot!")
#         return 0


class ParkingLot:
    def __init__(self):
        self.spots = []                 # list of ParkingSpot
        self.plate_to_spot = {}         # license_plate -> ParkingSpot

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            print(spot.show_status())

    def park_vehicle(self, vehicle) -> bool:
        plate = vehicle.get_license_plate()
        if plate in self.plate_to_spot:
            print(f"[INFO] {plate} already parked in spot {self.plate_to_spot[plate].spot_id}")
            return False

        for spot in self.spots:
            if spot.is_empty() and spot.is_vehicle_fit(vehicle):
                ok = spot.assign_vehicle(vehicle)
                if ok:
                    self.plate_to_spot[plate] = spot
                    print(f"[OK] Parked {plate} at spot {spot.spot_id}")
                    return True
        print(f"[FAIL] No suitable spot available for {plate}")
        return False

    def unpark_vehicle(self, vehicle=None, license_plate: str = None, hours: int = 1) -> int:
        """
        Returns integer fee. Always returns int (0 if not found or error).
        Accepts either vehicle object or license_plate string.
        """
        plate = None
        if vehicle is not None:
            plate = vehicle.get_license_plate()
        elif license_plate is not None:
            plate = license_plate
        else:
            print("[ERROR] unpark_vehicle requires vehicle or license_plate")
            return 0

        # exact lookup
        spot = self.plate_to_spot.get(plate)
        if not spot:
            print(f"[INFO] Vehicle {plate} not found in this lot.")
            return 0

        removed = spot.remove_vehicle()
        # remove mapping even if remove returned None (defensive)
        try:
            del self.plate_to_spot[plate]
        except KeyError:
            pass

        if removed is None:
            print(f"[ERROR] Spot {spot.spot_id} reported vehicle missing when unparking {plate}")
            return 0

        # compute fee (ensure int)
        try:
            fee = removed.calculate_parking_fee(int(hours))
            fee = int(fee)
        except Exception as e:
            print(f"[ERROR] Failed to compute fee for {plate}: {e}")
            return 0

        print(f"[OK] Unparked {plate} from spot {spot.spot_id}. Fee: ₹{fee}")
        return fee
