from vehicle_rentals.bike import Bike
from vehicle_rentals.car import Car
from vehicle_rentals.truck import Truck


class Rental:

    def __init__(self):
        self.car = Car("Ford","Fiesta",20,5,10,"Sam",40)
        self.bike = Bike("Yamaha","FZ",20,7,10)
        self.truck = Truck("Ashok_leyland","Stallion",25,5,3,12000,"Shiva",12)

    def rental_details(self):
        print("\n ---Rental for car---")
        self.car.calculate_rental()
        self.car.display_rental()
        print("\n ---Rental for bike---")
        self.bike.calculate_rental()
        self.bike.display_rental()
        print("\n ---Rental for Truck---")
        self.truck.calculate_rental()
        self.truck.display_rental()


rnt = Rental()
rnt.rental_details()
