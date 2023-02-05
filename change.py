from view import *

def change_data():
    example = get_value()
    example = example.replace(' ', '').replace('+',' + ').\
        replace('-',' - ').replace('*',' * ').replace('/',' / ')
    if example.startswith(' - '):
        example = '-' + example[3:]
    example = example.split()
    return example