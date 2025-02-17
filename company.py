from employee import SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current employees:')
        for employee in self.employees:
            print(employee.fname, employee.lname)
            print('----------------------------------')

    def pay_employees(self):
        print('Paying employees...')
        for employee in self.employees:
            print('Paycheck for: ', employee.fname, employee.lname)
            print(f'Amount: , ${employee.calculate_paycheck():,.2f}')
            print('----------------------------------')

def main():

    my_company = Company()

    employee1 = SalaryEmployee('Bob', 'Jons', 60000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Jane', 'Hicks', 25,50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Sue', 'Smith', 40000,15, 200)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()