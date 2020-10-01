
import shutil
import os
import argparse
import json

print("\nBienvenido a C:\Pete> \nPara crear una nueva instancia de pete, Complete los siguientes campos:\n")
nombre_curso = input(" Nombre del curso: ")
direccion = input(
    r" Ruta de la nueva instancia (Ejemplo, 'C:\Users\gabo_\Desktop'): ")
if os.path.isdir(direccion):
    # verificamos si ya hay un archivo de pete_data
    if os.path.exists(os.path.join(direccion, 'pete_data.json')):
        print("\n'pete_data.json' ya existe en '"+direccion + "'\n")
    else:
        data = {  # creamos el pete_data
            "nombre_curso": nombre_curso,
            "desarrollado_por": "B.B",
            "fecha": "29/03/2020",
            "version": "pete-windows v0.1"
        }
        # Serializing json
        data = json.dumps(data, indent=4)
        with open(os.path.join(direccion, "pete_data.json"), "w") as pete_data:
            pete_data.write(data)
            # creamos la carpeta que usaremos
            os.mkdir(os.path.join(direccion, nombre_curso))
        archivos = []  # Recolectamos todos los archivos necesarios
        for archivo in os.listdir(r'.\utilites'):
            if archivo.endswith(".bat") or archivo.endswith(".py"):
                archivos.append(archivo)
                shutil.copy(os.path.join(
                    r'.\utilites', archivo), direccion)

        os.chdir(direccion)
        archivos.append('pete_data.json')
        for archivo in archivos:
            p = os.popen('attrib +h ' + archivo)
        os.startfile(direccion)
else:
    print("\nRuta inexistente\n")
