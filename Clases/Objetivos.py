from Clases.printer import Printer as p

class Objetivos:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def getNombre(self):
        return self.nombre
    
    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setFila(self, fila):
        self.fila = fila

    def setColumna(self, columna):
        self.columna = columna

    def desplegar(self):
        contenido = p()
        contenido.add(f"Objetivo {self.nombre} en fila {self.fila} y columna {self.columna}")
        return contenido.getTexto()