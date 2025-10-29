class Employee:
    def __init__(self,Name,Base_Salary):
        self.name=Name
        self.base_salary=Base_Salary

    def calculate_salary(self):
        return self.base_salary

    def display_salary(self):
        print(f"{self.name}: Total salary ₹{self.calculate_salary()}")
