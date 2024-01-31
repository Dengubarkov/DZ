matem = ["Матвей", "Евгения", "Михаил", "Максим", "Наталья"]
phisic = ["Максим","Матвей","Александр"]
print("Все призёры:",set(matem)|set(phisic))
matem = set(matem)&set(phisic[0:3])
print("Призёры обеих олимпиад:",matem)
del phisic
print("Обновленный список призеров по математике:", matem)


