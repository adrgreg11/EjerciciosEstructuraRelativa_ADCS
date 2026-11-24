#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

caracter = input("Escribe una letra (espacio para terminar): ")

while caracter != " ":
    if caracter.lower() in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")

    caracter = input("Escribe otra letra (espacio para terminar): ")