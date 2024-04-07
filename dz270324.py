class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    @staticmethod
    def clock_valid(x):
        if isinstance(x, Clock):
            return x
        else:
            raise ArithmeticError("Некорректный правый операнд")

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec == other.sec:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __sub__(self, other):
        Clock.clock_valid(other)
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        Clock.clock_valid(other)
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        Clock.clock_valid(other)
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        Clock.clock_valid(other)
        return Clock(self.sec % other.sec)

    def __ge__(self, other):
        Clock.clock_valid(other)
        if self.sec >= other.sec:
            return True
        return False

    def __gt__(self, other):
        Clock.clock_valid(other)
        if self.sec > other.sec:
            return True
        return False

    def __lt__(self, other):
        Clock.clock_valid(other)
        if self.sec < other.sec:
            return True
        return False

    def __le__(self, other):
        Clock.clock_valid(other)
        if self.sec <= other.sec:
            return True
        return False


c1 = Clock(100)
c2 = Clock(200)
print("Задача №1\nC1:", c1.get_format_time(), "C2:",c2.get_format_time())

print("C1-C2:", (c1 - c2).get_format_time())
print("C1*C2:", (c1 * c2).get_format_time())
print("C1//C2:", (c1 // c2).get_format_time())
print("C1%C2:", (c1 % c2).get_format_time())
c1 -= c2
print("c1-=c2", c1.get_format_time())
# И так далее
print("Задача №2\nc1:",c1.sec,"c2:",c2.sec)
print("c2>c1",c2>c1)
print("c2>=c1",c2>=c1)
print("c2<c1",c2<c1)
print("c2<=c1",c2<=c1)