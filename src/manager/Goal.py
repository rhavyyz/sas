from src.manager.SystemClass import SystemClass
from typing import Callable

class Goal:
    props : list[str] = []

    __checker : Callable[[dict[str, any]], bool]
    __action : Callable[[SystemClass], bool]

    def __init__(self, props : list[str], checker : Callable[[dict[str, any]], bool], action : Callable[[SystemClass], bool] ) -> None:
        self.props = props.copy()
        self.__checker = checker
        self.__action = action
    
    # It recieves a function that checks if an action is needed to be taken 
    def check(self, args : dict[str, any]) -> bool:
        return self.__checker(args.copy())
    
    # A function that represents the adaptation by itself
    # it should recieve the managed system and  
    def act(self, sys : SystemClass) -> bool:
        return self.__action(sys)