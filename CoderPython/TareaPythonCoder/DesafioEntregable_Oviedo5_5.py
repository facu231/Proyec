print("""Programa que pide al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo

""".upper())
opcion = int(input('Elija un Numero del 1 al 9: '))
numeros = [1, 3, 6, 9]

while opcion not in numeros:
    if opcion <= 9:
        opcion = int(input('Incorrecto! Elija Otro Numero del 1 al 9: '.center(50,'*')))
else:
    print(f'{opcion} esta en la lista {numeros} correcto!!!'.upper())


        
