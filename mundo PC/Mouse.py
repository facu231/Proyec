from dispositivo_de_conecxion import DispositivoDeConecxion

class Mouse(DispositivoDeConecxion):

    contado_mouse = 0

    def __init__(self,marca, tipodeEntrada):
        Mouse.contado_mouse +=1
        self._ide_mouse = Mouse.contado_mouse
        DispositivoDeConecxion.__init__(self,marca, tipodeEntrada)

    @property
    def ide_mouse(self):
        return self._ide_mouse

    @ide_mouse.setter
    def ide_mouse(self,ide_mouse):
        self.ide_mouse = ide_mouse
    
    
    def __str__(self):
        return f'IDE Mouse {self.ide_mouse}  , {DispositivoDeConecxion.__str__(self)}'


