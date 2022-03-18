import os
from PIL import Image


def main(main_images_folder, new_width):
    if not os.path.isdir(main_images_folder):
        print('Diretório não encontrado')
        return
    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            if file.endswith('.png'):
                file_full_path = os.path.join(root, file)
                tag_name = '_converted'
                if tag_name in file_full_path:
                    os.remove(file_full_path)
                    continue
                file_name, extension = os.path.splitext(file)
                new_file = file_name + tag_name + extension
                new_file_full_path = os.path.join(root, new_file)
                img_pillow = Image.open(file_full_path)
                # Pegar informações da imagem
                exif = img_pillow._getexif()
                # print(exif)
                width, height = img_pillow.size
                new_height = int(height * new_width / width)
                new_image = img_pillow.resize(
                    (new_width, new_height), Image.LANCZOS)
                new_image.save(new_file_full_path, optimize=True,
                               quality=70, exif=img_pillow.info['exif'])
                print(f'{file} converted to {new_file}')

                img_pillow.close()


if __name__ == '__main__':
    main_images_folder = '/Users/es19237/Desktop/Python/Pycharm/CursoPython3/Seção5_Modulos-Pyhton/Imagens'
    main(main_images_folder, 600)
