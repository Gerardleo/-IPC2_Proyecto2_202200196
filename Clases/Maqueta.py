from Clases.ListaDoble import lista_doble as ld
from Clases.printer import Printer as p
import graphviz as gv


class Maqueta:
    def __init__(self, nombre, filas, columnas, estructura):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.entrada = ld()
        self.objetivos = ld()
        self.estructura = estructura

    def agregarObjetivo(self, objetivo):
        self.objetivos.insertar(objetivo)
    
    def agregarEntrada(self, entrada):
        self.entrada.insertar(entrada)
    
    def getNombre(self):
        return self.nombre
    
    def getFilas(self):
        return self.filas
    
    def getColumnas(self):
        return self.columnas
    
    def getEstructura(self):
        return self.estructura
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setFilas(self, filas):
        self.filas = filas

    def setColumnas(self, columnas):
        self.columnas = columnas
    
    def setEstructura(self, estructura):
        self.estructura = estructura
    
    def getObjetivos(self):
        return self.objetivos
    
    def getEntrada(self):
        return self.entrada
    
    def desplegar(self):
        contenido = p()
        contenido.add(f"===================================")
        contenido.add(f"         Maqueta: {self.nombre}   ")
        contenido.add(f"===================================")
        contenido.add(f"Filas: {self.filas}")
        contenido.add(f"Columnas: {self.columnas}")
        contenido.add(f"Estructura: {self.estructura}")
        contenido.add(f"===================================")
        contenido.add(f"           Entradas:               ")
        contenido.add(f"===================================")
        self.entrada.ordenar()
        contenido.add(self.entrada.desplegar())
        contenido.add(f"===================================")
        contenido.add(f"           Objetivos:              ")
        contenido.add(f"===================================")
        self.objetivos.ordenar()
        contenido.add(self.objetivos.desplegar())
        return contenido.getTexto()
       
    def generar_dot(self):
        dot_code = 'digraph G {\n'
        dot_code += 'node [shape=plaintext];\n'
        dot_code += 'matriz [label=<<TABLE CELLSPACING="0" CELLPADDING="5" border="0">\n'  # Modificación aquí
        estructura = self.estructura

        for i in range(self.filas):
            dot_code += '<TR>'
            for j in range(self.columnas):
                char = estructura[i * self.columnas + j]  # Calcular el índice correcto en la cadena
                if self.entrada.buscar(f'{i},{j}') is not None:
                    color = 'blue'
                elif char == '-':
                    color = 'white'
                else:
                    color = 'black'
                dot_code += f'<TD BGCOLOR="{color}" WIDTH="30" HEIGHT="30"></TD>'
            dot_code += '</TR>'

        dot_code += '</TABLE>>];'
        dot_code += '}'

        return dot_code


    
    
    def generar_imagen_dot(self,dot_code, file_path='maqueta.png'):
        with open('archivo.dot', 'w') as dot_file:
            dot_file.write(dot_code)
        graph = gv.Source(dot_code)
        graph.render(file_path, format='png', cleanup=True)