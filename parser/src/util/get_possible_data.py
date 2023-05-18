from src.util.is_edk2_file import is_edk2_file
from src.data_classes.library_instance import Library_Instance


def get_possible_data(data_sample) -> str:

    if data_sample is str and is_edk2_file(data_sample):
        return data_sample

    if data_sample is Library_Instance and data_sample.path is str and not data_sample.implementation:
        return data_sample.path

    if data_sample is list:
        for data in data_sample:
            if is_edk2_file(data):
                return data

    return None
