import os
import datetime
import sys

# Nombre del curso
curso = "Curso"

# La materia que seleccionamos en la que ibamos a trabajar
materia_req = sys.argv[1]

# El directorio donde estamos trabajando
sub_dir = os.getcwd() + "\\" + curso + "\\"

# Las materias que ya existen y en las que vamos a trabajar
materias = []
for materia in os.listdir(curso):
    if os.path.isdir(sub_dir + materia):
        materias.append(materia)
# Los dias que ya existen
dias_registrados = []
# Los meses que ya existen
meses_registrados = []

# El string que se encargara de abrir la ruta u na vez creada
abrir_aqui = curso + "\\"

# Fechas
mes_actual = datetime.datetime.now().strftime("%B")
dia_actual = datetime.datetime.now() .strftime("%d")

# Si la materia de parámetro existe
if materia_req in materias:
    # Hace que vayas a ese directorio (el de la materia)
    sub_dir += materia_req
    # Cuales meses se tiene registrado
    #meses_registrados = os.listdir(sub_dir)
    for mes in os.listdir(sub_dir):
        if os.path.isdir(sub_dir+"\\"+mes_actual):
            meses_registrados.append(mes)
    # Le da la materia al Opener
    abrir_aqui += materia_req
    # Si el mes actual esta ahí
    if mes_actual in meses_registrados:
        # Aqui creamos el directorio del mes
        sub_dir += "\\" + mes_actual
        # Lista de Dias que ya han sido usados
        for dia in os.listdir(sub_dir):
            if os.path.isdir(sub_dir+"\\"+dia):
                dias_registrados.append(dia)

    # Si el dia de hoy esta en los días registrados
        if dia_actual in dias_registrados:
            # Simplemente abrimos la carpeta de ese dia
            abrir_aqui += "\\" + mes_actual + "\\"+dia_actual
            os.system("explorer " + abrir_aqui)
            print("Abriendo... \n"+abrir_aqui)
            print("Ya se ha utilizado ese comando hoy.")
        else:
            # Si el dia de hoy  NO  está en los días registrados
            sub_dir = os.path.join(sub_dir, dia_actual)
            os.mkdir(sub_dir)
            # Aqui completamos y ejecutamos el Opener
            abrir_aqui += "\\" + mes_actual + "\\"+dia_actual
            print("Abriendo... \n"+abrir_aqui)
            os.system("explorer " + abrir_aqui)

    # Si el mes aun no ha sido registrado
    else:
        sub_dir += "\\"+mes_actual
        os.mkdir(sub_dir)
        nuevo_dia = os.path.join(sub_dir, dia_actual)
        os.mkdir(nuevo_dia)
        # Completamos y ejecutamos el Opener
        abrir_aqui += "\\" + mes_actual + "\\" + dia_actual
        # Aqui completamos y ejecutamos el Opener
        os.system("explorer " + abrir_aqui)
        print(abrir_aqui)

else:
    print("Porfavor elija una materia existente \n")
    for materia in materias:
        print(materia)
