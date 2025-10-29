from employee_management.Regular_employee import RegularEmployee
from employee_management.contract_employee import ContractEmployee
from employee_management.manager import Manager


class Salary:
    def __init__(self):
      self.Regular_employee = RegularEmployee("Karthik V",30000,5000)
      self.Contract_employee = ContractEmployee("Anand",750,150)
      self.Manager = Manager("Sangeeta",60000,15000,8000)

    def salary_details(self):
        print("\n ----Regular Employee salary----")
        self.Regular_employee.calculate_salary()
        self.Regular_employee.display_salary()
        print("\n ----Contract Employee salary---")
        self.Contract_employee.calculate_salary()
        self.Contract_employee.display_salary()
        print("\n ----Manager salary----")
        self.Manager.calculate_salary()
        self.Manager.display_salary()


sly = Salary()
sly.salary_details()



