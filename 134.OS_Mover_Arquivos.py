import os
import shutil

caminho_original = '/Users/es19237/Downloads/3e16a10450e588818c86c0358e8a7fdb'
caminho_novo = '/Users/es19237/Downloads/serie'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f"Pasta {caminho_novo} já existe.")

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        if '.xml' in file:
            # move
            #shutil.move(old_file_path, new_file_path)
            # copia
            #shutil.copy(old_file_path, new_file_path)
            # remove
            os.remove(new_file_path)
            print(f'Arquivo {file} movido!')
