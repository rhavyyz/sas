from constants import STORAGE, API_KEY, CITY, RESET
from src.util.Saveble import Saveble
from simulation.TemperatureChanger import TemperatureChanger
from src.util.Logger import Logger

import requests, datetime

class Environment(Saveble):
    today : str
    temperature : float

    _changers : list[TemperatureChanger] = []

    __logger : Logger
    __time_pace : int = 10
    __specific_heat_capacity : float = 1

    def _save(self,) -> None:
        return super()._save(STORAGE + "Environment.txt")

    def add(self, *args : tuple[TemperatureChanger] | tuple[list[TemperatureChanger]]) -> None:
        if len(args) == 0:
            raise Exception("add function should recieve at least one paramether")

        if isinstance(args[0], TemperatureChanger):
            return self._changers.extend(args)
        
        for l in args:
            self._changers.extend(l)

    def __init__(self, logger = None) -> None:
        if logger == None:
            self.__logger = Logger()
        else:
            self.__logger = logger

        self.today = datetime.datetime.now().strftime("%d/%m/%y")
        
        if not RESET:
            with open(STORAGE + "Environment.txt") as f:

                f.readline()
                self.temperature = float( Saveble.get_value(f.readline()) )
    
        else:
            res = requests.get(f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}')

            data = res.json()

            self.temperature = data['current']['temp_c']

            self._save()

        self.add(TemperatureChanger(self.temperature))

    def single_execution(self) -> None:

        tot = float(0)

        for changer in self._changers:
            tot += changer.calc(self.temperature, self.__time_pace)

            self.__logger.add(tot)

        self.__logger.log('\n')

        self.__logger.add(self.temperature)
        self.temperature += tot / self.__specific_heat_capacity

        self.__logger.add(self.temperature)
        self.__logger.log("\n"+"-" * 40)


        self._save()