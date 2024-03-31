from Clases.printer import Printer as p

class Entrada:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna
    
    def setFila(self, fila):
        self.fila = fila

    def setColumna(self, columna):
        self.columna = columna

    def desplegar(self):
        contenido = p()
        contenido.add(f"Entrada en fila {self.fila} y columna {self.columna}")
        return contenido.getTexto()
    
    def buscar(self, fila, columna):
        if self.fila == fila and self.columna == columna:
            return True
        return False