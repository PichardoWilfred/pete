import os
import sys
import argparse
import commons

parser = argparse.ArgumentParser(
    description="Añadir mas materias ")
parser.add_argument(
    "materias", nargs='*', help="Las materias que querramos añadir", default=None)
parser.add_argument(
    "-o", "--open", help="Abrir la carpeta del curso una vez creada", action="store_true")
args = parser.parse_args()

for materia in args.materias:
    materia = materia.upper()
    nueva_materia = os.path.join(commons.directorio, materia)
    if not os.path.isdir(nueva_materia):
        os.mkdir(nueva_materia)
    else:
        print("\n", materia, " ya existe.\n")
if args.open:
    os.system("explorer " + commons.directorio)
