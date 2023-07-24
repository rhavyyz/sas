from src.env import environment, Env
from src.simulation.main import simulate

from src.system.ac_managed import base_path_acs, AcManaged

from os import listdir
from os.path import isfile, join

def setup_acs(environment : Env):
    ac_files = [f for f in listdir(base_path_acs) if isfile(join(base_path_acs, f))]

    ac_instances = [AcManaged(ac_file) for ac_file in ac_files]
    
    for ac_instance in ac_instances:
        environment.register(ac_instance)

        # here we should run our system manager for each ac instance as well
    

def main():
    setup_acs(environment)

    simulate(environment)


if __name__ == "__main__":
    main()
