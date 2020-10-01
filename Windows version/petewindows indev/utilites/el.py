import os
import sys
import argparse
import commons
import shutil


def notificar(materia):
    print(materia+" fue eliminada.")


def eliminar(materia):
    shutil.rmtree(materia, ignore_errors=True)


# Tomamos los argumentos
parser = argparse.ArgumentParser(
    description="Eliminar materias ")
parser.add_argument(
    "materias", nargs='*', help="Las materias que queremos eliminar", default=None)
parser.add_argument(
    "-o", "--open", help="Abrir la carpeta del curso una vez hallamos terminado", action="store_true")
parser.add_argument(
    "-f", "--hard", help="Eliminar las materias sin consultar", action="store_true")
args = parser.parse_args()


for materia in args.materias:

    materia = materia.upper()
    # Esto convierte el parámetro en una ruta
    materia_ruta = os.path.join(commons.directorio, materia)

    if os.path.isdir(materia_ruta):  # Si la materia existe
        if args.hard:  # Y tiene el argumento -f
            eliminar(materia_ruta)  # Se elimina
            notificar(materia)
        else:  # Sino tiene el argumento -f, se pregunta al usuario antes de proceder
            respuesta = input("Seguro que desea eliminar: \n" +
                              materia + " y todo su contenido? (s/n)\n")
            if respuesta is "s":  # Se elimina
                eliminar(materia_ruta)
                notificar(materia)
            elif respuesta is "n":
                pass
            else:
                print("Su respuesta no es válida. \nElija 's' para si o 'n' para no\n")
    else:
        print("\n"+materia+" no existe\n")

if args.open:
    os.startfile(commons.directorio)
