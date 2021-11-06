
class Funciones:



    def suma_de_Enteros (self,Lista):
        try:
            print('Empieza el metodo Suma_de_Enteros')
            entero = 0
            primo = 0
            for numero in range(Lista):
                if numero % 2 == 0:
                    entero +=1
                    print(f'entero: {numero}')
                else:
                    primo += 1
                    print(f'primo: {numero}')
        except Exception as E:      
            print(f'Error.{E} Nos comunicaremos con control de Calidad') 
    


    
    def potencias(self,*kaka):
        resultado = 0
        try:
            for numero in range(kaka):
                resultado = numero**numero
                print(f'Resultado{resultado}')

        except Exception as E: 
            print(f'Error Inesperado.{E}')
        else:
            print('funcion exitosa')










