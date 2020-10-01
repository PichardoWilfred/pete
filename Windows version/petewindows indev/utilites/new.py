import os
import datetime
import commons
import argparse


# Crear las carpetas del dia y mes actuales.
def crear_mes_y_dia(directorio):
    commons.directorio = os.path.join(commons.directorio, mes_actual)
    os.mkdir(commons.directorio)
    nuevo_dia = os.path.join(commons.directorio, dia_actual)
    os.mkdir(nuevo_dia)
    print("Abriendo... \n")  # Aqui abrimos
    os.startfile(commons.directorio)


# Crear la carpeta del dia actual.
def crear_dia(directorio):
    commons.directorio = os.path.join(commons.directorio, dia_actual)
    os.mkdir(commons.directorio)
    print("Abriendo... \n")
    os.startfile(commons.directorio)


# Unimos el directorio y lo abrimos
def solo_abrir(directorio):
    commons.directorio = os.path.join(
        directorio, dia_actual)
    print("Ya se ha utilizado ese comando hoy.")
    print("Abriendo... \n")
    os.startfile(commons.directorio)


# Tomamos los argumentos
parser = argparse.ArgumentParser(
    description="Crear las carpetas para dividir las sesiones de trabajo.")
parser.add_argument(
    "materia", help="La materia en la cual trabajaremos", default=None)
args = parser.parse_args()

# La materia que seleccionamos en la que ibamos a trabajar
materia = args.materia.upper()

# Fechas
mes_actual = datetime.datetime.now().strftime("%B")
dia_actual = datetime.datetime.now() .strftime("%d")

if len(commons.materias) < 1:  # Si no hay ninguna materia
    print("\n No hay ninguna materia registrada. \n")
else:
    if materia in commons.materias:  # Si la materia de parámetro existe
        # Hace que vayas a ese commons.directorio (el de la materia)
        commons.directorio = os.path.join(commons.directorio, materia)
        meses_registrados = commons.ver_folders(
            commons.directorio)  # Cuáles meses se tiene registrado
        if meses_registrados is None:  # Si no hay ningun mes registrado
            crear_mes_y_dia(commons.directorio)
        else:

            if mes_actual in meses_registrados:  # Si el mes actual esta ahí
                commons.directorio = os.path.join(  # Aqui creamos el commons.directorio del mes
                    commons.directorio, mes_actual)
                dias_registrados = commons.ver_folders(
                    commons.directorio)  # Los dias que ya existen
                if dias_registrados is None:  # Si no hay ningun dia
                    crear_dia(commons.directorio)
                else:

                    if dia_actual in dias_registrados:  # Si el dia de hoy esta en los días registrados
                        solo_abrir(commons.directorio)  # Solamente lo abrimos
                    else:
                        crear_dia(commons.directorio)  # Si no, creamos el dia
            else:  # Si no, creamos el mes y el dia
                crear_mes_y_dia(commons.directorio)
    else:  # Si no, solo listamos las materias
        print("\n Porfavor elija una de las siguientes materias \n")
        for materia in commons.materias:
            print(materia)
