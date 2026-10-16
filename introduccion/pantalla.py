# Pantalla de introducción del proyecto.
# Explica el objetivo, las herramientas, el proceso de trabajo y lo aprendido.

import tkinter as tk
import webbrowser

lienzo_introduccion=None
ventana_del_contenido=None
direccion_del_proyecto="https://github.com/juanpisurzolamarin-prog/nuevo-proyecto"


def dibujar_icono_introduccion(lienzo):
    # Recibe el lienzo de la tarjeta del inicio.
    # Dibuja un saludo para reconocer la introducción.
    # No devuelve nada.
    lienzo.create_oval(46,6,124,78,fill="#ede9fe",outline="#6d28d9",width=3)
    lienzo.create_text(85,42,text="Hola",font=("Segoe UI",22,"bold"),fill="#6d28d9")

def dibujar_icono_python(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja dos círculos, azul y amarillo, como la marca de Python.
    # No devuelve nada.
    lienzo.create_oval(8,10,44,46,fill="#3776ab",outline="")
    lienzo.create_oval(28,26,64,62,fill="#ffd343",outline="")

def dibujar_icono_cursor(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja una flecha de cursor, la herramienta donde se escribió el código.
    # No devuelve nada.
    lienzo.create_polygon(16,10,16,58,30,44,42,62,50,56,36,38,56,38,fill="#1d3557",outline="")

def dibujar_icono_baldor(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja un libro, el Álgebra de Baldor.
    # No devuelve nada.
    lienzo.create_rectangle(14,12,58,60,fill="#9a3412",outline="")
    lienzo.create_rectangle(14,12,22,60,fill="#7c2d12",outline="")
    lienzo.create_text(40,36,text="B",font=("Segoe UI",18,"bold"),fill="#ffedd5")

def dibujar_icono_grok(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja una chispa para la inteligencia artificial.
    # No devuelve nada.
    lienzo.create_polygon(36,6,42,26,62,32,42,38,36,58,30,38,10,32,30,26,fill="#7c3aed",outline="")

def dibujar_icono_objetivo(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja una meta, el objetivo de aprender.
    # No devuelve nada.
    lienzo.create_oval(12,12,60,60,outline="#0f766e",width=4)
    lienzo.create_oval(24,24,48,48,outline="#0f766e",width=4)
    lienzo.create_oval(32,32,40,40,fill="#0f766e",outline="")

def dibujar_icono_plan(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja una hoja con tres renglones, el plan.
    # No devuelve nada.
    lienzo.create_rectangle(16,8,56,64,fill="#ffffff",outline="#b45309",width=3)
    lienzo.create_line(24,22,48,22,fill="#b45309",width=3)
    lienzo.create_line(24,34,48,34,fill="#b45309",width=3)
    lienzo.create_line(24,46,40,46,fill="#b45309",width=3)

def dibujar_icono_agente(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja una persona sencilla, el agente que escribe siguiendo el plan.
    # No devuelve nada.
    lienzo.create_oval(24,8,48,32,fill="#dbeafe",outline="#1d4ed8",width=3)
    lienzo.create_arc(14,36,58,78,start=0,extent=180,fill="#dbeafe",outline="#1d4ed8",width=3)

def dibujar_icono_prueba(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja una paloma, la prueba contra el ejercicio hecho a mano.
    # No devuelve nada.
    lienzo.create_line(12,36,28,52,58,16,fill="#15803d",width=6,capstyle="round",joinstyle="round")

def dibujar_icono_algoritmo(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja los números 1, 2 y 3, los pasos de un algoritmo.
    # No devuelve nada.
    lienzo.create_text(36,36,text="1  2  3",font=("Segoe UI",14,"bold"),fill="#6d28d9")

def dibujar_icono_variable(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja una caja con x, una variable.
    # No devuelve nada.
    lienzo.create_rectangle(12,18,60,54,fill="#fff7ed",outline="#b45309",width=3)
    lienzo.create_text(36,36,text="x",font=("Segoe UI",18,"bold"),fill="#b45309")

def dibujar_icono_funcion(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja f(x), el nombre de una función.
    # No devuelve nada.
    lienzo.create_text(36,36,text="f(x)",font=("Segoe UI",16,"bold"),fill="#1d4ed8")

def dibujar_icono_libreria(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja tres libros, una librería de funciones.
    # No devuelve nada.
    lienzo.create_rectangle(10,20,26,58,fill="#2f6fed",outline="")
    lienzo.create_rectangle(28,12,44,58,fill="#0f766e",outline="")
    lienzo.create_rectangle(46,24,62,58,fill="#b45309",outline="")

def dibujar_icono_condicional(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja un camino que se parte en dos, un condicional.
    # No devuelve nada.
    lienzo.create_line(36,10,36,28,fill="#9a3412",width=4)
    lienzo.create_line(36,28,14,54,fill="#9a3412",width=4)
    lienzo.create_line(36,28,58,54,fill="#9a3412",width=4)
    lienzo.create_text(36,24,text="if",font=("Segoe UI",10,"bold"),fill="#9a3412")

def dibujar_icono_ciclo(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja una vuelta, un ciclo que se repite.
    # No devuelve nada.
    lienzo.create_oval(14,14,58,58,outline="#0f766e",width=4)
    lienzo.create_polygon(50,12,62,22,46,24,fill="#0f766e",outline="")

def dibujar_icono_tiempo(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja un reloj, las horas que tomó el proyecto.
    # No devuelve nada.
    lienzo.create_oval(12,12,60,60,outline="#6d28d9",width=4)
    lienzo.create_line(36,36,36,22,fill="#6d28d9",width=3,capstyle="round")
    lienzo.create_line(36,36,48,44,fill="#6d28d9",width=3,capstyle="round")

def dibujar_icono_github(lienzo):
    # Recibe un lienzo pequeño.
    # Dibuja un círculo para compartir el proyecto.
    # No devuelve nada.
    lienzo.create_oval(10,10,62,62,fill="#1d3557",outline="")
    lienzo.create_text(36,36,text="Git",font=("Segoe UI",12,"bold"),fill="#ffffff")

def enlazar_clic(widget,funcion):
    # Recibe un cuadro y la función que debe correr al hacer clic.
    # Pone ese clic en el cuadro y en lo que tiene dentro.
    # No devuelve nada.
    widget.bind("<Button-1>",funcion)
    for hijo in widget.winfo_children():
        enlazar_clic(hijo,funcion)

def poner_opcion_en_el_inicio(marco,al_pulsar):
    # Recibe el marco del inicio y la función que abre esta pantalla.
    # Pone una tarjeta ancha, antes de los tres temas.
    # No devuelve nada.
    tarjeta=tk.Frame(marco,bg="#ffffff",highlightbackground="#6d28d9",highlightthickness=3,cursor="hand2")
    tarjeta.grid(row=4,column=0,columnspan=3,padx=24,pady=(4,4),sticky="ew")
    lienzo=tk.Canvas(tarjeta,width=150,height=84,bg="#ffffff",highlightthickness=0,cursor="hand2")
    lienzo.grid(row=0,column=0,rowspan=2,padx=(12,0),pady=8)
    dibujar_icono_introduccion(lienzo)
    nombre=tk.Label(tarjeta,text="Introducción",font=("Segoe UI",22,"bold"),bg="#ffffff",fg="#6d28d9",cursor="hand2")
    nombre.grid(row=0,column=1,sticky="sw",padx=8)
    detalle=tk.Label(
        tarjeta,
        text="Por qué lo hice, qué herramientas usé y qué aprendí.",
        font=("Segoe UI",14),
        bg="#ffffff",
        fg="#33415c",
        cursor="hand2",
    )
    detalle.grid(row=1,column=1,sticky="nw",padx=8,pady=(0,10))
    tarjeta.grid_columnconfigure(1,weight=1)
    enlazar_clic(tarjeta,al_pulsar)

def al_cambiar_el_contenido(evento):
    # Recibe el aviso de que el contenido cambió de tamaño.
    # Ajusta el largo de la barra para poder bajar.
    # No devuelve nada.
    lienzo_introduccion.configure(scrollregion=lienzo_introduccion.bbox("all"))

def al_cambiar_el_ancho(evento):
    # Recibe el ancho nuevo de la ventana.
    # Hace que el texto use todo ese ancho.
    # No devuelve nada.
    lienzo_introduccion.itemconfig(ventana_del_contenido,width=evento.width)

def al_girar_rueda(evento):
    # Recibe el giro de la rueda del ratón.
    # Baja o sube la página.
    # No devuelve nada.
    if evento.delta>0:
        lienzo_introduccion.yview_scroll(-3,"units")
    else:
        lienzo_introduccion.yview_scroll(3,"units")

def enlazar_rueda(widget):
    # Recibe un cuadro de la página.
    # Permite bajar con la rueda también encima de los textos.
    # No devuelve nada.
    widget.bind("<MouseWheel>",al_girar_rueda)
    for hijo in widget.winfo_children():
        enlazar_rueda(hijo)

def crear_titulo(marco,texto,fila):
    # Recibe el marco, el título y la fila.
    # Escribe un título morado de sección.
    # Devuelve la fila siguiente.
    etiqueta=tk.Label(
        marco,
        text=texto,
        font=("Segoe UI",20,"bold"),
        bg="#eef3fa",
        fg="#6d28d9",
        anchor="w",
    )
    etiqueta.grid(row=fila,column=0,columnspan=2,sticky="ew",padx=8,pady=(18,6))
    return fila+1

def crear_parrafo(marco,texto,fila):
    # Recibe el marco, el párrafo y la fila.
    # Escribe el texto en una tarjeta blanca.
    # Devuelve la fila siguiente.
    tarjeta=tk.Frame(marco,bg="#ffffff",highlightbackground="#ddd6fe",highlightthickness=2)
    tarjeta.grid(row=fila,column=0,columnspan=2,sticky="ew",padx=8,pady=4)
    etiqueta=tk.Label(
        tarjeta,
        text=texto,
        font=("Segoe UI",15),
        bg="#ffffff",
        fg="#1d3557",
        justify="left",
        anchor="w",
        wraplength=860,
        padx=16,
        pady=12,
    )
    etiqueta.pack(fill="x")
    return fila+1

def crear_tarjeta_horizontal(marco,dibujar,titulo,texto,color,fila):
    # Recibe el dibujo, los textos, el color y la fila.
    # Arma una tarjeta con el icono a la izquierda y la explicación a la derecha.
    # Devuelve la fila siguiente.
    tarjeta=tk.Frame(marco,bg="#ffffff",highlightbackground=color,highlightthickness=2)
    tarjeta.grid(row=fila,column=0,columnspan=2,sticky="ew",padx=8,pady=4)
    lienzo=tk.Canvas(tarjeta,width=72,height=72,bg="#ffffff",highlightthickness=0)
    lienzo.grid(row=0,column=0,padx=12,pady=10)
    dibujar(lienzo)
    caja=tk.Frame(tarjeta,bg="#ffffff")
    caja.grid(row=0,column=1,sticky="ew",padx=(0,12),pady=8)
    nombre=tk.Label(caja,text=titulo,font=("Segoe UI",16,"bold"),bg="#ffffff",fg=color,anchor="w")
    nombre.grid(row=0,column=0,sticky="ew")
    detalle=tk.Label(
        caja,
        text=texto,
        font=("Segoe UI",14),
        bg="#ffffff",
        fg="#33415c",
        justify="left",
        anchor="w",
        wraplength=760,
    )
    detalle.grid(row=1,column=0,sticky="ew")
    tarjeta.grid_columnconfigure(1,weight=1)
    caja.grid_columnconfigure(0,weight=1)
    return fila+1

def crear_tarjeta_pequena(marco,dibujar,titulo,texto,color,fila,columna):
    # Recibe el dibujo, los textos, el color, la fila y la columna.
    # Arma una tarjeta corta para una idea, como variable o función.
    # No devuelve nada.
    tarjeta=tk.Frame(marco,bg="#ffffff",highlightbackground=color,highlightthickness=2)
    tarjeta.grid(row=fila,column=columna,sticky="nsew",padx=8,pady=4)
    lienzo=tk.Canvas(tarjeta,width=72,height=64,bg="#ffffff",highlightthickness=0)
    lienzo.grid(row=0,column=0,pady=(8,0))
    dibujar(lienzo)
    nombre=tk.Label(tarjeta,text=titulo,font=("Segoe UI",15,"bold"),bg="#ffffff",fg=color)
    nombre.grid(row=1,column=0,pady=(0,2))
    detalle=tk.Label(
        tarjeta,
        text=texto,
        font=("Segoe UI",13),
        bg="#ffffff",
        fg="#33415c",
        justify="center",
        wraplength=400,
        padx=10,
        pady=8,
    )
    detalle.grid(row=2,column=0)

def abrir_el_proyecto(evento):
    # Recibe el clic del enlace.
    # Abre el proyecto en GitHub, en el navegador.
    # No devuelve nada.
    webbrowser.open(direccion_del_proyecto)

def crear_tarjeta_de_github(marco,fila):
    # Recibe el marco y la fila.
    # Explica por qué el proyecto está en GitHub y deja abrirlo con un clic.
    # Devuelve la fila siguiente.
    tarjeta=tk.Frame(marco,bg="#ffffff",highlightbackground="#1d3557",highlightthickness=2)
    tarjeta.grid(row=fila,column=0,columnspan=2,sticky="ew",padx=8,pady=4)
    lienzo=tk.Canvas(tarjeta,width=72,height=72,bg="#ffffff",highlightthickness=0)
    lienzo.grid(row=0,column=0,rowspan=3,padx=12,pady=10)
    dibujar_icono_github(lienzo)
    titulo=tk.Label(tarjeta,text="Compartirlo",font=("Segoe UI",16,"bold"),bg="#ffffff",fg="#1d3557",anchor="w")
    titulo.grid(row=0,column=1,sticky="ew",pady=(10,0))
    texto=tk.Label(
        tarjeta,
        text="Descubrí que puedo compartir el proyecto en GitHub. Así otros niños que tienen las mismas dificultades que yo pueden verlo y practicar.",
        font=("Segoe UI",14),
        bg="#ffffff",
        fg="#33415c",
        justify="left",
        anchor="w",
        wraplength=760,
    )
    texto.grid(row=1,column=1,sticky="ew",padx=(0,12))
    enlace=tk.Label(
        tarjeta,
        text="Haz clic aquí para abrir el proyecto.",
        font=("Segoe UI",14,"bold"),
        bg="#ffffff",
        fg="#2f6fed",
        cursor="hand2",
        anchor="w",
    )
    enlace.grid(row=2,column=1,sticky="w",pady=(0,12))
    enlace.bind("<Button-1>",abrir_el_proyecto)
    tarjeta.grid_columnconfigure(1,weight=1)
    return fila+1

def poner_lo_aprendido(marco,fila):
    # Recibe el marco y la fila donde empiezan las tarjetas.
    # Pone las ideas nuevas en dos columnas: algoritmo, Python, variable y las demás.
    # Devuelve la fila que queda libre debajo.
    ideas=[]
    ideas.append(("Algoritmo","Es una lista de pasos en orden. Por ejemplo: primero el paréntesis de adentro y después los términos semejantes.","#6d28d9",dibujar_icono_algoritmo))
    ideas.append(("Python","Es el lenguaje con el que está escrito este programa. Con él la computadora abre la ventana y hace las cuentas.","#3776ab",dibujar_icono_python))
    ideas.append(("Variable","Es una caja con nombre. Guarda un valor, como el 6 de 6x o el texto de una ecuación.","#b45309",dibujar_icono_variable))
    ideas.append(("Función","Es una tarea con nombre. Recibe algo, hace una sola cosa y devuelve un resultado.","#1d4ed8",dibujar_icono_funcion))
    ideas.append(("Librería","Es un grupo de funciones ya hechas. Tkinter es la librería que dibuja esta ventana.","#0f766e",dibujar_icono_libreria))
    ideas.append(("Condicional","Es un if. El programa pregunta y elige un camino. Si la x es negativa, cambia los signos.","#9a3412",dibujar_icono_condicional))
    ideas.append(("Ciclo","Es un for o un while. Repite un paso varias veces, hasta que el trabajo termina.","#0f766e",dibujar_icono_ciclo))
    indice=0
    while indice<len(ideas):
        titulo=ideas[indice][0]
        texto=ideas[indice][1]
        color=ideas[indice][2]
        dibujar=ideas[indice][3]
        crear_tarjeta_pequena(marco,dibujar,titulo,texto,color,fila+(indice//2),indice%2)
        indice=indice+1
    return fila+4

def llenar_contenido(marco):
    # Recibe el marco de adentro de la página.
    # Escribe el objetivo, las herramientas, el proceso y lo aprendido.
    # No devuelve nada.
    fila=0
    fila=crear_titulo(marco,"Por qué lo hice",fila)
    fila=crear_parrafo(
        marco,
        "Lo hice para practicar factorización, congruencia de triángulos y ecuaciones, y para mostrarlo en clase. Estos temas me costaban. Quería un programa que mostrara el proceso y me dejara comprobar lo que resolvía a mano.",
        fila,
    )
    fila=crear_titulo(marco,"El objetivo",fila)
    fila=crear_tarjeta_horizontal(
        marco,
        dibujar_icono_objetivo,
        "Mejorar lo que sé",
        "El objetivo es mejorar mi conocimiento en álgebra, matemáticas y geometría.",
        "#0f766e",
        fila,
    )
    fila=crear_titulo(marco,"Herramientas que usé",fila)
    fila=crear_tarjeta_horizontal(
        marco,
        dibujar_icono_python,
        "Python",
        "Es el lenguaje del programa. Sirve para leer la expresión, hacer la cuenta y mostrar el resultado.",
        "#3776ab",
        fila,
    )
    fila=crear_tarjeta_horizontal(
        marco,
        dibujar_icono_cursor,
        "Cursor",
        "Es el programa donde escribí el proyecto. Ahí ordené las carpetas y vi el código.",
        "#1d3557",
        fila,
    )
    fila=crear_tarjeta_horizontal(
        marco,
        dibujar_icono_baldor,
        "Álgebra de Baldor",
        "Es el libro que usé para estudiar los casos de factorización y los procesos de las ecuaciones.",
        "#9a3412",
        fila,
    )
    fila=crear_tarjeta_horizontal(
        marco,
        dibujar_icono_grok,
        "Inteligencia artificial, Grok 4.7",
        "Me ayudó a organizar el trabajo. El modelo es Grok 4.7. Yo revisaba el plan y comprobaba los resultados.",
        "#7c3aed",
        fila,
    )
    fila=crear_titulo(marco,"Cómo trabajé",fila)
    fila=crear_tarjeta_horizontal(
        marco,
        dibujar_icono_plan,
        "1. Primero, el plan",
        "Antes de escribir el código, armaba un plan: qué iba a hacer y en qué orden.",
        "#b45309",
        fila,
    )
    fila=crear_tarjeta_horizontal(
        marco,
        dibujar_icono_agente,
        "2. Luego, el agente",
        "Después activaba el agente. El agente escribía el código siguiendo ese plan.",
        "#1d4ed8",
        fila,
    )
    fila=crear_tarjeta_horizontal(
        marco,
        dibujar_icono_prueba,
        "3. Al final, las pruebas",
        "En el escritorio resolvía ejercicios a mano y los comparaba con lo que mostraba el programa.",
        "#15803d",
        fila,
    )
    fila=crear_tarjeta_horizontal(
        marco,
        dibujar_icono_tiempo,
        "El tiempo y la ayuda",
        "Nos demoramos aproximadamente 30 horas. Conté con la ayuda de papá.",
        "#6d28d9",
        fila,
    )
    fila=crear_titulo(marco,"Qué aprendí",fila)
    fila=poner_lo_aprendido(marco,fila)
    fila=crear_titulo(marco,"Para otros niños",fila)
    crear_tarjeta_de_github(marco,fila)
    marco.grid_columnconfigure(0,weight=1)
    marco.grid_columnconfigure(1,weight=1)

def armar_pantalla_introduccion(marco,volver):
    # Recibe el marco de la ventana y la función que vuelve al inicio.
    # Arma el título, la página con iconos y el botón para regresar.
    # No devuelve nada.
    global lienzo_introduccion
    global ventana_del_contenido

    titulo=tk.Label(
        marco,
        text="Introducción",
        font=("Segoe UI",26,"bold"),
        bg="#eef3fa",
        fg="#6d28d9",
    )
    titulo.grid(row=0,column=0,padx=16,pady=(12,0),sticky="w")

    estudiante=tk.Label(
        marco,
        text="Juan Pablo Urzola Marin  ·  Matemáticas 8C",
        font=("Segoe UI",14),
        bg="#eef3fa",
        fg="#33415c",
    )
    estudiante.grid(row=1,column=0,padx=16,pady=(0,6),sticky="w")

    lienzo_introduccion=tk.Canvas(marco,bg="#eef3fa",highlightthickness=0)
    lienzo_introduccion.grid(row=2,column=0,sticky="nsew",padx=(8,0))
    barra=tk.Scrollbar(marco,command=lienzo_introduccion.yview)
    barra.grid(row=2,column=1,sticky="ns",padx=(0,8))
    lienzo_introduccion.configure(yscrollcommand=barra.set)

    contenido=tk.Frame(lienzo_introduccion,bg="#eef3fa")
    llenar_contenido(contenido)
    ventana_del_contenido=lienzo_introduccion.create_window((0,0),window=contenido,anchor="nw")
    contenido.bind("<Configure>",al_cambiar_el_contenido)
    lienzo_introduccion.bind("<Configure>",al_cambiar_el_ancho)
    enlazar_rueda(marco)

    boton_volver=tk.Button(
        marco,
        text="Volver al inicio",
        font=("Segoe UI",14),
        bg="#ffffff",
        command=volver,
    )
    boton_volver.grid(row=3,column=0,columnspan=2,padx=16,pady=12,sticky="ew")
    marco.grid_columnconfigure(0,weight=1)
    marco.grid_rowconfigure(2,weight=1)
