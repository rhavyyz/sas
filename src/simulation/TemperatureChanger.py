from src.util.Saveble import Saveble

class TemperatureChanger(Saveble):
    desired_temperature : float

    def __init__(self, desired_temperature) -> None:
        self.desired_temperature = desired_temperature


    # This method is meant to return the value in calories or any other 
    # thermodynamics unit
    def calc(self, current_temperature : float, time_pace : int) -> float:
        return (self.desired_temperature - current_temperature)/2 