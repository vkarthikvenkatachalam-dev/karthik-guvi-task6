from employee_management.employee import Employee


class RegularEmployee(Employee):
    def __init__(self,name,base_salary,bonus):
        super().__init__(name,base_salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.base_salary + self.bonus
    def display_salary(self):
        print(f"Employee_Name: {self.name}")
        print(f"Employee_Base_salary: ₹{self.base_salary}")
        print(f"Employee_Bonus: ₹{self.bonus}")
        print(f"Total_Salary: ₹{self.calculate_salary()}")
