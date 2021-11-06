from Monitor import Monitor
from Mouse import Mouse
from Teclado import Teclado

class CPU (Monitor , Mouse , Teclado ):

    contadorCPU = 0 
    def __init__(self,nombre , monitor, teclado, mouse):
        CPU.contadorCPU +=1
        self._IdeCPU = CPU.contadorCPU
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor


    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado
    
    @property
    def mouse(self):
        return self._mouse

    @mouse.setter
    def mouse(self, mouse):
        self._mouse = mouse


    def __str__(self):
        return f'''
        Nombre :[{self._nombre}ID {self._IdeCPU}]
        Monitor:[{self._monitor}]
        Teclado:[{self._teclado}]
        Mouse:[{self._mouse}]  
        '''

teclado1 = Teclado('Gamer','USB')
mouse = Mouse ('Gamer', 'USB')
monitor1 = Monitor('SONY', '15')
computadora = CPU ('Zeus,',monitor1,teclado1,mouse)

print (computadora)


