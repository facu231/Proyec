class Peliculas:

    def __init__(self,Nombre):
        self._Nombre = Nombre

    @property
    def Nombre(self):
        try:
            return self._Nombre
        except Exception as N:
            print(f'Error de atributo: {N}')

    @Nombre.setter
    def Nombre(self,Nombre):
        try:
            self._Nombre = Nombre
        except Exception as N:
            print(f'Error de atributo: {N}')

    def __str__(self):
        try:
            return self._Nombre
        except Exception as N:
            print (f'Error de atributo: {N}')


