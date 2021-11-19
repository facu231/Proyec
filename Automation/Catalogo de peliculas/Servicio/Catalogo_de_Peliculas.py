import os
class CatalogoDePeliculas:

    ruta_de_Archivo = 'Peliculas.txt'

    @classmethod
    def agregar_Peliculas(cls,Peliculas):
        try:
            with open(cls.ruta_de_Archivo, 'a', encoding='utf8' ) as archive:
                archive.write(f'{Peliculas.Nombre}\n')          
        except Exception as ERROR:
            print (f'Error en agregar_Pelicula: {ERROR}')
            
    @classmethod
    def Listar_Peliculas(cls):
        try:
            with open(cls.ruta_de_Archivo,'r', encoding='utf8') as archive:
                print ('Catalogo de Peliculas'.center(50,'#'))
                print (archive.read())
        except Exception as ERROR:
            print (f'Error en Listar_Peliculas: {ERROR}')
    @classmethod
    def eliminar_Archivo (cls):
        try:
            os.remove(cls.ruta_de_Archivo)
            print (f'Archivo Elmininada {cls.ruta_de_Archivo}')
        except Exception as OS:
            print(F'Error de Os {OS}')

