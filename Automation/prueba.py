def Cobranza():
    #''' Funcion Para calcular montos... 
    # si el total pasa a ser mayor de  1000
    #  se descuenta un 10% del monto total '''
    try: 
        print( " Bienvenido a sector de Combranzasas " .center(50,'*'))
        monto = float(input( ' Ingresar Monto:$ '))
        total = 0
        while monto !=0: 
            if monto <0:
                print(" Monto  invalido Ingrese un nuevo monto ".upper().center(50,'#'))
            else:
                total+=monto
            monto = float(input( ' Ingresar Monto:$ '))
        if total >= 1000:
            total-=total*0.10
        print(f"Total a Cobrar $: {total}")
    except Exception as Error:
        print(f"Error Inesperado.... : {Error}")

Cobranza()

def contador_de_Numeros_ParesYInpares():
# ''' Funcion para contar todos los numeros Pares e inpares 
# que hay en un numero que coloque el Usuario'''
    try:
        numeros = int ((input("Ingrese sus numero  ")))
        contadorPar = 0
        contadorInpar = 0
        while numeros !=0:
            pares = 0
            Inpares = 0
            while numeros !=0:
                ultimoDigito = numeros % 10
                if ultimoDigito % 2 == 0:
                    pares +=1
                    contadorPar+=1
                else:
                    Inpares+=1
                    contadorInpar+=1
                numeros=numeros//10
            print (f"Total de numeros Pares: {pares}")
            print (f"Total de Numeros Inpares: {Inpares}")
            numeros = int ((input("Ingrese sus numero  ")))
    except Exception as Error:
        print (f"Error Inesperado: {Error}")
        print (f"Total de numeros Pares: {contadorPar}")
        print (f"Total de numeros Inpares: {contadorInpar}")





      
    

