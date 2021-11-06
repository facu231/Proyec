class DispositivoDeConecxion:

    def __init__(self, marca, tipodeEntrada):
        self._marca = marca
        self._tipodeEntrada = tipodeEntrada

    @property
    def tipodeEntrada(self):
        return self._tipodeEntrada

    @tipodeEntrada.setter
    def tipodeEntrada(self,tipodeEntrada):
        self._tipodeEntrada = tipodeEntrada
    
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca = marca
    
    def __str__(self):
        return f'Marca {self._marca} , tipodeEntrada {self._tipodeEntrada}'
