#Вариант 1, площадь опередлена глобальной переменной
s1 = 0

def out1(a,b,c):
    global s1
    def inner():
        return a*b, b*c, c*a
    s1 = sum(inner())*2
out1(2,4,6)
print(s1)

#Вариант 2, площадь опередлена локальной переменной

def out2(a,b,c):
    def inner():
        s2 = 0
        s2 = 2*(a*b+b*c+c*a)
        return s2

    return inner

print(out2(5,8,2)())

#Вариант 3, использование nonlocal

def out3(a,b,c):
    s3 = 0
    def inner():
        nonlocal s3
        s3 = 2*(a*b+b*c+c*a)
    inner()
    return s3

print(out3(1,6,8))


