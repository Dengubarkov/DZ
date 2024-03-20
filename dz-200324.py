import math


class Pair:
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def ab(self,a=None,b=None):
        if a: self.a = a
        if b: self.b = b
    def suma(self):
        print("Сумма:",self.a+self.b)
    def pr(self):
        print ("Произведение:",self.a*self.b)


class RightTriangle(Pair):
    def __init__(self,a,b):
        super().__init__(a,b)
        self.hypo = a ** 2 + b ** 2
    def hypot(self):
        print("Гипотенуза ▲ABC",self.hypo)
    def info(self):
        print(f"Прямоугольный треугольник ▲ABC({self.a}, {self.b}, {self.hypo})")

    def st(self):
        s = round(0.5 * self.a * self.b-math.sin(self.a),1)
        print("Площадь ▲ABC:", s)

x = RightTriangle(5,8)
x.hypot()
x.info()
x.st()
print()
x.suma()
x.pr()
x.ab(10,20)
x.hypot()
x.suma()
x.pr()
x.st()