# -*- coding: utf-8 -*-
import os

import time

main_directory = 'X:\\PP\\pythonProject1\\module7'
for directory, directory_names, filenames in os.walk(main_directory):
    for file in filenames:
        full_path_file = os.path.join(directory, file)
        file_time = os.path.getmtime(full_path_file)
        file_time_normalized = time.strftime('%d.%m.%Y %H:%M', time.gmtime(file_time))
        file_size = os.path.getsize(full_path_file)
        dir_name = directory_names
        print(f'Обнаружен файл: {file}, Путь: {full_path_file}, Размер: {file_size} байт,'
              f'Время изменения: {file_time_normalized}, Родительская директория: {os.path.dirname(directory)}')
