import os

# from src.utils import create_sections, ends_section, starts_section

from data_classes.File import File
from src.data_classes.section import Section

from src.to_ini.generate_ini import generate_ini
from src.util.get_possible_data import get_possible_data

from src.classes.edk2_file_handler import Edk2_File_Handler
from src.classes.dec import Dec
from src.classes.dsc import Dsc
from src.classes.inf import Inf


def parse(path: str) -> File:
    path = path.strip()
    if not os.path.exists(path=path):
        print(f'arquivo nao existe {path}')
        return File()

    handler: Edk2_File_Handler

    end_of_path = path[-3:]

    if end_of_path == 'dec':
        handler = Dec()
    elif end_of_path == 'dsc':
        handler = Dsc()
    elif end_of_path == '.inf':
        handler = Inf()

    f = open(path)
    file = f.readlines()
    f.close()

    all_sections = []

    file = File(path=path)

    # List with all dependencies
    deps: list[File] = file.deps

    # Dict to store all section data
    data = file.data

    def complete_section(pos: int) -> tuple[int, str]:
        line = ""
        while pos < len(file):
            line += handler.rm_comments(file[pos]).strip()

            if handler.ends_section(line):
                return (pos, line)
            pos += 1

        return (-1, "")

    current_sections: list[Section] = []

    for c in range(0, len(file)):
        line = handler.rm_comments(file[c]).strip()

        if len(line) == 0:
            continue

        if handler.starts_section(line):
            c, line = complete_section(c)
            current_sections = handler.create_sections(line=line, data=data)
            for section in current_sections:
                all_sections.append(section)
            continue

        #
        line = handler.handle_macros(line=line, sections=current_sections)
        #

        if len(line) == 0:
            continue

        data_sample = handler.handle_data(line=line, sections=current_sections)

        path_to_recursion = get_possible_data(data_sample)

        if path_to_recursion != None:
            deps.append(parse(path))

        for section in current_sections:
            data[section].append(data_sample)

    for dt in data:
        print('-=' * 70, '\n', dt, '\n', '-=' * 70, '\n')
        print(data[dt], '\n\n\n\n')

    # rename this variable later

    return file


if __name__ == "__main__":
    out = parse(input())

    while True:
        print(out.deps, out.path, '\n' * 3)
        if len(out.deps) == 0:
            break
        out = out.deps[0]
