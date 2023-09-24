from src.manager.SystemClass import SystemClass
from src.simulation.TemperatureChanger import TemperatureChanger

class AC( TemperatureChanger ,SystemClass):
    stand_by : bool = False

    def set_stand_by(self, value : bool):
        self.stand_by = value

    def calc(self, current_temperature: float, time_pace: int) -> float:
        if self.stand_by:
            return 0
        return super().calc(current_temperature, time_pace)