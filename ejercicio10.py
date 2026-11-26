#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for numero in range(1, 6):
    print("Tabla del", numero)

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

    print()