from constants import STORAGE, API_KEY, CITY, RESET
from src.util.Saveble import Saveble
from src.simulation.TemperatureChanger import TemperatureChanger
from src.util.Logger import Logger
from src.managed.AC import AC
from threading import Lock

import requests, datetime

class Environment(Saveble):
    today : str
    
    temperature : float

    _changers : list[TemperatureChanger] = []

    __lock : Lock
    __logger : Logger
    __time_pace : int = 10
    __specific_heat_capacity : float = 1

    def sync_get_temperature(self):
        with self.__lock:
            return self.temperature
        
    def sync_set_temperature(self, value : float):
        with self.__lock:
            self.temperature = value

    def sync_increase_temperature(self, value : float):
        with self.__lock:
            self.temperature += value

    def _save(self,) -> None:
        return super()._save(STORAGE + "Environment.txt")

    def add(self, *args : tuple[TemperatureChanger] | tuple[list[TemperatureChanger]]) -> None:
        if len(args) == 0:
            raise Exception("add function should recieve at least one paramether")

        for arg in args: 
            if isinstance(arg, AC):
                self._changers.append(arg)
                # Maybe refactor this line because of logic inconsistens
                arg.configure_sensor(self.sync_get_temperature)
                continue

            if isinstance(arg, TemperatureChanger):
                self._changers.append(arg)
                continue
            if issubclass(type(arg), list):
                self.add(*arg)

    def __init__(self, lock : Lock,logger = None) -> None:
        if logger == None:
            self.__logger = Logger()
        else:
            self.__logger = logger

        self.__lock = lock

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

            self.__logger.log(f"Delta t: {tot} after processing {changer},")

        self.__logger.log('\n')

        self.__logger.log( f'Initial temperature {self.temperature}')
        
        self.sync_increase_temperature(tot / self.__specific_heat_capacity)

        self.__logger.log(f'Final temperature {self.temperature}')
        self.__logger.log("-" * 40)

        self._save()