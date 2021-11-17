print("Programa de 4 Opciones Para 2 numeros".center(50,"*"))
print("""
1 Mostrar una suma de los dos números
2 Mostrar una resta de los dos números (el primero menos el segundo)
3 Mostrar una multiplicación de los dos números
4 Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
5 En caso de no introducir una opción válida, el programa informará de que no es correcta.
""")


pregunta = input("")
numero_1 = int(input("Ingresa tu primer numero: "))
numero_2 = int(input("Ingresa tu segundo numero: "))
opcion = int(input("Ingresa tu Opcion: "))

while opcion != 4:
    if opcion >= 5:
        opcion = int(input("""Ingresa Otra Opcion Valida... 
Sin c ABC. y numeros Superiores a 4: """ )) 
        if opcion == 4:
            print(' Programa finalizado '.center(50,'#'))
            break
    if opcion == 1:
        suma = numero_1 + numero_2 
        print(f'La suma de los 2 nuemros es: {suma}')
    elif opcion == 2:
        resta = numero_1 - numero_2
        print(f'La resta de los 2 nuemros es: {resta}')
    elif opcion == 3:
        multiplicación = numero_1 * numero_2
        print(f'La multiplicación entre los 2 numeros es: {multiplicación}')
    opcion = int(input("Ingrese su nueva Opcion: "))
else: 
    print(' Programa finalizado '.center(50,'#'))


    

    




  
