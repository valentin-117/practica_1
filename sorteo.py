print("")
print("Este es un programa que realizará un sorteo de numeros e imprimirá el ganador. ")#imprime la funcion del programa
print("")
print("Frías Villa Angel Valentín 3W")# Imprime mi nombre en pantalla
print("")


numeros=[] # Almacena los numeros ganadores

#Pide al usuario ingresar los numeros de la loteria.(en caso de ser 6.)
numeros.append(int(input("Número 1.- ")))
numeros.append(int(input("Número 2.- ")))
numeros.append(int(input("Número 3.- ")))
numeros.append(int(input("Número 4.- ")))
numeros.append(int(input("Número 5.- ")))
numeros.append(int(input("Número 6.- ")))
#ordena la lista en forma ascendente
numeros.sort()
#muestra los numeros ganadores
print("Números ganadores ordenados:", numeros)