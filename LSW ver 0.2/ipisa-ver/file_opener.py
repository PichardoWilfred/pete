import os
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

if materia_req in materias:
    opener+= materia_req
    os.system("explorer.exe "+ opener)