class Vehicle:
    def __init__(self,model,rate):
        self.model=model
        self.rate=rate
    def calculate_rental(self):
        return self.rate
    def display_rental(self):
        print(f"{self.model}:Rent for vehicle ₹{self.calculate_rental()}")