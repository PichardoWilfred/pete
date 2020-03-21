import os
import sys
import argparse
import commons

curso = "Curso"

parser = argparse.ArgumentParser(
    description="Buscar carpetas de trabajo en especifico")
parser.add_argument(
    "materia", nargs='?', help="La materia que queremos buscar", default=None)
parser.add_argument(
    "mes", nargs='?', help="El mes que queremos buscar", default=None)
parser.add_argument(
    "dia", nargs='?', help="La dia que queremos buscar", default=None)

args = parser.parse_args()


def print_err():
    print("\n La ruta especificada no existe. \n")


if args.dia:
    commons.abrir_aqui = os.path.join(
        commons.abrir_aqui, args.materia, args.mes, args.dia)
    if os.path.isdir(commons.abrir_aqui):
        print("\n"+commons.abrir_aqui)
        os.system("explorer " + commons.abrir_aqui)
    else:
        print_err()

elif args.mes:
    commons.abrir_aqui = os.path.join(
        commons.abrir_aqui, args.materia, args.mes)
    if os.path.isdir(commons.abrir_aqui):
        print("\n"+commons.abrir_aqui)
        os.system("explorer " + commons.abrir_aqui)
    else:
        print_err()
elif args.materia:
    commons.abrir_aqui = os.path.join(
        commons.abrir_aqui, args.materia)
    if os.path.isdir(commons.abrir_aqui):
        print("\n"+commons.abrir_aqui)
        os.system("explorer " + commons.abrir_aqui)
    else:
        print_err()
