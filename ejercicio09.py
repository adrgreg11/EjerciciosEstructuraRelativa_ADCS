#Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base = float(input("Base: "))
exponente = int(input("Exponente positivo: "))

resultado = 1

for i in range(exponente):
    resultado = resultado * base

print("Resultado:", resultado)