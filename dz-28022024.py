import re
def pwd_guard(p):
    res = ""
    reg = r"[a-zA-Z@0-1_-]+"
    if len(p)>6 and len(p)<18:
        for i in p:
            if re.findall(reg,i):
                res+=i
            else:
                res = "В пароле содержаться недопустимые символы"
                break
            res = re.findall(reg,p)
    else:
        res = "Число символов не соответствует заданным параметрам(от 6 до 16)"
    return res


pwd = input("Введите пароль: ")
print(pwd_guard(pwd))
