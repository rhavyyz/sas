from src.env import Env

class SensorSystem:

    environment : Env

    def __init__(self, environment : Env):
        self.environment = environment

    def sense_temperature(self):
        return self.environment.temp
    
    