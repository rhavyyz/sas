from src.simulation.Environment import Environment
from src.simulation.TemperatureChanger import TemperatureChanger
from src.util.Logger import Logger
from src.managed.AC import AC
from src.manager.FeedbackLoop import FeedbackLoop
from src.manager.Goal import Goal 

from threading import Lock

lock = Lock()
logger = Logger()
e = Environment(lock, logger)

air_conditioner = AC(45)

loop = FeedbackLoop(air_conditioner, lock)

e.add(air_conditioner)

# print(air_conditioner.__dict__)

loop.add(Goal(['sense', 'desired_temperature'], 
              lambda d : d["sense"]() <= d["desired_temperature"],
              lambda sys : sys.set_stand_by(True)),
         Goal(['sense', 'desired_temperature', 'stand_by'], 
              lambda d : d["sense"]() > d["desired_temperature"] + 2 and d["stand_by"],
              lambda sys : sys.set_stand_by(False)),
              )

loop.start()

for c in range(0, 10):
    e.single_execution()