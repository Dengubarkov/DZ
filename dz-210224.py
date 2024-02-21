fio = input("Введите ФИО: ").split()
try:
    print(f"{fio[0].title()} {fio[1][0].upper()}. {fio[2][0].upper()}.")
except IndexError:
    print("Данные введены не корректно")