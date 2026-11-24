#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

suma = 0
cantidad = 0

numero = int(input("Escribe un número (0 para terminar): "))

while numero != 0:
    suma += numero
    cantidad += 1
    numero = int(input("Escribe otro número (0 para terminar): "))

print("Suma:", suma)

if cantidad > 0:
    print("Media:", suma / cantidad)
else:
    print("No se introdujeron números.")