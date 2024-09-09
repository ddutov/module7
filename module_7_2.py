# -*- coding: utf-8 -*-

from pprint import pprint

my_file = 'info.txt'
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(len(strings)):
        key = (i + 1, file.tell())
        file.write(strings[i] + '\n')
        strings_positions[key] = strings[i]
    file.close()
    return strings_positions


result = custom_write(my_file, info)
for elem in result.items():
    print(elem)
