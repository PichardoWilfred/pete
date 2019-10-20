import os
print("Creando carpetas de Materias en cuestión...")
materias = ['ESP', 
'MATH', 
'SOC', 
'FISICA',
'ARTE',
'FIHR',
'EDUF',
'ENG',
'ORIFOR',
'IMPL-WEB',
'IMPL-APP'
]

for materia in materias:
    os.mkdir(materia)
