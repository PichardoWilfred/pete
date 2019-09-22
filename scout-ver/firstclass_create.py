import os
import datetime
import time

opener = "1era Clase\\\\"
materia_req = os.getenv('tarea')

creator = "1era Clase/"

os.mkdir(creator + materia_req)
opener+=materia_req
os.system("explorer.exe "+opener)