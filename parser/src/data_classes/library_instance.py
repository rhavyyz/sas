from dataclasses import dataclass


@dataclass
class Library_Instance:
    name: str
    path: str or None = None
    implementation: bool = False

    def __init__(self, line: str) -> None:
        line = line.strip()
        args = line.split('|')
        self.name = args[0]

        if len(args) == 2:
            self.path = args[1]
            end = self.path[-2:]
            if end == '.h':
                self.implementation = True
