class Market:
    def __init__(self, name, income):
        self.name = name
        self.__income = income

    def get_income(self):
        return self.__income

    def set_income(self, new_income):
        self.__income = new_income


m1 = Market('Korzinka', 100000)

print(m1.name)
print(m1.get_income())

m1.set_income(150000)

print(m1.get_income())
