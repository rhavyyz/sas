from src.manager.SystemClass import SystemClass
from src.simulation.TemperatureChanger import TemperatureChanger
from typing import Callable

class AC( TemperatureChanger ,SystemClass):
    stand_by : bool = False
    sense : Callable[[any], float] = lambda self : -274
    __HARD_CODED__ = float(-2)

    def __init__(self, desired_temperature) -> None:
        self.stand_by = False
        super().__init__(desired_temperature)

    def configure_sensor(self, sense : Callable[[any], float]):
        self.sense = sense

    def toggle_stand_by(self):
        self.stand_by = not self.stand_by

    def set_stand_by(self, stand_by : bool):
        self.stand_by = stand_by

    def calc(self, current_temperature: float, time_pace: int) -> float:
        if self.stand_by:
            return 0
        return super().calc(current_temperature, time_pace)