#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que había generado.

import random

secreto = random.randint(1, 100)

for intento in range(1, 11):
    numero = int(input("Adivina el número: "))

    if numero == secreto:
        print("¡Acertaste en", intento, "intentos!")
        break
    elif numero < secreto:
        print("El número es mayor")
    else:
        print("El número es menor")

    print("Te quedan", 10 - intento, "intentos")

else:
    print("Se acabaron los intentos. El número era", secreto)