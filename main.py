# -*- coding: utf-8 -*-
import os
import sys
import shutil

# Задаем распределение типов файлов по каталогам
ORGANIZED_PATHS = {
    'Documents': ['.pdf', '.doc', '.docx', '.md', '.xlsx', '.ppt'],
    'Images': ['.jpg', 'jpeg', '.gif', 'png', '.svg', '.tga'],
    'Archives': ['.zip', '.rar', '.7z'],
    '1C': ['.epf', '.erf', '.cf', '.cfu', '.cfe', '.dt', '.DT'],
    'Softs': ['.exe','.msi'],
    'Texts': ['.txt'],
    'Temps': ['.crdownload'],
}
def organize_downloads(downloads_path):
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)

        # Обрабатываем только файлы
        if not os.path.isfile(file_path):
            continue

        # Определяем по типу файла подкаталог размещения файла
        file_type = None
        for folder, extensions in ORGANIZED_PATHS.items():
            for extension in extensions:
                if filename.upper().endswith(extension.upper()):
                    file_type = folder
                    break
            if file_type:
                break

        # Выполняем перемещение файла если подкаталог размещения определен
        if file_type:
            dest_folder = os.path.join(downloads_path, file_type)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, filename))
        else:
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for folder in sys.argv:
            if os.path.isdir(folder):
                print("Запуск перемещения файлов в каталоге {}".format(folder))
                organize_downloads(folder)
                print("Перемещение файлов закончено.")
    else:
        print("Не задан список каталогов для обработки файлов")