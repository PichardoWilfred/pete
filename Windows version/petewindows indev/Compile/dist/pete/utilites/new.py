import os
import datetime
import sys
import commons
import argparse


parser = argparse.ArgumentParser(
    description="Crear las carpetas para dividir las sesiones de trabajo.")
parser.add_argument(
    "materia", help="La materia en la cual trabajaremos", default=None)
args = parser.parse_args()

# La materia que seleccionamos en la que ibamos a trabajar
materia_req = args.materia.upper()

# Fechas
mes_actual = datetime.datetime.now().strftime("%B")
dia_actual = datetime.datetime.now() .strftime("%d")


# Crear las carpetas del dia y mes actuales.
def crear_mes_y_dia(directorio, abrir):
    commons.directorio = os.path.join(commons.directorio, mes_actual)
    os.mkdir(commons.directorio)
    nuevo_dia = os.path.join(commons.directorio, dia_actual)
    os.mkdir(nuevo_dia)
    # Completamos y ejecutamos el Opener
    abrir = os.path.join(abrir, mes_actual, dia_actual)
    # Aqui completamos y ejecutamos el Opener
    print("Abriendo... \n"+abrir)
    os.startfile(abrir)


def crear_dia(directorio, abrir):
    commons.directorio = os.path.join(commons.directorio, dia_actual)
    os.mkdir(commons.directorio)
    # Aqui completamos y ejecutamos el Opener
    abrir = os.path.join(abrir, mes_actual, dia_actual)
    print("Abriendo... \n" + abrir)
    os.startfile(abrir)



# Si no hay ninguna materia
if len(commons.materias) < 1:
    print("\n No hay ninguna materia registrada. \n")
else:
    # Si la materia de parámetro existe
    if materia_req in commons.materias:
        # Hace que vayas a ese commons.directorio (el de la materia)=
        commons.directorio = os.path.join(commons.directorio, materia_req)
        # Cuáles meses se tiene registrado
        meses_registrados = commons.ver_folders(commons.directorio)
        # Le da la materia al Opener
        commons.abrir_aqui = os.path.join(commons.abrir_aqui, materia_req)
        # Si no hay ningun mes registrado
        if meses_registrados is None:
            crear_mes_y_dia(commons.directorio, commons.abrir_aqui)
        else:
            # Si el mes actual esta ahí
            if mes_actual in meses_registrados:
                # Aqui creamos el commons.directorio del mes
                commons.directorio = os.path.join(
                    commons.directorio, mes_actual)
                # Los dias que ya existen
                dias_registrados = commons.ver_folders(commons.directorio)
                # Si no hay ningun dia
                if dias_registrados is None:
                    crear_dia(commons.directorio, commons.abrir_aqui)
                else:
                    # Si el dia de hoy esta en los días registrados
                    if dia_actual in dias_registrados:
                        # Simplemente abrimos la carpeta de ese dia
                        commons.abrir_aqui = os.path.join(
                            commons.abrir_aqui, mes_actual, dia_actual)
                        os.startfile(commons.abrir_aqui)
                        print("Abriendo... \n"+commons.abrir_aqui)
                        print("Ya se ha utilizado ese comando hoy.")
                    else:
                        crear_dia(commons.directorio, commons.abrir_aqui)
            else:
                crear_mes_y_dia(commons.directorio, commons.abrir_aqui)
    else:
        print("\n Porfavor elija una de las siguientes materias \n")
        for materia in commons.materias:
            print(materia)
