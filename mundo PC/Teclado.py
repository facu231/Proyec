
from  dispositivo_de_conecxion import DispositivoDeConecxion

class Teclado(DispositivoDeConecxion):

    contadorTeclados =0
    def __init__(self, marca, tipodeEntrada):
        Teclado.contadorTeclados+=1
        self._ideteclado = Teclado.contadorTeclados
        DispositivoDeConecxion.__init__(self, marca, tipodeEntrada)
    @property
    def ideteclado(self):
        return self._ideteclado

    @ideteclado.setter
    def ideteclado(self,ideteclado):
        self._ideteclado = ideteclado
    def __str__(self):
        return f'[Ide:{self._ideteclado}] , {DispositivoDeConecxion.__str__(self)} ]'
