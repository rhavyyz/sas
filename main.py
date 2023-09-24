from simulation.Environment import Environment
from simulation.TemperatureChanger import TemperatureChanger
from src.util.Logger import Logger


logger = Logger()
e = Environment(logger)

e.add(TemperatureChanger(20))

for c in range(0, 10):
    e.single_execution()