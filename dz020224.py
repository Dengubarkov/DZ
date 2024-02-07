students = {}
for i in range(int(input("Введите количество студентов: "))):
    print("Введите данные студента",i+1)
    students["Student-"+str(i+1)]={"Fname":input("Введите фамилию: "),"Name":input("Введите имя: "),
                                 "Score":int(input("Балл: "))}
scores = 0
for i in students.items():
    scores += students[i[0]]["Score"]
sr = scores/len(students)
print("Средний балл: ",round(sr),". Студенты с баллом выше среднего:",sep="")
for i in students.items():
    if students[i[0]]["Score"] > sr:
        print(students[i[0]]["Fname"],students[i[0]]["Name"])
