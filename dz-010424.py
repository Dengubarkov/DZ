from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def s(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    title = "===Квадрат==="

    def __init__(self, a, color):
        self.a = a
        super().__init__(color)

    def perimetr(self):
        return f"Периметр: {self.a * 4}"

    def s(self):
        return f"Площадь: {sqrt(self.a)}"

    def draw(self):
        dr = ""
        for i in range(self.a):
            dr += "*"*self.a+"\n"

        return dr

    def info(self):
        print(f"{self.title}\nСторона: {self.a}\nЦвет: {self.color}\n{self.s()}\n{self.perimetr()}\n{self.draw()}")


class Rectangle(Shape):
    title = "===Прямоугольик==="

    def __init__(self, a,b,color):
        self.a = a
        self.b = b
        super().__init__(color)

    def perimetr(self):
        return f"Периметр: {(self.a + self.b)*2}"

    def s(self):
        return f"Площадь: {self.a*self.b}"

    def draw(self):
        dr = ""
        for i in range(self.b):
            dr += "*"*self.a+"\n"

        return dr

    def info(self):
        print(f"{self.title}\nСторона 1: {self.a}\nCторона 2: {self.b}\nЦвет: {self.color}\n{self.s()}\n{self.perimetr()}\n{self.draw()}")



class Triangle(Shape):
    title = "===Треугольник==="

    def __init__(self, a,b,c,color):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(color)

    def perimetr(self):
        return f"Периметр: {self.a + self.b+self.c}"

    def s(self):
        return f"Площадь: {(((self.a + self.b+self.c)/2)-self.a)*(((self.a + self.b+self.c)/2)-self.b)}"

    def draw(self):
        dr = ""
        x = self.a
        y = self.b
        z = self.c
        for i in range(1,y+1):
            dr += " "*(x-i)+"*"*i+"\n"




        return dr.center(y,"*")
    def info(self):
        print(f"{self.title}\nСторона 1: {self.a}\nCторона 2: {self.b}\nCторона 3: {self.c}\nЦвет: {self.color}\n{self.s()}\n{self.perimetr()}\n{self.draw()}")




lst=[Square(4,"red"),Rectangle(10,5,"green"),Triangle(11,6,6,"Yellow")]

for i in lst:
    i.info()
