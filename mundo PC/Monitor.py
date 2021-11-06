
class Monitor:

    contadorMonitor = 0
    
    def __init__(self,marca,tamaño):
        Monitor.contadorMonitor += 1
        self._idemonitor = Monitor.contadorMonitor
        self._marca = marca
        self._tamaño = tamaño

    @property
    def idemonitor(self):
        return self._idemonitor
    @idemonitor.setter
    def idemonitor(self, idemonitor):
        self._idemonitor = idemonitor
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    @property
    def tamaño(self):
        return self._tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self.tamaño = tamaño
    
    def __str__(self):
        return f'[ID:{self._idemonitor}]  [Marca:{self._marca}]  [Tamaño:{self._tamaño}]'

