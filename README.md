# practica_1
#Mayor y menor.

print("")
print("Este es un programa que imprimirá el numero mayor y menor de una lista. ")# imprime en pantalla la descripcion del programa  
print("")
print("Frías Villa Angel Valentín 3W")# imprime mi nombre en pantalla

precios=[43, 57, 92, 20, 37, 5, 9] #Almacena los precios en una variable
Se declara el numero mayor y el menor
mayor=max(precios)
menor=min(precios)
 Imprime los numeros mayor y menor en pantalla
print("El numero más grande en la lista es: ",mayor)
print("")
print("el numero menor en la lista es: ", menor)
![image](https://github.com/user-attachments/assets/06388ca3-c1c6-4b66-88f4-8b41c7bdcc52)



#Materias.


print("")
print("Este es un programa que imprimirá una lista de materias para luego pedir la calificación obtenida. ")#imprime la funcion del programa
print("")
print("Frías Villa Angel Valentín 3W")# Imprime mi nombre en pantalla


 Almacenar las materias en una lista
materias = ["Matematicas", "lengua", "Inglés", "Ecosistemas", "Formación", "Frameworks"]
print(materias) #se imprime la lista de materias
Mostrar un mensaje para cada materia en pantalla
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

![image](https://github.com/user-attachments/assets/92cf51e2-8db7-43ca-bcea-64742f33dcab)
![image](https://github.com/user-attachments/assets/ef8e8d45-db59-4173-95c8-1191301d829b)
#lista de materias


print("")
print("Este programa almacenará una lista de todas las materias que llevo. ")# imprime en pantalla la descripcion del programa  
print("")
print("Frías Villa Angel Valentín 3W")# imprime mi nombre en pantalla
 Almacena las materias en distintas variables.
a=("1.- Humanidades.")
b=("2.- Cálculo.")
c=("3.- Ecositemas. ")
d=("4.- Frameworks. ")
e=("5.- lengua.")
f=("6.- Formación. ")
Imprime las materias en pantalla
print(a)
print(" ")
print(b)
print(" ")
print(c)
print(" ")
print(d)
print(" ")
print(e)
print(" ")
print(f)
![image](https://github.com/user-attachments/assets/9d10d7a6-b41f-4ead-a93f-fdb7dfeb23e5)
sorteo.



print("")
print("Este es un programa que realizará un sorteo de numeros e imprimirá el ganador. ")#imprime la funcion del programa
print("")
print("Frías Villa Angel Valentín 3W")# Imprime mi nombre en pantalla

# Inicializar una lista vacía para almacenar los números triunfadores
numeros_ganadores = []

# Bucle infinito para permitir al usuario ingresar múltiples números
while True:
    # Pedir al usuario que ingrese un número o 'fin' para terminar
    entrada = input("Ingresa un número triunfador (o 'fin' para terminar): ")
    
  # Verificar si el usuario desea terminar la entrada
  if entrada.lower() == 'fin':
        break  # Salir del bucle si se ingresa 'fin'
    
   try:
        # Intentar convertir la entrada a un número entero
        numero = int(entrada)
        # Agregar el número a la lista de números triunfadores
        numeros_ganadores.append(numero)
  except ValueError:
        # Si la conversión falla, informar al usuario que ingrese un número válido
        print("Por favor, ingresa un número válido.")

# Ordenar la lista de números triunfadores de menor a mayor
numeros_ganadores.sort()

# Mostrar los números triunfadores ordenados
print("Números triunfadores de la lotería en orden de menor a mayor:")
print(numeros_ganadores)
![image](https://github.com/user-attachments/assets/ec93e879-b3e7-43de-a6e7-e1610dc71a2f)




