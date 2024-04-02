from Clases.Nodo import Nodo as nodo

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

