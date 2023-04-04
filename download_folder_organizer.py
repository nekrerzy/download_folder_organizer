import os
import shutil
import time
import subprocess

# Definir los tipos de archivo y su ubicación de destino
file_types = {
    "instaladores_deb": [".deb"],
    "instaladores_rpm": [".rpm"],
    "archivos_iso": [".iso"],
    "archivos_ejecutables": [".sh"],
    "documentos": [".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx"],
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "audio": [".mp3", ".wav", ".flac"],
    "video": [".mp4", ".webm", ".mkv", ".avi"],
    "comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "app_images": ["AppImage"]
    # Agrega más tipos aquí si es necesario
}

# Cambiar la ruta según la ubicación de la carpeta Download en tu computadora
download_folder = "/home/backslash/Downloads"


# Intervalo de tiempo para revisar la carpeta (en segundos)
time_interval = 60


def create_folders(download_folder, file_types):
    """
    Esta función crea las carpetas de destino para los diferentes tipos de archivos en la carpeta Download.

    :param download_folder: La ruta de la carpeta Download.
    :param file_types: Un diccionario con los tipos de archivo y sus extensiones.
    """
    for folder in file_types.keys():
        folder_path = os.path.join(download_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


def move_files_to_folders(download_folder, file_types):
    """
    Esta función clasifica los archivos en la carpeta Download y los mueve a sus respectivas carpetas de destino,
    según las extensiones definidas en el diccionario file_types.

    :param download_folder: La ruta de la carpeta Download.
    :param file_types: Un diccionario con los tipos de archivo y sus extensiones.
    """
    for filename in os.listdir(download_folder):
        file_src = os.path.join(download_folder, filename)

        for folder, extensions in file_types.items():
            for extension in extensions:
                if filename.endswith(extension):
                    folder_path = os.path.join(download_folder, folder)
                    file_dst = os.path.join(folder_path, filename)

                    # Evitar mover la carpeta a sí misma o a otras carpetas de destino
                    if not os.path.isdir(file_src):
                        shutil.move(file_src, file_dst)
                    break


if __name__ == '__main__':
    create_folders(download_folder, file_types)
    
    # Monitorear la carpeta Download indefinidamente
    while True:
        move_files_to_folders(download_folder, file_types)
        time.sleep(time_interval)