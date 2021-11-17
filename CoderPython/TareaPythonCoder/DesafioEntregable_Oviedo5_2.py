####################################### PARTE 2 ##############################################

print(""" 
Programa que lee un número impar por teclado. Si el usuario no introduce un número impar 
se repetira el proceso hasta que lo introduzca correctamente.
""")

numero = int (input('Ingresa un numero Inpar.'))
while numero % 2 == 0 :
    print('El número', numero, 'es par')
    numero = int (input(f'el nuemro {numero} es Par Introdusca un numero Inpar por favor.'))

else:
    print(f'El número {numero} es impar.')

print(' Fin del programa '.center(50,'*'))

