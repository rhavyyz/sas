import json

from src.env import Env
from src.simulation.main import simulate

from src.simulation.main import base_path ## fix this to put all base_paths into one constant files
from src.system.ac_managed import base_path_acs, AcManaged

from os import listdir
from os.path import isfile, join

def setup_env() -> Env:
    return Env(base_path + 'env_config.json')


def setup_acs(environment : Env):
    ac_files = [f for f in listdir(base_path_acs) if isfile(join(base_path_acs, f))]

    print(len(ac_files))

    ac_instances = [AcManaged( base_path_acs+ ac_file, environment) for ac_file in ac_files]

    ac_instances[0].decrease_desired_temp()

    # here we should run our system manager for each ac instance as well
    

def main():
    environment = setup_env()
    
    environment.interact(1)

    setup_acs(environment)

    simulate(environment)


if __name__ == "__main__":
    main()
