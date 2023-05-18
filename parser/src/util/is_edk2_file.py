def is_edk2_file(data: str) -> bool:
    return (data.strip()[-3:] in ['inf', 'dec', 'dsc'])
