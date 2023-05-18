from src.data_classes.section import Section
from src.data_classes.define_property import Define_Property


def generate_ini(data: dict[Section, list[any]]):

    defines = Section('Defines')

    import configparser
    config = configparser.ConfigParser()

    config['uSWID'] = {}

    uswid = config['uSWID']

    conversion = {
        'PLATFORM_GUID': 'tag-id',
        'PLATFORM_NAME': 'software-name',
        'PLATFORM_VERSION': 'software-version',
        'PLATFORM_VERSION': 'software-version',
    }

    for def_prop in data[defines]:

        # print(def_prop)
        if def_prop.name in conversion:
            uswid[conversion[def_prop.name]] = def_prop.value
            continue
        uswid[def_prop.name] = def_prop.value

    uswid['version-scheme'] = 'multipartnumeric'

    with open('example.ini', 'w') as configfile:
        config.write(configfile)
