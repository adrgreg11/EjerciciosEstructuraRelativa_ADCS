#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario

inicio = int(input("Primer número: "))
fin = int(input("Segundo número: "))

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print(numero)