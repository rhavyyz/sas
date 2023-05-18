from dataclasses import dataclass

from src.data_classes.section import Section


@dataclass
class File:
    path: str = ''
    deps: list = []
    data: dict[Section, list] = {}
