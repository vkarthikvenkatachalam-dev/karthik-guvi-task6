from vehicle_rentals.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,make,model,rate,hours,driver_bata,driver_name,kilometers):
        super().__init__(model,rate)
        self.make=make
        self.hours=hours
        self.driver_bata=driver_bata
        self.driver_name=driver_name
        self.kilometers=kilometers
    def calculate_rental(self):
        base_cost = self.hours * self.kilometers
        driver_cost = self.rate * self.driver_bata
        rental_cost = base_cost + driver_cost
        return rental_cost

    def display_rental(self):
        print(f"Vehicle name: {self.make}")
        print(f"Vehicle model: {self.model}")
        print(f"Driver name: {self.driver_name}")
        print(f"Rate per hour: {self.rate}")
        print(f"No of hours: {self.hours}")
        print(f"Driver bata: {self.driver_bata}")
        print(f"Total rental:₹{self.calculate_rental()}")


