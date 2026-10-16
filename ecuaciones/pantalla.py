# Pantalla de ecuaciones de primer grado.
# Primero explica los conceptos y el proceso.
# Después pide la ecuación y muestra el caso y el resultado.

import tkinter as tk
from ecuaciones.conceptos import texto_de_conceptos_y_procesos,texto_de_las_fracciones
from ecuaciones.resolver import texto_del_resultado
from ecuaciones.fracciones import texto_de_la_fraccionaria

marco_inicio=None
marco_sin_fracciones=None
marco_con_fracciones=None
marco_conceptos=None
marco_conceptos_fraccion=None
marco_resolver=None
marco_resolver_fraccion=None
al_volver_al_menu=None
cuadro_ecuacion=None
etiqueta_resultado=None
cuadro_fraccion=None
etiqueta_resultado_fraccion=None
cuadro_numerador=None
cuadro_denominador=None
cuadro_activo=None


def ocultar_pantallas():
    # No recibe datos.
    # Esconde el inicio, los conceptos y la resolución.
    # No devuelve nada.
    marco_inicio.grid_remove()
    marco_sin_fracciones.grid_remove()
    marco_con_fracciones.grid_remove()
    marco_conceptos.grid_remove()
    marco_conceptos_fraccion.grid_remove()
    marco_resolver.grid_remove()
    marco_resolver_fraccion.grid_remove()

def mostrar_inicio_ecuaciones():
    # No recibe datos.
    # Muestra el submenú: sin fracciones o con fracciones.
    # No devuelve nada.
    ocultar_pantallas()
    marco_inicio.grid(row=0,column=0,sticky="nsew")

def mostrar_menu_sin_fracciones():
    # No recibe datos.
    # Muestra la definición y el botón de resolver de las ecuaciones sin fracciones.
    # No devuelve nada.
    ocultar_pantallas()
    marco_sin_fracciones.grid(row=0,column=0,sticky="nsew")

def mostrar_menu_con_fracciones():
    # No recibe datos.
    # Muestra la definición y el botón de resolver de las ecuaciones con fracciones.
    # No devuelve nada.
    ocultar_pantallas()
    marco_con_fracciones.grid(row=0,column=0,sticky="nsew")

def mostrar_conceptos():
    # No recibe datos.
    # Muestra la definición y el proceso de las ecuaciones sin fracciones.
    # No devuelve nada.
    ocultar_pantallas()
    marco_conceptos.grid(row=0,column=0,sticky="nsew")

def mostrar_conceptos_de_fracciones():
    # No recibe datos.
    # Muestra la definición y el proceso de las ecuaciones fraccionarias.
    # No devuelve nada.
    ocultar_pantallas()
    marco_conceptos_fraccion.grid(row=0,column=0,sticky="nsew")

def mostrar_resolver():
    # No recibe datos.
    # Muestra el cuadro para escribir la ecuación sin fracciones.
    # No devuelve nada.
    ocultar_pantallas()
    marco_resolver.grid(row=0,column=0,sticky="nsew")
    cuadro_ecuacion.focus()

def mostrar_resolver_fracciones():
    # No recibe datos.
    # Muestra el cuadro para escribir la ecuación con fracciones.
    # No devuelve nada.
    ocultar_pantallas()
    marco_resolver_fraccion.grid(row=0,column=0,sticky="nsew")
    recordar_cuadro_directo(cuadro_fraccion)

def volver_al_menu():
    # No recibe datos.
    # Regresa a la pantalla donde se elige el tema.
    # No devuelve nada.
    al_volver_al_menu()

def la_resolucion_esta_visible():
    # No recibe datos.
    # Mira si se está mostrando alguna pantalla de resolver.
    # Devuelve True o False. Sirve para la tecla Enter.
    if marco_resolver!=None and marco_resolver.winfo_ismapped():
        return True
    if marco_resolver_fraccion!=None and marco_resolver_fraccion.winfo_ismapped():
        return True
    return False

def crear_boton_blanco(marco,mensaje,accion):
    # Recibe el marco, el texto y la función del clic.
    # Crea un botón blanco.
    # Devuelve el botón.
    boton=tk.Button(
        marco,
        text=mensaje,
        font=("Segoe UI",14),
        bg="#ffffff",
        activebackground="#ffedd5",
        command=accion,
    )
    return boton

def armar_inicio(marco):
    # Recibe el marco de las ecuaciones.
    # Pone el submenú: sin fracciones y con fracciones.
    # No devuelve nada.
    global marco_inicio
    marco_inicio=tk.Frame(marco,bg="#eef3fa")

    titulo=tk.Label(
        marco_inicio,
        text="Ecuaciones",
        font=("Segoe UI",22,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=0,column=0,pady=(28,8))

    ayuda=tk.Label(
        marco_inicio,
        text="Elige si la ecuación tiene fracciones o no.",
        font=("Segoe UI",14),
        bg="#eef3fa",
        fg="#33415c",
        justify="center",
    )
    ayuda.grid(row=1,column=0,pady=(0,16))

    boton_sin=tk.Button(
        marco_inicio,
        text="Sin fracciones",
        font=("Segoe UI",16,"bold"),
        bg="#b45309",
        fg="#ffffff",
        activebackground="#9a3412",
        activeforeground="#ffffff",
        command=mostrar_menu_sin_fracciones,
    )
    boton_sin.grid(row=2,column=0,padx=180,pady=8,sticky="ew")

    boton_con=tk.Button(
        marco_inicio,
        text="Con fracciones",
        font=("Segoe UI",16,"bold"),
        bg="#b45309",
        fg="#ffffff",
        activebackground="#9a3412",
        activeforeground="#ffffff",
        command=mostrar_menu_con_fracciones,
    )
    boton_con.grid(row=3,column=0,padx=180,pady=8,sticky="ew")

    boton_menu=crear_boton_blanco(marco_inicio,"Volver al inicio",volver_al_menu)
    boton_menu.grid(row=4,column=0,padx=180,pady=(16,8),sticky="ew")
    marco_inicio.grid_columnconfigure(0,weight=1)

def armar_menu_de_tipo(marco_padre,titulo_texto,al_abrir_definicion,al_abrir_resolver):
    # Recibe el marco, el título y las dos funciones de los botones.
    # Arma la definición y el resolver de un tipo de ecuación.
    # Devuelve el marco de ese submenú.
    marco=tk.Frame(marco_padre,bg="#eef3fa")

    titulo=tk.Label(
        marco,
        text=titulo_texto,
        font=("Segoe UI",22,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=0,column=0,pady=(28,8))

    boton_definicion=tk.Button(
        marco,
        text="Definición y proceso",
        font=("Segoe UI",16,"bold"),
        bg="#b45309",
        fg="#ffffff",
        activebackground="#9a3412",
        activeforeground="#ffffff",
        command=al_abrir_definicion,
    )
    boton_definicion.grid(row=1,column=0,padx=180,pady=8,sticky="ew")

    boton_resolver=tk.Button(
        marco,
        text="Resolver una ecuación",
        font=("Segoe UI",16,"bold"),
        bg="#b45309",
        fg="#ffffff",
        activebackground="#9a3412",
        activeforeground="#ffffff",
        command=al_abrir_resolver,
    )
    boton_resolver.grid(row=2,column=0,padx=180,pady=8,sticky="ew")

    boton_volver=crear_boton_blanco(marco,"Volver a ecuaciones",mostrar_inicio_ecuaciones)
    boton_volver.grid(row=3,column=0,padx=180,pady=(16,8),sticky="ew")
    marco.grid_columnconfigure(0,weight=1)
    return marco

def armar_menus_de_tipo(marco):
    # Recibe el marco de las ecuaciones.
    # Arma el submenú de sin fracciones y el de con fracciones.
    # No devuelve nada.
    global marco_sin_fracciones
    global marco_con_fracciones
    marco_sin_fracciones=armar_menu_de_tipo(
        marco,
        "Sin fracciones",
        mostrar_conceptos,
        mostrar_resolver,
    )
    marco_con_fracciones=armar_menu_de_tipo(
        marco,
        "Con fracciones",
        mostrar_conceptos_de_fracciones,
        mostrar_resolver_fracciones,
    )

def armar_conceptos(marco):
    # Recibe el marco de las ecuaciones.
    # Pone el texto de conceptos y procesos, con barra para bajar.
    # No devuelve nada.
    global marco_conceptos
    marco_conceptos=tk.Frame(marco,bg="#eef3fa")

    titulo=tk.Label(
        marco_conceptos,
        text="Definición y proceso",
        font=("Segoe UI",22,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=0,column=0,columnspan=2,padx=16,pady=(16,8),sticky="ew")

    cuadro=tk.Text(
        marco_conceptos,
        font=("Segoe UI",16),
        bg="#ffffff",
        fg="#1d3557",
        wrap="word",
        padx=16,
        pady=16,
        relief="solid",
        borderwidth=1,
    )
    cuadro.grid(row=1,column=0,padx=(16,0),pady=8,sticky="nsew")
    cuadro.insert("1.0",texto_de_conceptos_y_procesos())
    cuadro.config(state="disabled")

    barra=tk.Scrollbar(marco_conceptos,command=cuadro.yview)
    barra.grid(row=1,column=1,padx=(0,16),pady=8,sticky="ns")
    cuadro.config(yscrollcommand=barra.set)

    boton_volver=crear_boton_blanco(marco_conceptos,"Volver",mostrar_menu_sin_fracciones)
    boton_volver.grid(row=2,column=0,columnspan=2,padx=16,pady=(8,16),sticky="ew")
    marco_conceptos.grid_columnconfigure(0,weight=1)
    marco_conceptos.grid_rowconfigure(1,weight=1)

def insertar_texto(texto):
    # Recibe el texto de un botón, por ejemplo "x" o "(".
    # Lo escribe en el cuadro, en el lugar del cursor.
    # No devuelve nada.
    cuadro_ecuacion.insert(tk.INSERT,texto)
    cuadro_ecuacion.focus()

def borrar_un_caracter():
    # No recibe datos.
    # Borra el carácter que está justo antes del cursor.
    # No devuelve nada.
    posicion=cuadro_ecuacion.index(tk.INSERT)
    if posicion>0:
        cuadro_ecuacion.delete(posicion-1,posicion)
    cuadro_ecuacion.focus()

def borrar_la_ecuacion():
    # No recibe datos.
    # Deja el cuadro vacío y limpia el resultado.
    # No devuelve nada.
    cuadro_ecuacion.delete(0,tk.END)
    etiqueta_resultado.config(text="Aquí aparece el caso y el resultado.")
    cuadro_ecuacion.focus()

def mostrar_el_resultado():
    # No recibe datos.
    # Si está abierta la ecuación con fracciones, la resuelve. Si no, resuelve la otra.
    # No devuelve nada.
    if marco_resolver_fraccion!=None and marco_resolver_fraccion.winfo_ismapped():
        mostrar_resultado_fraccion()
        return
    ecuacion=cuadro_ecuacion.get()
    etiqueta_resultado.config(text=texto_del_resultado(ecuacion))

def al_pulsar_tecla(evento):
    # Recibe el clic de una tecla de la pantalla.
    # Escribe el signo o borra un carácter si es la flecha.
    # No devuelve nada.
    texto=evento.widget["text"]
    if texto=="←":
        borrar_un_caracter()
    else:
        insertar_texto(texto)

def crear_tecla(marco,texto,fila,columna,columnas=1):
    # Recibe el marco, el texto, la fila, la columna y cuántas columnas ocupa.
    # Crea la tecla y la pone en la cuadrícula.
    # Devuelve la tecla.
    boton=tk.Button(
        marco,
        text=texto,
        font=("Segoe UI",14),
        bg="#ffffff",
        activebackground="#ffedd5",
    )
    boton.grid(row=fila,column=columna,columnspan=columnas,padx=3,pady=3,sticky="nsew")
    boton.bind("<Button-1>",al_pulsar_tecla)
    return boton

def armar_teclado(marco):
    # Recibe el marco de resolver.
    # Pone números, la x, los signos de agrupación y el igual.
    # No devuelve nada.
    teclas=[
        ["1","2","3","4","5","6","7","8","9","0"],
        ["x","+","-","(",")","[","]","{","}","="],
    ]
    fila=3
    for grupo in teclas:
        columna=0
        for tecla in grupo:
            crear_tecla(marco,tecla,fila,columna)
            columna=columna+1
        fila=fila+1
    crear_tecla(marco,"←",5,0,2)

def armar_resolver(marco):
    # Recibe el marco de las ecuaciones.
    # Arma el cuadro, el teclado y el lugar del resultado.
    # No devuelve nada.
    global marco_resolver
    global cuadro_ecuacion
    global etiqueta_resultado
    marco_resolver=tk.Frame(marco,bg="#eef3fa")

    titulo=tk.Label(
        marco_resolver,
        text="Resolver una ecuación",
        font=("Segoe UI",22,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=0,column=0,columnspan=10,padx=16,pady=(16,4),sticky="ew")

    ayuda=tk.Label(
        marco_resolver,
        text="Ejemplo: 2(x+3)-4=10",
        font=("Segoe UI",14),
        bg="#eef3fa",
        fg="#33415c",
    )
    ayuda.grid(row=1,column=0,columnspan=10,padx=16,pady=(0,8),sticky="ew")

    cuadro_ecuacion=tk.Entry(
        marco_resolver,
        font=("Segoe UI",20),
        justify="center",
        bg="#ffffff",
        relief="solid",
        borderwidth=1,
    )
    cuadro_ecuacion.grid(row=2,column=0,columnspan=10,padx=16,pady=(0,8),sticky="ew")

    armar_teclado(marco_resolver)

    boton_resolver=tk.Button(
        marco_resolver,
        text="Resolver",
        font=("Segoe UI",14,"bold"),
        bg="#b45309",
        fg="#ffffff",
        activebackground="#9a3412",
        activeforeground="#ffffff",
        command=mostrar_el_resultado,
    )
    boton_resolver.grid(row=5,column=2,columnspan=4,padx=8,pady=8,sticky="ew")

    boton_borrar=tk.Button(
        marco_resolver,
        text="Borrar",
        font=("Segoe UI",14),
        bg="#f8d7da",
        command=borrar_la_ecuacion,
    )
    boton_borrar.grid(row=5,column=6,columnspan=4,padx=8,pady=8,sticky="ew")

    etiqueta_resultado=tk.Label(
        marco_resolver,
        text="Aquí aparece el caso y el resultado.",
        font=("Segoe UI",16),
        bg="#ffffff",
        fg="#1d3557",
        justify="left",
        anchor="nw",
        padx=12,
        pady=12,
        wraplength=920,
    )
    etiqueta_resultado.grid(row=6,column=0,columnspan=10,padx=16,pady=(0,8),sticky="nsew")

    boton_volver=crear_boton_blanco(marco_resolver,"Volver",mostrar_menu_sin_fracciones)
    boton_volver.grid(row=7,column=0,columnspan=10,padx=16,pady=(0,12),sticky="ew")

    columna=0
    while columna<10:
        marco_resolver.grid_columnconfigure(columna,weight=1)
        columna=columna+1
    marco_resolver.grid_rowconfigure(6,weight=1,minsize=160)

def armar_conceptos_de_fracciones(marco):
    # Recibe el marco de las ecuaciones.
    # Pone la definición y el proceso de las fracciones, con barra para bajar.
    # No devuelve nada.
    global marco_conceptos_fraccion
    marco_conceptos_fraccion=tk.Frame(marco,bg="#eef3fa")

    titulo=tk.Label(
        marco_conceptos_fraccion,
        text="Definición y proceso",
        font=("Segoe UI",22,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=0,column=0,columnspan=2,padx=16,pady=(16,8),sticky="ew")

    cuadro=tk.Text(
        marco_conceptos_fraccion,
        font=("Segoe UI",16),
        bg="#ffffff",
        fg="#1d3557",
        wrap="word",
        padx=16,
        pady=16,
        relief="solid",
        borderwidth=1,
    )
    cuadro.grid(row=1,column=0,padx=(16,0),pady=8,sticky="nsew")
    cuadro.insert("1.0",texto_de_las_fracciones())
    cuadro.config(state="disabled")

    barra=tk.Scrollbar(marco_conceptos_fraccion,command=cuadro.yview)
    barra.grid(row=1,column=1,padx=(0,16),pady=8,sticky="ns")
    cuadro.config(yscrollcommand=barra.set)

    boton_volver=crear_boton_blanco(marco_conceptos_fraccion,"Volver",mostrar_menu_con_fracciones)
    boton_volver.grid(row=2,column=0,columnspan=2,padx=16,pady=(8,16),sticky="ew")
    marco_conceptos_fraccion.grid_columnconfigure(0,weight=1)
    marco_conceptos_fraccion.grid_rowconfigure(1,weight=1)

def recordar_cuadro(evento):
    # Recibe el clic o el foco de un cuadro.
    # Recuerda si se está escribiendo la ecuación, el numerador o el denominador.
    # No devuelve nada.
    global cuadro_activo
    cuadro_activo=evento.widget

def cuadro_donde_se_escribe():
    # No recibe datos.
    # Elige el cuadro que el estudiante tocó por última vez.
    # Devuelve ese cuadro. Si todavía no tocó ninguno, devuelve la ecuación.
    if cuadro_activo==cuadro_numerador:
        return cuadro_numerador
    if cuadro_activo==cuadro_denominador:
        return cuadro_denominador
    if cuadro_activo==cuadro_fraccion:
        return cuadro_fraccion
    return cuadro_fraccion

def insertar_en_la_fraccion(texto):
    # Recibe el texto de una tecla, por ejemplo "2" o "x".
    # Lo escribe en el cuadro activo: numerador, denominador o ecuación.
    # No devuelve nada.
    cuadro=cuadro_donde_se_escribe()
    cuadro.insert(tk.INSERT,texto)
    cuadro.focus()

def borrar_un_caracter_fraccion():
    # No recibe datos.
    # Borra el carácter anterior en el cuadro activo, no en otro.
    # No devuelve nada.
    cuadro=cuadro_donde_se_escribe()
    posicion=cuadro.index(tk.INSERT)
    if posicion>0:
        cuadro.delete(posicion-1,posicion)
    cuadro.focus()

def borrar_la_fraccion():
    # No recibe datos.
    # Deja vacíos la ecuación, el numerador y el denominador.
    # No devuelve nada.
    cuadro_fraccion.delete(0,tk.END)
    cuadro_numerador.delete(0,tk.END)
    cuadro_denominador.delete(0,tk.END)
    etiqueta_resultado_fraccion.config(text="Aquí aparece el caso y el resultado.")
    recordar_cuadro_directo(cuadro_fraccion)

def mostrar_resultado_fraccion():
    # No recibe datos.
    # Lee la ecuación con fracciones y muestra el caso y el resultado.
    # No devuelve nada.
    ecuacion=cuadro_fraccion.get()
    etiqueta_resultado_fraccion.config(text=texto_de_la_fraccionaria(ecuacion))

def agregar_fraccion():
    # No recibe datos.
    # Lee el numerador y el denominador y los escribe en la ecuación.
    # No devuelve nada. Ejemplo: numerador x+1 y denominador 2x queda (x+1)/(2x).
    numerador=cuadro_numerador.get().replace(" ","")
    denominador=cuadro_denominador.get().replace(" ","")
    if numerador=="" or denominador=="":
        etiqueta_resultado_fraccion.config(text="Escribe el numerador y el denominador.")
        return
    texto="("+numerador+")/("+denominador+")"
    cuadro_fraccion.insert(tk.INSERT,texto)
    cuadro_numerador.delete(0,tk.END)
    cuadro_denominador.delete(0,tk.END)
    recordar_cuadro_directo(cuadro_fraccion)

def recordar_cuadro_directo(cuadro):
    # Recibe el cuadro en el que se sigue escribiendo.
    # Lo deja activo y con el cursor.
    # No devuelve nada.
    global cuadro_activo
    cuadro_activo=cuadro
    cuadro.focus()

def al_pulsar_tecla_fraccion(evento):
    # Recibe el clic de una tecla de la pantalla de fracciones.
    # Escribe el signo o borra un carácter si es la flecha.
    # No devuelve nada.
    texto=evento.widget["text"]
    if texto=="←":
        borrar_un_caracter_fraccion()
    else:
        insertar_en_la_fraccion(texto)

def crear_tecla_fraccion(marco,texto,fila,columna,columnas=1):
    # Recibe el marco, el texto, la fila, la columna y cuántas columnas ocupa.
    # Crea la tecla de la pantalla de fracciones.
    # Devuelve la tecla.
    boton=tk.Button(
        marco,
        text=texto,
        font=("Segoe UI",14),
        bg="#ffffff",
        activebackground="#ffedd5",
    )
    boton.grid(row=fila,column=columna,columnspan=columnas,padx=3,pady=3,sticky="nsew")
    boton.bind("<Button-1>",al_pulsar_tecla_fraccion)
    return boton

def armar_teclado_fraccion(marco):
    # Recibe el marco de resolver fracciones.
    # Pone números, la x, la barra de fracción, los signos y el igual.
    # No devuelve nada.
    teclas=[
        ["1","2","3","4","5","6","7","8","9","0"],
        ["x","+","-","(",")","[","]","{","}","/"],
    ]
    fila=4
    for grupo in teclas:
        columna=0
        for tecla in grupo:
            crear_tecla_fraccion(marco,tecla,fila,columna)
            columna=columna+1
        fila=fila+1
    crear_tecla_fraccion(marco,"=",6,0,2)
    crear_tecla_fraccion(marco,"←",6,2,2)

def armar_resolver_fracciones(marco):
    # Recibe el marco de las ecuaciones.
    # Arma la ecuación, los cuadros de la fracción, el teclado y el resultado.
    # No devuelve nada.
    global marco_resolver_fraccion
    global cuadro_fraccion
    global etiqueta_resultado_fraccion
    global cuadro_numerador
    global cuadro_denominador
    marco_resolver_fraccion=tk.Frame(marco,bg="#eef3fa")

    titulo=tk.Label(
        marco_resolver_fraccion,
        text="Resolver una ecuación con fracciones",
        font=("Segoe UI",22,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=0,column=0,columnspan=10,padx=16,pady=(12,4),sticky="ew")

    ayuda=tk.Label(
        marco_resolver_fraccion,
        text="Ejemplo: x/2+1/3=5/6. Si ya hay un término, pon + o - antes de agregar otra fracción.",
        font=("Segoe UI",13),
        bg="#eef3fa",
        fg="#33415c",
    )
    ayuda.grid(row=1,column=0,columnspan=10,padx=16,pady=(0,6),sticky="ew")

    cuadro_fraccion=tk.Entry(
        marco_resolver_fraccion,
        font=("Segoe UI",20),
        justify="center",
        bg="#ffffff",
        relief="solid",
        borderwidth=1,
    )
    cuadro_fraccion.grid(row=2,column=0,columnspan=10,padx=16,pady=(0,6),sticky="ew")
    cuadro_fraccion.bind("<FocusIn>",recordar_cuadro)

    caja=tk.Frame(marco_resolver_fraccion,bg="#ffffff",highlightbackground="#cbd5e1",highlightthickness=1)
    caja.grid(row=3,column=0,columnspan=10,padx=280,pady=(0,8),sticky="ew")

    etiqueta_numerador=tk.Label(
        caja,
        text="Numerador",
        font=("Segoe UI",13),
        bg="#ffffff",
        fg="#1d3557",
    )
    etiqueta_numerador.grid(row=0,column=0,padx=12,pady=(8,0))

    cuadro_numerador=tk.Entry(
        caja,
        font=("Segoe UI",18),
        justify="center",
        bg="#ffffff",
        relief="solid",
        borderwidth=1,
    )
    cuadro_numerador.grid(row=1,column=0,padx=24,pady=(4,6),sticky="ew")
    cuadro_numerador.bind("<FocusIn>",recordar_cuadro)

    linea=tk.Frame(caja,bg="#1d3557",height=3)
    linea.grid(row=2,column=0,padx=24,pady=4,sticky="ew")

    etiqueta_denominador=tk.Label(
        caja,
        text="Denominador",
        font=("Segoe UI",13),
        bg="#ffffff",
        fg="#1d3557",
    )
    etiqueta_denominador.grid(row=3,column=0,padx=12)

    cuadro_denominador=tk.Entry(
        caja,
        font=("Segoe UI",18),
        justify="center",
        bg="#ffffff",
        relief="solid",
        borderwidth=1,
    )
    cuadro_denominador.grid(row=4,column=0,padx=24,pady=(4,8),sticky="ew")
    cuadro_denominador.bind("<FocusIn>",recordar_cuadro)

    boton_agregar=tk.Button(
        caja,
        text="Agregar fracción",
        font=("Segoe UI",13,"bold"),
        bg="#b45309",
        fg="#ffffff",
        activebackground="#9a3412",
        activeforeground="#ffffff",
        command=agregar_fraccion,
    )
    boton_agregar.grid(row=5,column=0,padx=24,pady=(0,10),sticky="ew")
    caja.grid_columnconfigure(0,weight=1)

    armar_teclado_fraccion(marco_resolver_fraccion)

    boton_resolver=tk.Button(
        marco_resolver_fraccion,
        text="Resolver",
        font=("Segoe UI",14,"bold"),
        bg="#b45309",
        fg="#ffffff",
        activebackground="#9a3412",
        activeforeground="#ffffff",
        command=mostrar_resultado_fraccion,
    )
    boton_resolver.grid(row=6,column=4,columnspan=3,padx=8,pady=8,sticky="ew")

    boton_borrar=tk.Button(
        marco_resolver_fraccion,
        text="Borrar",
        font=("Segoe UI",14),
        bg="#f8d7da",
        command=borrar_la_fraccion,
    )
    boton_borrar.grid(row=6,column=7,columnspan=3,padx=8,pady=8,sticky="ew")

    etiqueta_resultado_fraccion=tk.Label(
        marco_resolver_fraccion,
        text="Aquí aparece el caso y el resultado.",
        font=("Segoe UI",16),
        bg="#ffffff",
        fg="#1d3557",
        justify="left",
        anchor="nw",
        padx=12,
        pady=12,
        wraplength=920,
    )
    etiqueta_resultado_fraccion.grid(row=7,column=0,columnspan=10,padx=16,pady=(0,8),sticky="nsew")

    boton_volver=crear_boton_blanco(marco_resolver_fraccion,"Volver",mostrar_menu_con_fracciones)
    boton_volver.grid(row=8,column=0,columnspan=10,padx=16,pady=(0,12),sticky="ew")

    columna=0
    while columna<10:
        marco_resolver_fraccion.grid_columnconfigure(columna,weight=1)
        columna=columna+1
    marco_resolver_fraccion.grid_rowconfigure(7,weight=1,minsize=100)

def armar_pantalla_ecuaciones(marco,volver):
    # Recibe el marco de la ventana y la función que vuelve al inicio.
    # Arma el submenú, las dos definiciones y las dos pantallas de resolver.
    # No devuelve nada.
    global al_volver_al_menu
    al_volver_al_menu=volver
    marco.grid_columnconfigure(0,weight=1)
    marco.grid_rowconfigure(0,weight=1)
    armar_inicio(marco)
    armar_menus_de_tipo(marco)
    armar_conceptos(marco)
    armar_conceptos_de_fracciones(marco)
    armar_resolver(marco)
    armar_resolver_fracciones(marco)
    mostrar_inicio_ecuaciones()
