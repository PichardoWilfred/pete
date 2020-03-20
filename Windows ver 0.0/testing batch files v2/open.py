import os
import datetime
import time
import sys

curso = "Curso"
#Nombres de Materias/Dir
#La materia que seleccionamos en la que ibamos a trabajar
materia_req = sys.argv[1] or None
mes_req = sys.argv[2] or None
dia_req = sys.argv[3] or None

# if materia_req and not mes_req and mes_req and not dia_req:
#     abrir_aqui = curso + "\\" + materia_req 
#     os.system("explorer "+ abrir_aqui)
# elif materia_req and mes_req and not dia_req:
#     abrir_aqui = curso + "\\" + materia_req + "\\" + mes_req
#     os.system("explorer "+ abrir_aqui)
# elif materia_req and mes_req and dia_req:
#     abrir_aqui = curso + "\\" + materia_req + "\\" + mes_req + "\\" + dia_req
# else:
#     print("No se reconocen los parametros ingresados 'help' para mas información")



print(materia_req)


# #Las materias que ya hay en existencia y en las que vamosa trabajar

# materias = os.listdir("6to/")
# #El directorio donde estamos trabajando
# sub_dir = os.getcwd() + "/6to"

# #Opener
# abrir_aqui = "6to\\\\"

# if materia_req in materias:
#     abrir_aqui += materia_req
#     os.system("explorer"+ abrir_aqui )
