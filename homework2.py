# -*- coding: utf-8 -*-

hw2 = 'homework1.txt'
with open(hw2, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')
pass
# в отличие от необходимости использовать команду file.close() после работы с файлом,
# при использовании with open(# file_name...)
# открываемый файл автоматически закроется после выполнения блока кода (в данной работе это строки 5-6).
