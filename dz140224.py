print(list(filter(lambda x:x==x[::-1],('madam','fire','tomato','book','kiosk','mom'))))
print(list(filter(lambda x:x==x[::-1],(input("Введите слово: ") for i in range(int(input("Введите количество слов: ")))))))
