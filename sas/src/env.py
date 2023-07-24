from dataclasses import dataclass
from src.common.temperature_changer import TemperatureChanger
from src.common.temperature_changer import TemperatureChanger
from src.register_obj import RegisterObj


# @dataclass 
class Env(RegisterObj):
    temp : float = 30
    temp_changers : list[TemperatureChanger] = []

    def log(self) -> str:
        res = "-="*40 + "\n"

        res += str(self.temp) + "\n"

        res += self.temp_changers.__str__() + "\n"

        return res

    def register(self, obj: TemperatureChanger) -> None:
        self.temp_changers.append(obj)

    def interact(self, change: float):
        self.temp += change

environment = Env()
