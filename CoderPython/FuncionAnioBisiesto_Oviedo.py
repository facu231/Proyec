def anio_bisiesto(anio):
    '''Funsion que verifica que el año depositado sea bisiesto'''
    if type(anio) !=int:
        print('Ingrese un valor numerico Por favor'.center(50,'*'))
    else:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            print(" Es bisiesto ".center(50,'!'))
        else:
            print(" No es bisiesto ".center(50,'X'))
            
anio_bisiesto(2010)
    
    