from src.data_classes.define_property import Define_Property
from src.data_classes.library_instance import Library_Instance
from src.data_classes.section import Section
from abc import ABC, abstractclassmethod


class Edk2_File_Handler(ABC):

    __operation_handler: dict = {
        'LibraryClasses': lambda line: Library_Instance(line),
        'Defines': lambda line: Define_Property(line)
    }

    # Function to remove comments from file lines
    def rm_comments(self, line: str) -> str:
        pos = line.find('#')
        if pos == -1:
            return line
        return line[:pos]

    # At the beginning this function is just ignoring all macros it sees
    def handle_macros(self, line: str, sections: list[Section] = []) -> str:

        if line[0] == '!' or 'DEFINE' == line[:6] or line.find('$') != -1:
            return ''

        return line

    def handle_data(self, line: str, sections: list[Section] = []):

        # This section of code pass the responsibility to convert data to
        # a function stored inside __operation_handler so we just need to
        # create these functions inside each file handler
        for section in sections:
            if section.name in self.__operation_handler:
                return self.__operation_handler[section.name](line)
        ###########################################################

        ########### Generic way to handle data ###########
        data = [dt.strip() for dt in line.split('|')]

        if len(data) == 1:
            data = [dt.strip() for dt in line.split('=')]

        new_data = []

        for dt in data:
            if dt.strip() == '':
                continue
            new_data.append(dt)

        if len(new_data) == 1:
            return line

        return new_data
        ##################################################

    @classmethod
    def starts_section(cls, line: str) -> bool:
        if line.find('[') >= 0:
            return True
        return False

    @classmethod
    def ends_section(cls, line: str) -> bool:
        if line.find(']') >= 0:
            return True
        return False

    @classmethod
    def create_sections(cls, line: str, data: dict[Section, any]) -> list[Section]:
        line = line[line.find('[') + 1: line.find(']')]
        sections_str = line.split(',')

        # map(lambda x: Section(x.strip()), sections_str)
        sections = [Section(x.strip()) for x in sections_str]

        for section in sections:
            if section in data:
                continue
            data[section] = []

        return sections
