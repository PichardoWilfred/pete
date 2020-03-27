import commons
import json
import os
import argparse

def cambiar_nombre(nombre):
    with open('pete_data.json', 'r') as pete_data:
        pete_info = json.load(pete_data)  # cargar el JSON en un objeto
        nuevo_nombre = os.path.join(
            os.getcwd(), nombre)  # Renombrar la carpeta
        os.rename(commons.directorio, nuevo_nombre)  # ^^
        pete_info['nombre_curso'] = nombre  # Actualizar el archivo JSON
        print("El nuevo nombre del curso es", pete_info['nombre_curso'])
    with open("pete_data.json", "w", encoding="utf-8") as pete_data:
        json.dump(pete_info, pete_data, indent=4)
    

parser = argparse.ArgumentParser(
    description="Renombrar la carpeta del curso")
parser.add_argument(
    "nuevo_nombre", help="nuevo nombre de nuestra carpeta", default=None)
args = parser.parse_args()


cambiar_nombre(args.nuevo_nombre)

