import math
########################################## PARTE (1)
def area_rectangulo(base, altura):
    ''' Calcula el Area de un rectangulo '''
    if type(altura)!= int and type(base)!= int:
        if type(altura)!= float and type(base)!= float:
            print("Nose aceptan caracteres en esta funcion, Ingrese valores de tipo numerico")
        else:
            return print (base*altura)
    else:
        return print (base*altura)
#area_rectangulo()

############################################ PARTE (2)
def area_circulo(r):
    if type(r) != int:
        if type(r) != float:
            print("Nose aceptan caracteres en esta funcion, Ingrese valores de tipo numerico")
        else:
            area=math.pi*r**2
            return print('el area del circulo es %.3f ' % area)     
    else:
        area=math.pi*r**2
        return print('el area del circulo es %.3f ' % area)     
#area_circulo ()

############################################ PARTE(3)
def relacion(nro1,nro2):
    """Si el primer número es mayor que el segundo, debe devolver 1.
       Si el primer número es menor que el segundo, debe devolver -1.
       Si ambos números son iguales, debe devolver un 0.
    """
    if nro1 > nro2:
        return print(1) 
    elif nro1 < nro2:
        return print(-1)
    elif nro1 == nro2:
        return print(0) 
#relacion(5,5)

############################################ PARTE(4)

def intermedio (nro1,nro2):
    """ a partir de dos números, devuelva su punto intermedio:"""
    if type(nro1) != int and type(nro2) != int:
        if type(nro1) != float and type(nro2) != float:
            print("Nose aceptan caracteres en esta funcion, Ingrese valores de tipo numerico")
        else:
            total = nro1 + nro2
            return total / 2
    else:
        total = nro1 + nro2
        return total / 2
# print(intermedio())

############################################ PARTE(5)

def recortar (nro,limiteMaximo,limiteMinimo):
    '''Devolver el límite inferior si el número es menor que éste
       Devolver el límite superior si el número es mayor que éste.
       Devolver el número sin cambios si no se supera ningún límite
    '''
    if not nro < limiteMinimo and  not nro > limiteMaximo:
        return nro
    elif nro < limiteMinimo:
        return limiteMinimo
    elif nro > limiteMaximo:
        return limiteMaximo
#print(recortar(15,0,10))

############################################ PARTE(6)


def separar(lista):
    ''' toma una lista de números enteros y devuelva dos listas ordenadas. 
    La primera con los números pares, y la segunda con los números impares: '''
    listaPar = []
    listaInpar = []
    for i in (lista):
        if i % 2 == 0:
            listaPar.append(i)
        else:
            listaInpar.append(i)
    return print("Lista de numeros pares:",listaPar ," \n ", "Lista de numeros inpares:", listaInpar)

lista = [12,2,4,6,9,6,5,54,222,5 ]
separar (lista)





        


    

    


