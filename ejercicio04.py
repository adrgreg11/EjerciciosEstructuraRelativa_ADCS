#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

cantidad = int(input("¿Cuántos números vas a introducir? "))

mayores = 0
menores = 0
iguales = 0

for i in range(cantidad):
    numero = float(input("Escribe un número: "))

    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

print("Mayores que 0:", mayores)
print("Menores que 0:", menores)
print("Iguales a 0:", iguales)

