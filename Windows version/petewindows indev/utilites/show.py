import commons
materias = commons.ver_folders(commons.directorio)
if len(materias) < 1:
    print("\nAun no se ha registrado ninguna materia.\n")
else:
    print("""
    +======================+
    | Materias disponibles |
    +======================+""")
    for materia in materias:
        print("  -",materia)
