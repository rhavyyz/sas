from dataclasses import dataclass


@dataclass
class Define_Property:
    name: str
    value: str

    def __init__(self, line: str) -> None:
        args = line.split('=')
        self.name = args[0].strip()
        self.value = args[1].strip()
