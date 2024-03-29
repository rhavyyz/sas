import json
import uuid
from src.register_obj import RegisterObj
from src.system.sensor_system import SensorSystem
from src.common.temperature_changer import TemperatureChanger
from src.register_obj import RegisterObj

base_path_acs = "files/ac_files/"

# MAPEK

class AcManaged(TemperatureChanger):
    turbo : bool 
    stand_by : bool 
    desired_temp : int
    __file_path : str
    sensor_system : SensorSystem

    def __to_json_str(self) -> str:
        return '{\n' + f'"turbo": {str(self.turbo).lower()},\n "stand_by": {str(self.stand_by).lower()},\n "desired_temp": {self.desired_temp}\n' + '}\n'
    
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

    def __ctor_1(self, path : str, register_obj : RegisterObj):
        self.__file_path = path
        self.__get_info()
        super().__init__(register_obj, -0.5) # <---- future changes here  

    def __ctor_2(self, turbo : bool, stand_by : bool, desired_temp : int):
        self.turbo = turbo
        self.stand_by = stand_by
        self.desired_temp = desired_temp

        self.__file_path = base_path_acs + uuid.uuid4().__str__ + '.json'

        self.__save_changes()

    def __init__(self, sensor_system : SensorSystem ,*args) -> None:
        self.sensor_system = sensor_system
        self.change_rate = -0.5
    
        
        if len(args) == 2:
            return self.__ctor_1(*args)
        elif len(args) == 4:
            return self.__ctor_2(*args)
    
    def increase_desired_temp(self):
        self.desired_temp += 1
        self.__save_changes()

    def decrease_desired_temp(self):
        self.desired_temp -= 1
        self.__save_changes()

    def toggle_stand_by(self):
        self.stand_by = not self.stand_by
        self.__save_changes()

    def calc(self, time: float):

        # if self.desired_temp >= self.sensor_system.sense_temperature():
        #     self.change_rate = 0

        return super().calc(time)