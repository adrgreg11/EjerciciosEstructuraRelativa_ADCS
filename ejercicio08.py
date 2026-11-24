#Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. A continuación, se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:  La suma de los números que están dentro del intervalo (intervalo abierto).  Cuantos números están fuera del intervalo.  He informa si hemos introducido algún número igual a los límites del intervalo.

inferior = float(input("Límite inferior: "))
superior = float(input("Límite superior: "))

while inferior > superior:
    print("El límite inferior debe ser menor o igual al superior.")
    inferior = float(input("Límite inferior: "))
    superior = float(input("Límite superior: "))

suma = 0
fuera = 0
igual_limite = False

numero = float(input("Escribe un número (0 para terminar): "))

while numero != 0:
    if inferior < numero < superior:
        suma += numero
    elif numero < inferior or numero > superior:
        fuera += 1
    else:
        igual_limite = True

    numero = float(input("Escribe otro número (0 para terminar): "))

    print("Suma dentro del intervalo:", suma)
    print("Números fuera del intervalo:", fuera)
    print("¿Se introdujo un número igual a un límite?", igual_limite)
