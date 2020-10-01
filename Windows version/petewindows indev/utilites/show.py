import commons

if len(commons.materias) < 1:
    print("\nAun no se ha registrado ninguna materia.\n")
else:
    print("""
    +======================+
    | Materias disponibles |
    +======================+""")
    for materia in commons.materias:
        print("  -", materia)
