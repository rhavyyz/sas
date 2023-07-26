# employee.py

# from datetime import date

# class Employee:
#     def __init__(self, name, birth_date):
#         self.name = name
#         self.birth_date = birth_date

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value.upper()

#     @property
#     def birth_date(self):
#         return self._birth_date

#     @birth_date.setter
#     def birth_date(self, value):
#         self._birth_date = date.fromisoformat(value)

from src.register_obj import RegisterObj

class TemperatureChanger:

    # Temperature it changes per second
    change_rate : float = 1
    registerObj : RegisterObj

    def __init__(self, register_obj: RegisterObj, change_rate : float) -> None:
        self.registerObj = register_obj
        self.change_rate = change_rate

        self.registerObj.register(self)

    def calc(self, time : float) -> float:
        return self.change_rate * time

    def act(self, time : float = 1):
        self.registerObj.interact( self.calc(time))
