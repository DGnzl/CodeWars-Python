def calculator(txt: str):
    values = txt.split()
    return '.' * eval(f'{len(values[0])}{values[1]}{len(values[2])}')