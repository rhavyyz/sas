import json
from dataclasses import dataclass
from src.common.temperature_changer import TemperatureChanger
from src.common.temperature_changer import TemperatureChanger
from src.register_obj import RegisterObj

class Env(RegisterObj):
    temp : float 
    temp_changers : list[TemperatureChanger] = []
    __file_path : str


    def __to_json_str(self) -> str:
        return '{\n' + f'"temp": {self.temp}\n' + '}\n'
    
    def __get_info(self):
        f = open(self.__file_path)
        obj = dict(json.load(f))
        f.close()

        for key, value in obj.items():
            setattr(self, key, value)

    def __save_changes(self):
        f = open(self.__file_path, "w")
        f.write(self.__to_json_str())
        f.close()


    def __init__(self, path : str) -> None:
        self.__file_path = path

        self.__get_info()

    def log(self) -> str:
        res = "-="*40 + "\n"

        res += str(self.temp) + "\n"

        res += self.temp_changers.__str__() + "\n"

        return res

    def register(self, obj: TemperatureChanger) -> None:
        self.temp_changers.append(obj)

    def interact(self, change: float):
        self.temp += change
        self.__save_changes()
