import commons
materias = commons.ver_folders(commons.directorio)
print("""
 +======================+
 | Materias disponibles |
 +======================+""")
for materia in materias:
    print("  -",materia)