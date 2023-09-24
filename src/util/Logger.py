class Logger:

    __content : list[any] = []

    def __log(self, *args):
        print(*args)

    def add(self, content : any) -> None:
        self.__content.append(content)

    def log(self, content = []) -> None:
        
        
        if issubclass(type(content), (tuple, list)):
            self.__content.extend(content)
        else:
            self.__content.append(content)


        self.__log(*self.__content)

        self.__content.clear()