import argparse

parser = argparse.ArgumentParser(
    description="Buscar carpetas de trabajo en especifico")
parser.add_argument(
    "materia", nargs='?', help="La materia que queremos buscar", default=None)
parser.add_argument(
    "mes", nargs='?', help="El mes que queremos buscar", default=None)
parser.add_argument(
    "dia", nargs='?', help="La dia que queremos buscar", default=None)

args = parser.parse_args()

if args.mes:
    print("el mes que seleccionaste fue: ", args.mes)
if args.dia:
    print("el dia que seleccionaste fue: ", args.dia)
if args.materia:
    print("La materia que selccionaste fue: ", args.materia)


