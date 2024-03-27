class Student:
    def __init__(self, name):
        self._name = name
        self.notebook = self.NB()

    def show(self):
        print(f"{self._name} => {self.notebook.model}, {self.notebook.cpu}, {self.notebook.ram}")

    class NB:
        def __init__(self):
            self.model = "HP"
            self.cpu = "i7"
            self.ram = "16"


Student("Roman").show()
Student("Vladimir").show()
