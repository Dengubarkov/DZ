import math


class Plosh:
    count = 0
    def __del__(self):
        print(f"Количество подсчетов площади: {Plosh.count}")
    @staticmethod
    def geron(a,b,c):
        Plosh.verify(a,b,c)
        p = (a+b+c)/2
        print(f"Площадь треугольника по формуле Герона({a},{b},{c}): {math.sqrt(p*(p-a)*(p-b)*(p-c))}")
        Plosh.count += 1
    @staticmethod
    def square(a):
        Plosh.verify(a)
        print(f"Площадь квадрата({a}): {a*a}")
        Plosh.count += 1
    @staticmethod
    def rectangle(a,b):
        Plosh.verify(a, b)
        print(f"Площадь прямоугольника({a},{b}): {a * b}")
        Plosh.count += 1
    @staticmethod
    def verify(*arg):
        for i in arg:
            if not isinstance(i,(int,float)):
                raise TypeError("Нужно вводить число!")




s1 = Plosh()
s1.geron(3,4,5)
s1.square(7)
s1.rectangle(2,6)