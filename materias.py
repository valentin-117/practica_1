print("")
print("Este es un programa que imprimirá una lista de materias para luego pedir la calificación obtenida. ")#imprime la funcion del programa
print("")
print("Frías Villa Angel Valentín 3W")# Imprime mi nombre en pantalla


# Almacenar las materias en una lista
materias = ["Matematicas", "lengua", "Inglés", "Ecosistemas", "Formación", "Frameworks"]
print(materias) #se imprime la lista de materias
# Mostrar un mensaje para cada materia en pantalla
for materia in materias:
    print(f"Estoy cursando {materia}.")
    print(" ")
    mat=(float(input("¿Cuál fue la calificación que obtuviste en matematicas?: ")))
    leng=(float(input("¿Cuál fue la calificación que obtuviste en lengua?: ")))
    ing=(float(input("¿Cuál fue la calificación que obtuviste en ingles?: ")))
    eco=(float(input("¿Cuál fue la calificación que obtuviste en ecosistemas?: ")))
    form=(float(input("¿Cuál fue la calificación que obtuviste en formación?: ")))
    frame=(float(input("¿Cuál fue la calificación que obtuviste en frameworks?: ")))
    print("")
    print("has obtenido una calificación de ", mat)
    print("has obtenido una calificación de ", leng)
    print("has obtenido una calificación de ", ing) 
    print("has obtenido una calificación de ", eco) 
    print("has obtenido una calificación de ", form) 
    print("has obtenido una calificación de ", frame)

