#Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

numero = int(input("Escribe un número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)