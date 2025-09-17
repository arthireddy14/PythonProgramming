# Smart Parking System:
# • Create classes Vehicle, ParkingSpot, and ParkingLot.
# • Create multiple objects (vehicles, spots, parking lot).
# • Demonstrate object creation, attribute initialization, and method calls.
# • Make sensitive attributes private (e.g., license plate, owner name, spot status).
# • Provide getter/setter methods to access/update them safely.
# • Show that direct access fails but methods work.
# • Vehicle is the base class.
# • Derived classes:
# Bike (extra attribute: helmet_required)
# Car (extra attribute: seats)
# SUV (extra attribute: four_wheel_drive)
# Truck (extra attribute: max_load_capacity)
# • Each child class overrides display() to print its own details.
# • Create a list of different vehicle objects (Bike, Car, SUV, Truck).
# • Iterate and call display() → each object responds differently.
# • Implement a calculate_parking_fee() method:
# Bike → ₹20/hour
# Car → ₹50/hour
# SUV → ₹70/hour
# Truck → ₹100/hour
# • Demonstrate runtime polymorphism by calling the method on different objects.
# • Create an abstract class/interface Payment (using abc module).
# • Define an abstract method process_payment(amount).
# • Create child classes:
# CashPayment
# CardPayment
# UPIPayment
# • Demonstrate abstraction by processing payments differently (just print “Paid ₹X via UPI”).
# Task 1: Vehicle Classes
# Implement base and derived vehicle classes with encapsulation.
# Override display() and calculate_parking_fee().
# Task 2: ParkingSpot Class
# Implement ParkingSpot with size restrictions (S, M, L, XL).
# Methods: assign_vehicle(), remove_vehicle().
# Ensure vehicle type fits correct spot size (Bike → S+, Car → M+, SUV → L+, Truck → XL only).
# Task 3: ParkingLot Class
# Store multiple parking spots.
# Methods:
# add_spot() → add new parking spots.
# show_spots() → display all spots and their status.
# park_vehicle(vehicle) → find suitable spot and park.
# unpark_vehicle(vehicle) → remove from spot and calculate fee.
# Task 4: Payment (Abstraction + Polymorphism)
# When un-parking a vehicle, calculate fee (based on hours).
# Ask user for payment method → process payment using appropriate child class.
# Task 5: Main Program
# Create a parking lot with mixed spots.
# Create multiple vehicle objects.
# Park/unpark vehicles.
# Demonstrate encapsulation, inheritance, polymorphism, and abstraction throughout.
 

        
        
        
        
        
        
        
    