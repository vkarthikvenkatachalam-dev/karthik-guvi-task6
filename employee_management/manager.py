from employee_management.employee import Employee


class Manager(Employee):
    def __init__(self,name,base_salary,perfomance_bonus,incentive):
        super().__init__(name,base_salary)
        self.perfomance_bonus = perfomance_bonus
        self.incentive = incentive

    def calculate_salary(self):
        return self.base_salary + self.perfomance_bonus + self.incentive

    def display_salary(self):
        print(f"Manager_Name: {self.name}")
        print(f"Base_salary: ₹{self.base_salary}")
        print(f"perfomance_bonus: ₹{self.perfomance_bonus}")
        print(f"Incentive: ₹{self.incentive}")
        print(f"Total_salary: ₹{self.calculate_salary()}")