import shutil
import os
import argparse
import json


archivos = []

parser = argparse.ArgumentParser(
    description="Crea una instancia de pete en el directorio seleccionado")
parser.add_argument(
    "nombre_curso", help="El nombre de nuestro curso", default=None)
parser.add_argument(
    "direccion", nargs='+', help="La dirección donde queremos crear la instancia", default=None)

args = parser.parse_args()

args.direccion = ' '.join(args.direccion)


if os.path.isdir(args.direccion):
    # os.chdir(args.direccion)  # cambiamos el direcorio

    # verificamos si ya hay un archivo de pete_data
    if os.path.exists(os.path.join(args.direccion, 'pete_data.json')):
        print("\n'pete_data.json' ya existe en '"+args.direccion + "'\n")
    else:  # creamos el pete_data
        data = {
            "nombre_curso": args.nombre_curso,
            "desarrollado_por": "TeamPete",
            "fecha": "22/03/2020",
            "version": "pete-windows v0.1"
        }
        # Serializing json
        data = json.dumps(data, indent=4)

        with open(os.path.join(args.direccion, "pete_data.json"), "w") as pete_data:
            pete_data.write(data)
            # creamos la carpeta que usaremos
            os.mkdir(os.path.join(args.direccion, args.nombre_curso))

        # Recolectamos todos los archivos necesarios
        for archivo in os.listdir(r'.\archivos'):
            if archivo.endswith(".bat") or archivo.endswith(".py"):
                archivos.append(archivo)
                shutil.copy(os.path.join(
                    r'.\archivos', archivo), args.direccion)

        os.chdir(args.direccion)
        archivos.append('pete_data.json')
        for archivo in archivos:
            p = os.popen('attrib +h ' + archivo)

else:
    print("\nLa ruta especificada no existe\n")
