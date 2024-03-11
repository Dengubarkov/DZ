class Car:
    def __init__(self,model,year,vendor,power,color,price):
        self.model = model
        self.year = year
        self.vendor = vendor
        self.power = power
        self.color = color
        self.price = price
    def print_info(self):
         print("Данные автомобиля".center(40, "*"))
         print(f"Название модели: {self.model}\nГод выпуска: {self.year}\n"
              f"Производитель:  {self.vendor}\nМощность двигателя: {self.power}\n"
              f"Цвет машины: {self.color}\nЦена:{self.price}")
         print("="*40)


    def set_model(self, model):
        self.model = model

    def set_year(self,year):
        self.year = year

    def set_vendor(self,vendor):
        self.vendor = vendor

    def set_power(self,power):
        self.power = power


    def set_color(self,color):
        self.color = color


    def set_price(self,price):
        self.price = price

    def get_model(self):
        print("Модель: ", self.model)

    def get_year(self):
        print("Год выпуска: ", self.year)

    def get_vendor(self):
        print("Производитель: ", self.vendor)

    def get_power(self):
        print("Мощность двигателя: ", self.power)

    def get_color(self):
        print("Цвет авто: ", self.color)

    def get_price(self):
        print("Цена: ", self.price)

car1 = Car("x7 M50i", "2021", "BMW", "530 л.с.", "White ", "10790000")
car2 = Car("2109", "2001", "Lada", "60 л.с.", "Purple ", "30000")
car1.print_info()
car2.print_info()
car1.set_year("2019")
car1.get_year()
car2.set_price("100000")
car1.print_info()
car2.print_info()
