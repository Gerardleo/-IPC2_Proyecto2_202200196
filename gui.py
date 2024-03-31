import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
import webbrowser
from xml.etree import ElementTree as ET
from Clases.Entrada import Entrada
from Clases.Maqueta import Maqueta
from Clases.Objetivos import Objetivos
from Clases.ListaDoble import lista_doble as ld
from Clases.printer import Printer as p


Ruta = None
Lista_maquetas = ld()
maquetaSeleccionada = None

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de texto")

        # Configuración del fondo
        root.configure(bg='#303030')  # Color gris oscuro para el fondo de la ventana principal

        self.editor_frame = tk.Frame(root, bg='#404040')  # Color gris un poco más claro para el fondo del marco
        self.editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 8))  # 10px padding en los lados, 10px arriba y 5px abajo

        # Configuración del menú
        self.menu_bar = tk.Menu(root, bg='#505050', fg='white', activebackground='#707070', activeforeground='white')  # Color gris claro para el fondo del menú, texto blanco y colores activos más claros
        root.config(menu=self.menu_bar)


        self.menu_bar.add_command(label="Inicializar", command=self.limpiarVariables)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg='#505050', fg='white', activebackground='#707070', activeforeground='white')  # Configuración similar para el menú desplegable de Archivo
        self.menu_bar.add_cascade(label="Carga de archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)


        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg='#505050', fg='white', activebackground='#707070', activeforeground='white')  # Configuración similar para el menú desplegable de Archivo
        self.menu_bar.add_cascade(label="Gestion de Maquetas", menu=self.file_menu)
        self.file_menu.add_command(label="Ver listado de maquetas", command=self.MostarMaquetas)
        self.file_menu.add_command(label="Seleccionar maqueta", command=self.seleccionarMaqueta)
        self.file_menu.add_command(label="Ver Grafica", command=self.graficarMaquetaSeleccionada)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg='#505050', fg='white', activebackground='#707070', activeforeground='white')  # Configuración similar para el menú desplegable de Archivo
        self.menu_bar.add_cascade(label="Resolución de maquetas", menu=self.file_menu)
        self.file_menu.add_command(label="Seleccionar maquetas para resolucion", command=self.open_file)
        self.file_menu.add_command(label="Ver Grafica de resolucion", command=self.save_file)

        self.menu_bar.add_command(label="Ayuda", command=self.ayuda)


        # Etiqueta para el primer editor
        self.label_editor1 = tk.Label(self.editor_frame, text="Entrada", bg='#404040', fg='white', padx=10, pady=5)
        self.label_editor1.grid(row=0, column=0, sticky="nsew")

        # Primer editor
        self.text_widget = ScrolledText(self.editor_frame, wrap=tk.WORD, bg='#505050', fg='white')  # Color gris claro para el fondo del editor y texto blanco
        self.text_widget.grid(row=1, column=0, sticky="nsew")

        # Separador entre editores
        separator = tk.Label(self.editor_frame, text="    ", bg='#404040')
        separator.grid(row=1, column=1, padx=10, pady=10)

        # Etiqueta para el segundo editor
        self.label_editor2 = tk.Label(self.editor_frame, text="Salida", bg='#404040', fg='white', padx=10, pady=5)
        self.label_editor2.grid(row=0, column=2, sticky="nsew")

        # Segundo editor
        self.second_text_widget = ScrolledText(self.editor_frame, wrap=tk.WORD, state='disabled', bg='#505050', fg='white')  # Color gris claro para el fondo del editor y texto blanco
        self.second_text_widget.grid(row=1, column=2, sticky="nsew")

        self.editor_frame.grid_columnconfigure(0, weight=1)
        self.editor_frame.grid_columnconfigure(2, weight=1)


    def open_file(self):
        global Ruta
        Ruta = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
        if Ruta:
            with open(Ruta, 'r') as file:
                print(Ruta)
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
            self.leer_xml(Ruta)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos XML", "*.xml")])
        if file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")

    def show_text(self):
        text = self.text_widget.get(1.0, tk.END)
        self.second_text_widget.config(state='normal')
        self.second_text_widget.delete(1.0, tk.END)
        self.second_text_widget.insert(tk.END, text)
        self.second_text_widget.config(state='disabled')

    def limpiarSalida(self):
        self.second_text_widget.config(state='normal')
        self.second_text_widget.delete(1.0, tk.END)
        self.second_text_widget.config(state='disabled') 

    def limpiarVariables(self):
        global Ruta, Lista_maquetas, maquetaSeleccionada
        self.text_widget.delete(1.0, tk.END)
        self.limpiarSalida()
        Ruta = ""
        Lista_maquetas = ld()
        maquetaSeleccionada = None
        messagebox.showinfo(
                         message="Se ha limpiado el archivo correctamente",
                     )


    def ayuda(self):
        # Crear una ventana para mostrar datos del estudiante y link de documentacion
        student_info = (
            "Curso: INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 \n"
            "Seccion: C \n\n"
            "Desarrollado por:\n"
            "  - Gerardo Leonel Ortiz Tobar - 202200196\n"
        )
        documentation_link = "https://github.com/Gerardleo/-IPC2_Proyecto2_202200196"
        message = f"{student_info}Documentación: {documentation_link}"

        # Mostrar el mensaje
        messagebox.showinfo(title="Ayuda",message=message)

        # Abrir el enlace en el navegador web
        webbrowser.open(documentation_link)

    def leer_xml(self, ruta):
        try:
            tree = ET.parse(ruta)
            root = tree.getroot()
        
            for maqueta in root.findall('.//maqueta'):
                nombre = maqueta.find('nombre').text.strip()
                filas = int(maqueta.find('filas').text)
                columnas = int(maqueta.find('columnas').text)
                estructura = maqueta.find('estructura').text.strip()
                if filas < 0 or columnas < 0:
                    print(f"Error: Los valores de fila y columna deben ser mayores a 0 en la maqueta {nombre}")
                else:                
                    nueva_maqueta = Maqueta(nombre, filas, columnas, estructura)
                    for entrada in maqueta.findall('.//entrada'):
                        fila = int(entrada.find('fila').text)
                        columna = int(entrada.find('columna').text)
                        nueva_entrada = Entrada(fila, columna)
                        nueva_maqueta.agregarEntrada(nueva_entrada)
                    for objetivo in maqueta.findall('.//objetivo'):
                        fila = int(objetivo.find('fila').text)
                        columna = int(objetivo.find('columna').text)
                        nombre = objetivo.find('nombre').text
                        nuevo_objetivo = Objetivos(nombre, fila, columna)
                        nueva_maqueta.agregarObjetivo(nuevo_objetivo)
                Lista_maquetas.insertar(nueva_maqueta)
                  
                    # Aquí puedes agregar el código para procesar otros elementos de la maqueta
        # except FileNotFoundError:
        #     print("Error: No se ha encontrado el archivo")
        # except ET.ParseError:
        #     print("Error: El archivo XML no tiene el formato correcto")
        # except AttributeError:
        #     print("Error: El archivo XML no tiene el formato correcto")
        # except ValueError:
        #     print("Error: El archivo XML no tiene el formato correcto")
        except Exception as e:
            print(f"Error: {e}")


    def MostarMaquetas(self):
        global Lista_maquetas, Ruta
        contenido = p()
        if Lista_maquetas.estaVacia() == False:
            Lista_maquetas.ordenar()
            contenido.add(Lista_maquetas.desplegar())
            self.second_text_widget.config(state='normal')
            self.second_text_widget.delete(1.0, tk.END)
            self.second_text_widget.insert(tk.END, contenido.getTexto())
            self.second_text_widget.config(state='disabled')
        else:
            messagebox.showwarning(title="Error",
                        message="No se ha cargado niguna maqueta",
                    )

    def seleccionarMaqueta(self):
        global Lista_maquetas, Ruta, maquetaSeleccionada
        contenido = p()
        if Ruta:
            Lista_maquetas.desplegar()
            #mostrar un cuadro de dialogo para seleccionar la maqueta

            maquetaSeleccionada = simpledialog.askstring("Seleccionar Maqueta", "Ingrese el nombre de la maqueta que desea seleccionar:")
            maqueta = Lista_maquetas.buscar(maquetaSeleccionada)
            if maqueta:
                contenido.add(maqueta.getValor().desplegar())
                self.second_text_widget.config(state='normal')
                self.second_text_widget.delete(1.0, tk.END)
                self.second_text_widget.insert(tk.END, contenido.getTexto())
                self.second_text_widget.config(state='disabled')
                messagebox.showinfo(
                        message="Se ha seleccionado la maqueta correctamente",
                    )
            else:
                messagebox.showwarning(title="Error", message="No se ha encontrado la maqueta")	
        else:
            messagebox.showwarning(title="Error",
                        message="No se ha seleccionado ningun archivo",
                    )
    
    def graficarMaquetaSeleccionada(self):
        global maquetaSeleccionada
        if maquetaSeleccionada:
            maqueta = Lista_maquetas.buscar(maquetaSeleccionada)
            if maqueta:
                dot = maqueta.getValor().generar_dot()
                maqueta.getValor().generar_imagen_dot(dot, f'{maquetaSeleccionada}')
                webbrowser.open(f'{maquetaSeleccionada}.png')
                messagebox.showinfo(
                        message="Se ha generado la grafica correctamente",
                    )
            else:
                messagebox.showwarning(title="Error",
                        message="No se ha encontrado la maqueta",
                    )
        else:
            messagebox.showwarning(title="Error",
                        message="No se ha seleccionado ninguna maqueta",
                    )
    #     if Ruta:
    #         inicializador(Ruta)

    #         messagebox.showinfo(
    #                     message="Se ha analizado el archivo correctamente",
    #                 )
    #     else:
    #         messagebox.showwarning(
    #                     message="No se ha seleccionado ningun archivo",
    #                 )
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
