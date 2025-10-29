from vehicle_rentals.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self,make,model,rate,hours,days,weight,driver_name,driver_bata):
        super().__init__(model,rate)
        self.make=make
        self.hours=hours
        self.days=days
        self.weight=weight
        self.driver_name=driver_name
        self.driver_bata=driver_bata
    def calculate_rental(self):
        base_cost = self.hours * self.days
        driver_cost = self.driver_bata * self.days
        weight_charge = self.weight * 2
        rental_cost = base_cost + driver_cost+weight_charge
        return rental_cost
    def display_rental(self):
        print(f"Vehicle name:{self.make}")
        print(f"vehicle model:{self.model}")
        print(f"Hours:{self.hours}")
        print(f"Days:{self.days}")
        print(f"weight:{self.weight}")
        print(f"driver name:{self.driver_name}")
        print(f"driver bata:{self.driver_bata}")
        print(f"Total rental:₹{self.calculate_rental()}")


