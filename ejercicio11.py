#numero = int(input("Escribe un número: ")) primo = numero > 1 for divisor in range(2, int(numero ** 0.5) + 1): if numero % divisor == 0: primo = False break if primo: print("Es primo") else: print("No es primo")

numero = int(input("Escribe un número: "))
primo = numero > 1

for divisor in range(2, int(numero ** 0.5) + 1):
    if numero % divisor == 0:
        primo = False
        break

if primo:
    print("Es primo")
else:
    print("No es primo")