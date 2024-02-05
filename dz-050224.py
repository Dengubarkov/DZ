sales = {'John': {'N': 3056,
                'S': 8463,
                'E': 8441,
                'W': 2694},
        'Tom': {'N': 4832,
                'S':6786,
                'E': 4737,
                'W': 3612},
        'Anne': {'N': 5239,
                 'S': 4802,
                 'E': 5820,
                 'W': 1859},
    'Fiona': {'N': 3904,
              'S': 3645,
              'E': 8821,
              'W': 2451}
}
for x in sales:
    print(x)
    for y in sales[x]:
        print(y,":",sales[x][y])
while True:
    name = input("Имя: ")
    if name in sales.keys():
        while True:
            region = input("Регион: ")
            if region in sales[name].keys():
                print(sales[name][region])
                while True:
                    new = input("Новое значение: ")
                    try:
                        sales[name][region] = round(float(new))
                        print(sales[name])
                        break
                    except ValueError:
                        print("Ошибка ввода!\n Пожалуйста введите число")
                break
            else:
                print("Такого региона не существует!\n Пожалуйста повторите ввод.")
        break
    else:
        print("Такого сотрудника не существует!\n Пожалуйста повторите ввод.")


