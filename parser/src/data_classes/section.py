from dataclasses import dataclass
from src.enums.architecture import Architecture
from src.enums.module_type import Module_Type


@dataclass
class Section:
    name: str
    architecture: Architecture = Architecture.UNDEFINED
    module_type: Module_Type = Module_Type.UNDEFINED
    public: bool = True

    def __init__(self, section: str) -> None:
        args = map(lambda x: x.strip(), section.split('.'))

        for arg in args:
            # print(arg)

            if Architecture.has_element(arg):
                self.architecture = Architecture(arg.upper())
                continue
            if Module_Type.has_element(arg):
                self.module_type = Module_Type(arg.upper())
                continue
            if arg.upper() == "PRIVATE":
                self.public = False
                continue
            self.name = arg

        # print(self, '\n\n')

    def __eq__(self, __value) -> bool:
        if not isinstance(__value, Section):
            return False
        return self.name == __value.name and self.public == __value.public and self.architecture == __value.architecture and self.module_type == __value.module_type

    def __hash__(self):
        return hash((self.name, self.public, self.architecture, self.module_type))
