from Dominio.Peliculas import Peliculas
from Servicio.Catalogo_de_Peliculas import CatalogoDePeliculas as CP

Opcion = None
while Opcion !=4:
    try:
        print(' Bienvenido A catalogo de Peliculas.. '.center(50,'#'))
        print('1. Agregar Pelicula')
        print('2. Mostrar Catalogo Actual')
        print('3. Eliminar Catalogo')
        print('4 Salir De la Aplicacion...')
        Opcion = int(input('Agregue una Opcion de las Siguientes 1-4.: '))
        if Opcion == 1:
            nombre_pelicula = input(' Agregue el Nombre de Su pelicula ' ) 
            Pelicula1 = Peliculas(nombre_pelicula)
            CP.agregar_Peliculas(Pelicula1)
        elif Opcion == 2:
            CP.Listar_Peliculas()
        elif Opcion == 3:
            CP.eliminar_Archivo()
    except Exception as ERROR:
        print (f'ERROR {ERROR} de la aplicacion')
        opcion = None
else:
    print('Salimos del programa...')





        
      

