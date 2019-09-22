import os
import test
import datetime
import time
    #Nombres de Materias/Dir

#La materia que seleccionamos en la que ibamos a trabajar
materia_req = os.getenv('subject')
#Las materias que ya hay en existencia y en las que vamosa trabajar
materias = os.listdir("6to/")
#El directorio donde estamos trabajando
sub_dir = os.getcwd() + "/6to"

#Opener
opener = "6to\\\\"

    #Fechas
fecha_actual = datetime.datetime.now()    
month_dir = fecha_actual.strftime("%B")
day_name = fecha_actual.strftime("%d")

#Si la materia de parámetro existe
if materia_req in materias:
    #Hace que vayas a ese directorio (el de la materia)
    mainsub_dir = sub_dir +"/"+ materia_req
    #Cuales meses se tiene registrado
    months_of = os.listdir(mainsub_dir)
    #Le da la materia al Opener
    opener += materia_req+ ""

    #Si el mes actual esta ahí
    if month_dir in months_of:
        #Aqui creamos el directorio del mes
        mainsub_dir+= "/"+month_dir
        #Lista de Dias que ya han sido usados
        reg_days = os.listdir(mainsub_dir)

        if day_name in reg_days:
            print("Este ya haz activado ese comando hoy.")
        else:    
            #Aqui creamos el día
            mainsub_dir = os.path.join(mainsub_dir, day_name)
            os.mkdir(mainsub_dir)
            #Aqui completamos y ejecutamos el Opener
            opener += "\\\\" + month_dir + "\\\\" + day_name
            command = r"explorer.exe "+ opener
            os.system(command)
            print(opener)

    #Si no hay mes
    else:
        mainsub_dir+= "/"+month_dir
        os.mkdir(mainsub_dir)
        nday_of_nmonth = os.path.join(mainsub_dir,day_name)
        os.mkdir(nday_of_nmonth)
        #Completamos y ejecutamos el Opener
        opener += "\\\\" + month_dir + "\\\\" + day_name
        command = r"explorer.exe "+ opener
        #Opener
        os.system(command)
        print(command)
        
else:
    print("Esta materia no existe. \nSeleccione alguna de las siguientes:\n")
    for materia in materias:
        print("-"+materia)