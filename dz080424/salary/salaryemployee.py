from .employee import Employee


class SalaryEmployee(Employee):
    """Административные работники с фиксированной зарплатой"""

    def __init__(self, kod, name, weekly_salary):
        super().__init__(kod, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
