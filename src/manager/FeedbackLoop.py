# from src.manager.SystemClass import SystemClass
from src.manager.SystemClass import SystemClass
from src.manager.Goal import Goal

class FeedbackLoop (SystemClass):
    
    system : SystemClass
    __goals : list[Goal] = []

    def __init__(self, system : SystemClass) -> None:
        self.system = system

    def __get_values(self, props : list[str]):
        return {prop: self.system[prop] for prop in props}

    def add(self, *args : tuple[Goal] | tuple[list[Goal]]) -> None:
        if len(args) == 0:
            raise Exception("add function should recieve at least one paramether")

        if isinstance(args[0], Goal):
            return self.__goals.extend(args)
        
        for l in args:
            self.__goals.extend(l)

    def single_execution(self):
        for goal in self.__goals:
            if goal.check(self.__get_values(goal.props)):
                goal.act(self.system)
