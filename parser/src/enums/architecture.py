from enum import Enum


class Architecture(Enum):
    COMMON = 'COMMON'
    IA32 = 'IA32'
    X64 = 'X64'
    EBC = 'EBC'
    UNDEFINED = 'UNDEFINED'

    @classmethod
    def has_element(cls, arg: str) -> bool:
        return arg.upper() in ['UNDEFINED', 'COMMON', 'IA32', 'X64', 'EBC']
