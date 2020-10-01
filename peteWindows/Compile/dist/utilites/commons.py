import os
import json


def get_nombre():
    if not os.path.exists('pete_data.json'):
        print("\nFalta el archivo 'pete_data.json'\n")
        pass
    else:
        with open('pete_data.json', 'r') as pete_data:
            pete_info = json.load(pete_data)
            return pete_info['nombre_curso']


def get_directorio():
    directorio_local = os.path.join(os.getcwd(), curso)
    if not os.path.exists(directorio_local):
        print("\nLa carpeta del curso no existe\n")
    else:
        return directorio_local


# Nombre del curso
curso = get_nombre()
# Directorio en donde se trabajará
directorio = get_directorio()

#Ver SOLO los folders de dicho directorio
def ver_folders(directorio):
    folders = []
    for folder in os.listdir(directorio):
        if os.path.isdir(os.path.join(directorio, folder)):
            folders.append(folder)
    return folders


materias = ver_folders(directorio)
