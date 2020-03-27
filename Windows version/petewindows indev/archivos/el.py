import os
import sys
import argparse
import commons
import shutil

parser = argparse.ArgumentParser(
    description="Eliminar materias ")
parser.add_argument(
    "materias", nargs='*', help="Las materias que querramos eliminar", default=None)
parser.add_argument(
    "-o", "--open", help="Abrir la carpeta del curso una vez creada", action="store_true")
parser.add_argument(
    "-f", "--hard", help="Eliminar las materias sin consultar", action="store_true")
args = parser.parse_args()


def suave_eliminar():
    for materia in args.materias:
        materia = materia.upper()
        materia_eliminar = os.path.join(commons.directorio, materia)
        if os.path.isdir(materia_eliminar):
            respuesta = input("Seguro que desea eliminar: " +
                              materia + " y todo su contenido? (s/n)     ")
            if respuesta is "s":
                shutil.rmtree(materia_eliminar, ignore_errors=True)
                print("El contenido de ", materia, " fue eliminado.")
            elif respuesta is "n":
                pass
            else:
                print("Su respuesta no es válida. \nElija 's' para si o 'n' para no")
        else:
            print("\n", materia, " no existe.\n")


def fuerte_eliminar():
    for materia in args.materias:
        materia = materia.upper()
        materia_eliminar = os.path.join(commons.directorio, materia)
    if os.path.isdir(materia_eliminar):
        shutil.rmtree(materia_eliminar, ignore_errors=True)
    else:
        print("\n", materia, " no existe.\n")


if args.hard:
    fuerte_eliminar()
else:
    suave_eliminar()

if args.open:
    os.system("explorer " + commons.directorio)
