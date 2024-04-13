from .salaryemployee import SalaryEmployee
class ComissionEmployee(SalaryEmployee):
    """Торговые представители-получают фиксированную зарплату+комиссию"""
    def __init__(self,kod, name,weekly_salary, comission):
        super().__init__(kod, name,weekly_salary)
        self.comission = comission

    def calculate_payroll(self):
        return self.weekly_salary+self.comission