
print("""
programa que pide al usuario cuantos números quiere introducir. 
Luego lee todos los números y realiza una media aritmética

""".upper())

numero = int(input('Ingresa los Numeros que quieras: '))
cantidad = 0
suma = 0
total = 0


while numero!=0:
    cantidad += 1
    suma += numero
    total = suma / cantidad
    numero = int(input('Ingresa los Numeros que quieras: '))
else:
    print(f'Se an Ingresado: {cantidad} numeros'.center(50,'*'))
    print (f"La media de todos los Numeros es: {total}".upper())



    
    
