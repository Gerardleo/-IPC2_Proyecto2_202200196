
class Nodo:
    def __init__(self, valor, siguiente = None):
        self.valor = valor
        self.siguiente = siguiente
        self.anterior = None

    def getValor(self):
        return self.valor
    
    def getSiguiente(self):
        return self.siguiente
    
    def getAnterior(self):
        return self.anterior
    
    def setValor(self, valor):
        self.valor = valor

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def setAnterior(self, anterior):
        self.anterior = anterior

    def desplegar(self):
        return self.valor
    