from time import sleep
from src.env import Env

base_path = "files/"

# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
#  r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.

def reset_file(path : str, data : str = ""):
    f = open(base_path + path, "w")
    f.write(data)
    f.close()

def status_check():
    f = open(base_path+ "status.txt" , 'r')
    line  = f.readline().strip().upper()
    f.close()

    return line == "TRUE"

def to_log_file(data : str):
    f = open(base_path + "log.txt", "a+")

    f.write(data)

    f.close()

def simulate(env : Env):

    reset_file("log.txt")

    status = True
    reset_file("status.txt", "TRUE")


    while status:

        for temp_changer in env.temp_changers:
            temp_changer.act(5)

        to_log_file(env.log())

        status = status_check()
        sleep(5)

    print("simulation ended with status:")
    print(env.log())