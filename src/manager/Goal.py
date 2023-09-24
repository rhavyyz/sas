from src.manager.SystemClass import SystemClass

class Goal:
    props : list[str] = []
    __checker : callable[[dict[str, any]], bool]

    __action : callable[[SystemClass], bool]

    def __init__(self, props : list[str], checker : callable[[any], bool], action : callable[[SystemClass], bool] ) -> None:
        self.props = props.copy()
        self.__checker = checker
        self.__action = action
    
    def check(self, args : dict[str, any]) -> bool:
        return self.__checker(args.copy())
    
    def act(self, sys : SystemClass) -> bool:
        return self.__action(sys)