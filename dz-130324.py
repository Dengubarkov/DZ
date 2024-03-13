class Person:
    def __init__(self, name, old):
        self.__name = ""
        self.__old = 0
        if Person.__check(name,old):
            self.__name = name
            self.__old = old

    def __check(x, y):
        if isinstance(x,str) and isinstance(y,(int,float)):
            return True
        if not isinstance(x,str):
            print("Имя должно состоять из букв алфавита")
        if not isinstance(y,(int,float)):
            print("Возраст должен состоять из чисел")

    def __check_old(x):
        if isinstance(x,(int,float)):
            return True
        else:
            return False

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        if Person.__check_old(new_old):
            self.__old = new_old
        else:
            print("Возраст должен состоять из чисел")
    @old.deleter
    def old(self):
        del self.__old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("Имя должно состоять из букв алфавита")

    @name.deleter
    def name(self):
        del self.__name


human = Person("Irina", 26)
print(human.__dict__)
human.name = "Igor"
print(human.name)
human.old = 31
print(human.old)
del human.name
print(human.__dict__)