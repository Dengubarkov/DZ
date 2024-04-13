from salary.salaryemployee import SalaryEmployee
from salary.payrollsystem import PayrollSystem
from salary.hourlyemployee import HourlyEmployee
from salary.comissionemployee import ComissionEmployee



salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
commission_employee = ComissionEmployee(3, "Николай Хорольский", 1000, 250)
payroll_system = PayrollSystem()
payroll_system.calculate([salary_employee, hourly_employee, commission_employee])
