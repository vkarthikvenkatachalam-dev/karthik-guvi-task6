from vehicle_rentals.vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self,make,model,rate,hours,kilometers):
        super().__init__(model,rate)
        self.make=make
        self.hours=hours
        self.kilometers=kilometers
    def calculate_rental(self):
        return self.rate * self.hours * self.kilometers
    def display_rental(self):
        print(f"Bike make: {self.make}")
        print(f"Bike model: {self.model}")
        print(f"Rate per hour: {self.rate}")
        print(f"No of hours: {self.hours}")
        print(f"kilometers covered: {self.kilometers}")
        print(f"Total rental: ₹{self.calculate_rental()}")

