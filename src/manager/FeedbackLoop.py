# from src.manager.SystemClass import SystemClass
from src.manager.SystemClass import SystemClass
from src.manager.Goal import Goal
from threading import Lock, Thread
from time import sleep

class FeedbackLoop (SystemClass):
    
    system : SystemClass
    __goals : list[Goal] = []
    __lock : Lock
    __thread : Thread
    
    # returns a dict with the values of "props"
    def __get_values(self, props : list[str]):
        with self.__lock:
            return {prop: self.system[prop] for prop in props}

    # add Goals 
    def add(self, *args : tuple[Goal] | tuple[list[Goal]]) -> None:
        with self.__lock:
            if len(args) == 0:
                raise Exception("add function should recieve at least one paramether")

            if isinstance(args[0], Goal):
                return self.__goals.extend(args)
            
            for l in args:
                self.__goals.extend(l)

    # represents a singles execution of the loop
    def single_execution(self):
        for goal in self.__goals:
            
            if goal.check(self.__get_values(goal.props)):
                with self.__lock:
                    goal.act(self.system)

    def loop(self):
        while(True):
            self.single_execution()
            # sleep(3)

    def __init__(self, system : SystemClass, lock : Lock ) -> None:
        self.system = system
        self.__lock = lock
        self.__thread = Thread( target= self.loop, daemon=True)

    # starts the encapsulated thread
    def start(self):
        self.__thread.start()