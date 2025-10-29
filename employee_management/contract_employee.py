from employee_management.employee import Employee


class ContractEmployee(Employee):
    def __init__(self,name,hourly_rate,worked_hours):
        super().__init__(name,Base_Salary=0)
        self.hourly_rate = hourly_rate
        self.worked_hours=worked_hours
    def calculate_salary(self):
        return self.hourly_rate * self.worked_hours
    def display_salary(self):
        print(f"Contract Employee_Name: {self.name}")
        print(f"Hourly_rate: {self.hourly_rate}")
        print(f"Worked_hours: {self.worked_hours}")
        print(f"Total salary: ₹{self.calculate_salary()}")


