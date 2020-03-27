import json
import os
import argparse

parser = argparse.ArgumentParser(
    description="Crear la carpeta del curso y el pete_data.json")
parser.add_argument(
    "nombre_curso",  help="El nombre del curso que crearemos", default=None)
args = parser.parse_args()

data = {
    "nombre_curso": args.nombre_curso,
    "desarrollado_por": "TeamPete",
    "fecha_lanzamiento": "22/03/2020",
    "version": "pete-windows v0.1"
}

# Serializing json
data = json.dumps(data, indent=4)

if os.path.exists('pete_data.json'):
    print("\n'pete_data.json' ya existe\n")
else:
    with open(os.path.join(os.getcwd(), "pete_data.json"), "w") as pete_data:
        pete_data.write(data)
        os.mkdir(args.nombre_curso)
