import os
import sys
import argparse
import commons

# Tomamos los argumentos
parser = argparse.ArgumentParser(
    description="Busca las carpetas de trabajo en especifico. ")
parser.add_argument(
    "materia", nargs='?', help="La materia que queremos buscar", default=None)
parser.add_argument(
    "mes", nargs='?', help="El mes que queremos buscar", default=None)
parser.add_argument(
    "dia", nargs='?', help="La dia que queremos buscar", default=None)

args = parser.parse_args()


def print_err():
    print("\n La ruta especificada no existe. \n")


def abrir(directorio):
    if os.path.isdir(directorio):
        print("\nAbriendo...")
        os.startfile(directorio)
    else:
        print_err()


args.materia = args.materia.upper()  # Pasa el parámetro de la materia a Mayus
if args.dia:
    ruta = os.path.join(
        commons.curso, args.materia, args.mes, args.dia)
    abrir(ruta)

elif args.mes:
    ruta = os.path.join(
        commons.curso, args.materia, args.mes)
    abrir(ruta)

elif args.materia:
    ruta = os.path.join(
        commons.curso, args.materia)
    abrir(ruta)
