import os

# Nombre del curso
curso = "Curso"
# Ruta que abre
abrir_aqui = curso + "\\"

# Directorio en donde se trabajará
directorio = os.getcwd() + "\\" + curso + "\\"


def ver_folders(directorio):
    folders = []
    for folder in os.listdir(directorio):
        if os.path.isdir(directorio+"\\"+folder):
            folders.append(folder)
    return folders

    
materias = ver_folders(directorio)
