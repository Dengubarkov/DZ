from .employee import Employee

class HourlyEmployee(Employee):
    """Сотрудники с почасовой оплатой"""
    def __init__(self, kod, name, hours_worked, houers_rate):
        super().__init__(kod, name)
        self.hours_worked = hours_worked
        self.hours_rate = houers_rate
    def calculate_payroll(self):
        return self.hours_worked*self.hours_rate
