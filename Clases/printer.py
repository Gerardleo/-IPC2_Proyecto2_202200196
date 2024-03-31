class Printer:
    def __init__(self):
        self.texto = ""

    def add(self, mensaje):
        self.texto += mensaje + "\n"

    def getTexto(self):
        return self.texto
