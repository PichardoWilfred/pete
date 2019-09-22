import os
import datetime
import time

opener = "Especialidades\\\\"
materia_req = os.getenv('esp_name')

creator = "Especialidades/"

os.mkdir(creator + materia_req)
opener+=materia_req
os.system("explorer.exe "+opener)
