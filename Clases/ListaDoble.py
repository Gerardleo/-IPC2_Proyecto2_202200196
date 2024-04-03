from Clases.Nodo import Nodo as nodo
import graphviz as gv

class lista_doble:
  def __init__(self):
    self.primero = None


  def insertar(self, valor):
    nuevo = nodo(valor)
    if self.primero == None:
      self.primero = nuevo
    else:
      temp = self.primero
      while temp.siguiente != None:
        temp = temp.siguiente
      temp.siguiente = nuevo
      nuevo.anterior = temp
    
  def buscar(self, valor):
    temp = self.primero
    while temp != None:
      if temp.getValor().getNombre() == valor:
        return temp
      temp = temp.siguiente
    return None
  
  def eliminar(self, valor):
    temp = self.buscar(valor)
    if temp != None:
      if temp.anterior == None:
        self.primero = temp.siguiente
        temp.siguiente.anterior = None
      elif temp.siguiente == None:
        temp.anterior.siguiente = None
      else:
        temp.anterior.siguiente = temp.siguiente
        temp.siguiente.anterior = temp.anterior
      return True
    return False
  
  def desplegar(self):
    temp = self.primero
    contenido = ""
    while temp != None:
      #print(temp.getValor().getNombre())
      contenido += temp.getValor().desplegar()
      temp = temp.siguiente
    return contenido

  def ordenar(self):
    temp = self.primero
    while temp != None:
      temp2 = temp.siguiente
      while temp2 != None:
        if temp.getValor().getNombre() > temp2.getValor().getNombre():
          aux = temp.getValor()
          temp.setValor(temp2.getValor())
          temp2.setValor(aux)
        temp2 = temp2.siguiente
      temp = temp.siguiente

  def estaVacia(self):
    if self.primero == None:
      return True
    return False
  
  def buscarEntrada(self, fila, columna):
    temp = self.primero
    while temp != None:
      if temp.getValor().getFila() == fila and temp.getValor().getColumna() == columna:
        return True
      temp = temp.siguiente
    return False
  

  def buscarObjetivo(self, fila, columna):
    temp = self.primero
    while temp != None:
      if temp.getValor().getFila() == fila and temp.getValor().getColumna() == columna:
        return temp.getValor().getNombre()
      temp = temp.siguiente
    return None
  
  def generar_dot(self):
    dot_code = 'digraph G {\n'
    dot_code += 'node [shape=plaintext];\n'
    dot_code += 'matriz [label=<<TABLE CELLSPACING="0" CELLPADDING="5" border="0">\n'

    nodo_fila = self.primero
    while nodo_fila is not None:
        dot_code += '<TR>'
        nodo_temp = nodo_fila.valor.primero
        while nodo_temp is not None:
            valor = nodo_temp.valor
            if valor is not None:
                if valor == '*':
                    dot_code += f'<TD BGCOLOR="black" WIDTH="30" HEIGHT="30">{valor}</TD>'
                elif valor == '-':
                    dot_code += f'<TD BGCOLOR="#ADD8E6" WIDTH="30" HEIGHT="30"></TD>'  # Color azul claro
                elif valor == 'X':  # Marcar el camino hacia el objetivo con un color diferente
                    dot_code += f'<TD BGCOLOR="yellow" WIDTH="30" HEIGHT="30">{valor}</TD>'  # Color amarillo para el camino hacia el objetivo
                else:
                    dot_code += f'<TD BGCOLOR="white" WIDTH="30" HEIGHT="30">{valor}</TD>'
            else:
                dot_code += '<TD></TD>'  # Caso para nodos sin valor (None)
            nodo_temp = nodo_temp.siguiente
        dot_code += '</TR>'
        nodo_fila = nodo_fila.siguiente

    dot_code += '</TABLE>>];'
    dot_code += '}'

    return dot_code


  
  def generar_imagen_dot(self,dot_code, file_path='maquetaResolucion'):
      with open('archivoResolucion.dot', 'w') as dot_file:
            dot_file.write(dot_code)
      graph = gv.Source(dot_code)
      graph.render(file_path, format='png', cleanup=True)
     
     


