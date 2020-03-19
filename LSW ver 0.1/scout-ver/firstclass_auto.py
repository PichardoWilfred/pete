#Modulos a utilizar
import os
import datetime
import time

#La materia que seleccionamos en la que ibamos a trabajar
tarea_req = os.getenv('tarea')
#Las materias que ya hay en existencia y en las que vamosa trabajar
tareas_registered = os.listdir("1era Clase/")

#Opener
opener = "1era Clase\\\\"


fecha_actual = datetime.datetime.now()    

#Se revisa si la tarea que se solicita ya se ha registrado Anteriormente
if tarea_req in tareas_registered: #Si fue asi se crea el opener y simplemente se ejecuta
    opener += tarea_req
    command = "explorer.exe "+ opener
    print(opener)
    os.system(command)

else: #Si no se tiene registro de esa Tarea
    print("La tarea solicitada, no existe:")
    command = "explorer.exe "+ opener
    os.system(command)
