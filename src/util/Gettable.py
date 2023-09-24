from abc import ABC

class Gettable(ABC):
     def __getitem__(self, key : str) -> any:
        return self.__dict__[key]