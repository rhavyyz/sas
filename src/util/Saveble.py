from src.util.Gettable import Gettable
from abc import ABC


#Defines a __save method that stores all non private atributes in a path 
#the attributes are stored in order of declaration with this strucutre
#key:value
class Saveble(Gettable, ABC):

    def _save(self, path : str) -> None:
        
        with open(path, 'w') as f:
        
            for key in self.__dict__:
                if key.find("_") == 0:
                    continue
                f.write(f'{key}:{self.__dict__[key]}\n')

    @classmethod
    def get_value(cls, line : str) -> str:
        return line.split(":")[1].strip()
    
    @classmethod
    def get_key(cls, line : str) -> str:
        return line.split(":")[0].strip()
