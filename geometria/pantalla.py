# Pantalla de congruencia de triángulos.
# Primero explica los conceptos.
# Después deja marcar lados y ángulos con clics y arma la tabla.

import tkinter as tk
from geometria.conceptos import lista_de_conceptos, buscar_concepto
from geometria.criterios import filas_de_la_comprobacion, texto_del_resultado
from geometria.dibujos import dibujar_concepto, dibujar_dos_triangulos, dibujar_marcas, dibujar_parte_resaltada, parte_bajo_el_clic

marco_inicio=None
marco_lista=None
marco_concepto=None
marco_comparar=None
al_volver_al_menu=None
lienzo_concepto=None
titulo_concepto=None
texto_concepto=None
lienzo_comparar=None
etiqueta_aviso=None
etiqueta_resultado=None
marco_filas=None
marco_razones=None
marcas=[]
parte_elegida=None
par_pendiente=None
aviso="Haz clic en un lado o en la letra de un ángulo."


def ocultar_pantallas():
    # No recibe datos.
    # Esconde el inicio, los conceptos y la comparación.
    # No devuelve nada.
    marco_inicio.grid_remove()
    marco_lista.grid_remove()
    marco_concepto.grid_remove()
    marco_comparar.grid_remove()

def mostrar_inicio_geometria():
    # No recibe datos.
    # Muestra los dos caminos: leer conceptos o comparar triángulos.
    # No devuelve nada.
    ocultar_pantallas()
    marco_inicio.grid(row=0, column=0, sticky="nsew")

def mostrar_lista_de_conceptos():
    # No recibe datos.
    # Muestra un botón por cada concepto.
    # No devuelve nada.
    ocultar_pantallas()
    marco_lista.grid(row=0, column=0, sticky="nsew")

def mostrar_un_concepto(nombre):
    # Recibe el nombre, por ejemplo "Bisectriz".
    # Escribe el párrafo y dibuja el esquema de ese concepto.
    # No devuelve nada.
    concepto=buscar_concepto(nombre)
    if concepto==None:
        return
    titulo_concepto.config(text=concepto["nombre"])
    texto_concepto.config(text=concepto["texto"])
    ocultar_pantallas()
    marco_concepto.grid(row=0, column=0, sticky="nsew")
    lienzo_concepto.update()
    dibujar_concepto(lienzo_concepto, concepto["dibujo"])

def mostrar_comparar():
    # No recibe datos.
    # Muestra los dos triángulos, la tabla y las marcas que ya había.
    # No devuelve nada.
    ocultar_pantallas()
    marco_comparar.grid(row=0, column=0, sticky="nsew")
    actualizar_comparacion()

def al_abrir_concepto(evento):
    # Recibe el clic de un concepto.
    # Abre el texto y el dibujo de ese concepto.
    # No devuelve nada.
    mostrar_un_concepto(evento.widget["text"])

def volver_al_menu():
    # No recibe datos.
    # Regresa a la pantalla principal de factorización.
    # No devuelve nada.
    al_volver_al_menu()

def crear_boton_blanco(marco, mensaje, accion):
    # Recibe el marco, el texto y la función que se ejecuta al hacer clic.
    # Crea un botón blanco, del mismo estilo que el menú.
    # Devuelve el botón.
    boton=tk.Button(
        marco,
        text=mensaje,
        font=("Segoe UI", 14),
        bg="#ffffff",
        activebackground="#d9e6fb",
        command=accion,
    )
    return boton

def crear_boton_de_concepto(marco, nombre, fila, columna):
    # Recibe el marco, el nombre del concepto, la fila y la columna.
    # Crea el botón que abre ese concepto.
    # Devuelve el botón.
    boton=tk.Button(
        marco,
        text=nombre,
        font=("Segoe UI", 13),
        bg="#ffffff",
        activebackground="#d9e6fb",
        wraplength=420,
        justify="center",
    )
    boton.grid(row=fila, column=columna, padx=8, pady=6, sticky="nsew")
    boton.bind("<Button-1>", al_abrir_concepto)
    return boton

def armar_inicio(marco):
    # Recibe el marco de la geometría.
    # Pone el título y los botones de conceptos y de comparar.
    # No devuelve nada.
    global marco_inicio
    marco_inicio=tk.Frame(marco, bg="#eef3fa")

    titulo=tk.Label(
        marco_inicio,
        text="Congruencia de triángulos",
        font=("Segoe UI", 22, "bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=0, column=0, pady=(28, 8))

    ayuda=tk.Label(
        marco_inicio,
        text="Puedes leer cada concepto o comparar △ABC con △DEF.\nLa tabla de la comparación usa afirmación y razón, como en el examen.",
        font=("Segoe UI", 14),
        bg="#eef3fa",
        fg="#33415c",
        justify="center",
    )
    ayuda.grid(row=1, column=0, pady=(0, 16))

    boton_conceptos=tk.Button(
        marco_inicio,
        text="Conceptos",
        font=("Segoe UI", 16, "bold"),
        bg="#2f6fed",
        fg="#ffffff",
        activebackground="#1d4ed8",
        activeforeground="#ffffff",
        command=mostrar_lista_de_conceptos,
    )
    boton_conceptos.grid(row=2, column=0, padx=180, pady=8, sticky="ew")

    boton_comparar=tk.Button(
        marco_inicio,
        text="Comparar dos triángulos",
        font=("Segoe UI", 16, "bold"),
        bg="#0f766e",
        fg="#ffffff",
        activebackground="#115e59",
        activeforeground="#ffffff",
        command=mostrar_comparar,
    )
    boton_comparar.grid(row=3, column=0, padx=180, pady=8, sticky="ew")

    boton_menu=crear_boton_blanco(marco_inicio, "Volver al menú", volver_al_menu)
    boton_menu.grid(row=4, column=0, padx=180, pady=(16, 8), sticky="ew")
    marco_inicio.grid_columnconfigure(0, weight=1)

def armar_lista(marco):
    # Recibe el marco de la geometría.
    # Pone un botón por cada concepto y el regreso al inicio.
    # No devuelve nada.
    global marco_lista
    marco_lista=tk.Frame(marco, bg="#eef3fa")

    titulo=tk.Label(
        marco_lista,
        text="Conceptos",
        font=("Segoe UI", 22, "bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=0, column=0, columnspan=2, pady=(12, 8))

    conceptos=lista_de_conceptos()
    indice=0
    for concepto in conceptos:
        fila=1+(indice//2)
        columna=indice%2
        crear_boton_de_concepto(marco_lista, concepto["nombre"], fila, columna)
        indice=indice+1

    boton_comparar=crear_boton_blanco(marco_lista, "Comparar dos triángulos", mostrar_comparar)
    boton_comparar.grid(row=9, column=0, padx=8, pady=(8, 4), sticky="ew")

    boton_inicio=crear_boton_blanco(marco_lista, "Volver", mostrar_inicio_geometria)
    boton_inicio.grid(row=9, column=1, padx=8, pady=(8, 4), sticky="ew")

    boton_menu=crear_boton_blanco(marco_lista, "Volver al menú", volver_al_menu)
    boton_menu.grid(row=10, column=0, columnspan=2, padx=8, pady=(4, 12), sticky="ew")

    marco_lista.grid_columnconfigure(0, weight=1)
    marco_lista.grid_columnconfigure(1, weight=1)

def armar_concepto(marco):
    # Recibe el marco de la geometría.
    # Prepara el título, el dibujo y el párrafo de un concepto.
    # No devuelve nada.
    global marco_concepto
    global titulo_concepto
    global lienzo_concepto
    global texto_concepto
    marco_concepto=tk.Frame(marco, bg="#eef3fa")

    titulo_concepto=tk.Label(
        marco_concepto,
        text="",
        font=("Segoe UI", 22, "bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo_concepto.grid(row=0, column=0, pady=(12, 8))

    lienzo_concepto=tk.Canvas(
        marco_concepto,
        width=560,
        height=230,
        bg="#ffffff",
        highlightthickness=1,
        highlightbackground="#cbd5e1",
    )
    lienzo_concepto.grid(row=1, column=0, pady=4)

    texto_concepto=tk.Label(
        marco_concepto,
        text="",
        font=("Segoe UI", 15),
        bg="#ffffff",
        fg="#1d3557",
        justify="left",
        anchor="nw",
        padx=16,
        pady=12,
        wraplength=900,
    )
    texto_concepto.grid(row=2, column=0, padx=16, pady=8, sticky="nsew")

    boton_lista=crear_boton_blanco(marco_concepto, "Volver a los conceptos", mostrar_lista_de_conceptos)
    boton_lista.grid(row=3, column=0, padx=16, pady=(4, 12), sticky="ew")

    marco_concepto.grid_columnconfigure(0, weight=1)

def tamano_usado():
    # No recibe datos.
    # Lee el tamaño real del lienzo de la comparación.
    # Devuelve el ancho y el alto. Si todavía no se ve, usa 940 por 280.
    ancho=lienzo_comparar.winfo_width()
    alto=lienzo_comparar.winfo_height()
    if ancho<50:
        ancho=940
    if alto<50:
        alto=280
    return ancho, alto

def redibujar_comparacion():
    # No recibe datos.
    # Vuelve a dibujar los dos triángulos, las marcas y la parte elegida.
    # No devuelve nada.
    ancho, alto=tamano_usado()
    lienzo_comparar.delete("all")
    dibujar_dos_triangulos(lienzo_comparar, ancho, alto)
    dibujar_marcas(lienzo_comparar, ancho, alto, marcas)
    if par_pendiente!=None:
        parte_abc={}
        parte_abc["triangulo"]="ABC"
        parte_abc["tipo"]=par_pendiente["tipo"]
        parte_abc["nombre"]=par_pendiente["parte_abc"]
        parte_def={}
        parte_def["triangulo"]="DEF"
        parte_def["tipo"]=par_pendiente["tipo"]
        parte_def["nombre"]=par_pendiente["parte_def"]
        dibujar_parte_resaltada(lienzo_comparar, ancho, alto, parte_abc, "#2f6fed")
        dibujar_parte_resaltada(lienzo_comparar, ancho, alto, parte_def, "#2f6fed")
    elif parte_elegida!=None:
        dibujar_parte_resaltada(lienzo_comparar, ancho, alto, parte_elegida, "#2f6fed")

def crear_celda(fila, columna, mensaje, es_encabezado, es_conclusion):
    # Recibe la fila, la columna, el texto y si es título o conclusión.
    # Escribe una celda de la tabla de comprobación.
    # No devuelve nada.
    fondo="#ffffff"
    color="#1d3557"
    letra=("Segoe UI", 14)
    if es_encabezado:
        fondo="#1d3557"
        color="#ffffff"
        letra=("Segoe UI", 14, "bold")
    if es_conclusion:
        fondo="#d8f3dc"
        letra=("Segoe UI", 14, "bold")
    celda=tk.Label(
        marco_filas,
        text=mensaje,
        font=letra,
        bg=fondo,
        fg=color,
        anchor="w",
        padx=12,
        pady=6,
        relief="solid",
        borderwidth=1,
    )
    celda.grid(row=fila, column=columna, sticky="nsew")

def llenar_tabla():
    # No recibe datos.
    # Borra la tabla y la vuelve a escribir con las marcas y el criterio.
    # No devuelve nada.
    hijos=marco_filas.winfo_children()
    for hijo in hijos:
        hijo.destroy()
    crear_celda(0, 0, "Afirmación", True, False)
    crear_celda(0, 1, "Razón", True, False)
    filas=filas_de_la_comprobacion(marcas)
    numero=1
    for fila in filas:
        es_conclusion=fila[0]=="△ABC ≅ △DEF"
        crear_celda(numero, 0, fila[0], False, es_conclusion)
        crear_celda(numero, 1, fila[1], False, es_conclusion)
        numero=numero+1
    marco_filas.grid_columnconfigure(0, weight=1)
    marco_filas.grid_columnconfigure(1, weight=1)

def actualizar_comparacion():
    # No recibe datos.
    # Redibuja, llena la tabla y escribe el aviso y el resultado.
    # No devuelve nada.
    redibujar_comparacion()
    llenar_tabla()
    etiqueta_aviso.config(text=aviso)
    etiqueta_resultado.config(text=texto_del_resultado(marcas))

def al_cambiar_tamano_del_lienzo(evento):
    # Recibe el aviso de que el lienzo cambió de tamaño.
    # Vuelve a dibujar los triángulos para que sigan centrados.
    # No devuelve nada.
    if evento.widget!=lienzo_comparar:
        return
    redibujar_comparacion()

def mostrar_razones():
    # No recibe datos.
    # Muestra los botones para elegir la razón de la marca.
    # No devuelve nada.
    marco_razones.grid(row=2, column=0, sticky="ew", pady=(0, 4))

def ocultar_razones():
    # No recibe datos.
    # Esconde los botones de razón hasta que haya un par elegido.
    # No devuelve nada.
    marco_razones.grid_remove()

def guardar_par_pendiente(primera, segunda):
    # Recibe las dos partes elegidas, una de cada triángulo.
    # Las ordena para que una sea de ABC y la otra de DEF.
    # No devuelve nada. Deja el par listo para la razón.
    global par_pendiente
    if primera["triangulo"]=="ABC":
        parte_abc=primera["nombre"]
        parte_def=segunda["nombre"]
    else:
        parte_abc=segunda["nombre"]
        parte_def=primera["nombre"]
    par_pendiente={}
    par_pendiente["tipo"]=primera["tipo"]
    par_pendiente["parte_abc"]=parte_abc
    par_pendiente["parte_def"]=parte_def

def indice_de_la_marca(par):
    # Recibe un par de partes, por ejemplo AB con DE.
    # Busca si ese par ya está en la tabla.
    # Devuelve la posición. Si no está, devuelve -1.
    indice=0
    for marca in marcas:
        mismo_tipo=marca["tipo"]==par["tipo"]
        mismo_abc=marca["parte_abc"]==par["parte_abc"]
        mismo_def=marca["parte_def"]==par["parte_def"]
        if mismo_tipo and mismo_abc and mismo_def:
            return indice
        indice=indice+1
    return -1

def procesar_clic(x, y):
    # Recibe las coordenadas del clic en el lienzo.
    # Elige la primera parte o completa el par con la segunda.
    # No devuelve nada. Si el par está listo, pide la razón.
    global parte_elegida
    global par_pendiente
    global aviso
    if par_pendiente!=None:
        par_pendiente=None
        parte_elegida=None
        ocultar_razones()
    ancho, alto=tamano_usado()
    parte=parte_bajo_el_clic(x, y, ancho, alto)
    if parte==None:
        aviso="Haz clic sobre la línea de un lado o sobre la letra de un ángulo."
        actualizar_comparacion()
        return
    if parte_elegida==None:
        parte_elegida=parte
        aviso="Ahora elige una parte del mismo tipo en el otro triángulo."
        actualizar_comparacion()
        return
    if parte["triangulo"]==parte_elegida["triangulo"]:
        parte_elegida=parte
        aviso="Esa parte es del mismo triángulo. Elige una parte del otro."
        actualizar_comparacion()
        return
    if parte["tipo"]!=parte_elegida["tipo"]:
        aviso="Un lado se compara con un lado y un ángulo con un ángulo."
        actualizar_comparacion()
        return
    guardar_par_pendiente(parte_elegida, parte)
    aviso="Elige la razón de esta congruencia."
    mostrar_razones()
    actualizar_comparacion()

def al_hacer_clic_en_el_lienzo(evento):
    # Recibe el clic del ratón sobre el lienzo.
    # Lo pasa a la función que elige la parte.
    # No devuelve nada.
    procesar_clic(evento.x, evento.y)

def confirmar_razon(razon):
    # Recibe la razón elegida, por ejemplo "Dado".
    # Agrega la fila o cambia la razón si ese par ya estaba.
    # No devuelve nada.
    global marcas
    global parte_elegida
    global par_pendiente
    global aviso
    if par_pendiente==None:
        return
    indice=indice_de_la_marca(par_pendiente)
    if indice>=0:
        marcas[indice]["razon"]=razon
        aviso="Se cambió la razón de esa marca."
    else:
        marca={}
        marca["tipo"]=par_pendiente["tipo"]
        marca["parte_abc"]=par_pendiente["parte_abc"]
        marca["parte_def"]=par_pendiente["parte_def"]
        marca["razon"]=razon
        marcas.append(marca)
        aviso="Marca agregada. Puedes elegir otro par."
    par_pendiente=None
    parte_elegida=None
    ocultar_razones()
    actualizar_comparacion()

def al_elegir_razon(evento):
    # Recibe el clic de un botón de razón.
    # Usa el texto del botón como razón de la marca.
    # No devuelve nada.
    confirmar_razon(evento.widget["text"])

def quitar_ultima_marca():
    # No recibe datos.
    # Quita la última fila de la tabla y cancela la selección.
    # No devuelve nada.
    global marcas
    global parte_elegida
    global par_pendiente
    global aviso
    par_pendiente=None
    parte_elegida=None
    ocultar_razones()
    if len(marcas)==0:
        aviso="No hay marcas para quitar."
        actualizar_comparacion()
        return
    del marcas[len(marcas)-1]
    aviso="Se quitó la última marca."
    actualizar_comparacion()

def borrar_marcas():
    # No recibe datos.
    # Deja la comparación sin marcas y sin selección.
    # No devuelve nada.
    global marcas
    global parte_elegida
    global par_pendiente
    global aviso
    marcas=[]
    parte_elegida=None
    par_pendiente=None
    aviso="Se borraron las marcas."
    ocultar_razones()
    actualizar_comparacion()

def crear_boton_de_razon(marco, mensaje, fila, columna):
    # Recibe el marco, el nombre de la razón, la fila y la columna.
    # Crea el botón que guarda esa razón en la tabla.
    # Devuelve el botón.
    boton=tk.Button(
        marco,
        text=mensaje,
        font=("Segoe UI", 12),
        bg="#ffffff",
        activebackground="#d9e6fb",
        wraplength=180,
        justify="center",
    )
    boton.grid(row=fila, column=columna, padx=4, pady=4, sticky="nsew")
    boton.bind("<Button-1>", al_elegir_razon)
    return boton

def armar_razones(marco):
    # Recibe el marco de las razones.
    # Pone un botón por cada razón que se usa en la tabla.
    # No devuelve nada.
    razones=[
        ["Dado", "Bisectriz"],
        ["Punto medio", "Lado común"],
        ["Propiedad reflexiva", "Perpendicular"],
        ["Ángulos opuestos por el vértice"],
    ]
    fila=0
    for grupo in razones:
        columna=0
        for razon in grupo:
            boton=crear_boton_de_razon(marco, razon, fila, columna)
            if len(grupo)==1:
                boton.grid(columnspan=2)
            columna=columna+1
        fila=fila+1
    columna=0
    while columna<2:
        marco.grid_columnconfigure(columna, weight=1)
        columna=columna+1

def armar_comparar(marco):
    # Recibe el marco de la geometría.
    # Arma el lienzo, los botones de razón, la tabla y el resultado.
    # No devuelve nada.
    global marco_comparar
    global lienzo_comparar
    global etiqueta_aviso
    global etiqueta_resultado
    global marco_filas
    global marco_razones
    marco_comparar=tk.Frame(marco, bg="#eef3fa")

    titulo=tk.Label(
        marco_comparar,
        text="Comparar △ABC y △DEF",
        font=("Segoe UI", 20, "bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=0, column=0, pady=(8, 2))

    barra=tk.Frame(marco_comparar, bg="#eef3fa")
    barra.grid(row=1, column=0, sticky="ew", padx=16)
    boton_conceptos=crear_boton_blanco(barra, "Conceptos", mostrar_lista_de_conceptos)
    boton_conceptos.grid(row=0, column=0, padx=(0, 8), sticky="w")
    boton_inicio=crear_boton_blanco(barra, "Inicio", mostrar_inicio_geometria)
    boton_inicio.grid(row=0, column=1, padx=(0, 8), sticky="w")
    boton_menu=crear_boton_blanco(barra, "Volver al menú", volver_al_menu)
    boton_menu.grid(row=0, column=3, sticky="e")
    barra.grid_columnconfigure(2, weight=1)

    ayuda=tk.Label(
        marco_comparar,
        text="1. Clic en un lado o en la letra de un ángulo.  2. Clic en una parte del mismo tipo en el otro triángulo.  3. Elige la razón.",
        font=("Segoe UI", 12),
        bg="#eef3fa",
        fg="#33415c",
    )
    ayuda.grid(row=2, column=0, padx=16, pady=(4, 2), sticky="ew")

    zona=tk.Frame(marco_comparar, bg="#eef3fa")
    zona.grid(row=3, column=0, padx=16, pady=(0, 10), sticky="nsew")

    lienzo_comparar=tk.Canvas(
        zona,
        height=420,
        bg="#ffffff",
        highlightthickness=1,
        highlightbackground="#cbd5e1",
    )
    lienzo_comparar.grid(row=0, column=0, padx=(0, 12), sticky="nsew")
    lienzo_comparar.bind("<Button-1>", al_hacer_clic_en_el_lienzo)
    lienzo_comparar.bind("<Configure>", al_cambiar_tamano_del_lienzo)

    panel=tk.Frame(zona, bg="#eef3fa")
    panel.grid(row=0, column=1, sticky="nsew")

    nota=tk.Label(
        panel,
        text="El dibujo es un esquema. La congruencia se decide por las marcas y el criterio, no por el tamaño en la pantalla. Correspondencia: A con D, B con E y C con F.",
        font=("Segoe UI", 11),
        bg="#eef3fa",
        fg="#33415c",
        wraplength=460,
        justify="left",
    )
    nota.grid(row=0, column=0, sticky="ew")

    etiqueta_aviso=tk.Label(
        panel,
        text=aviso,
        font=("Segoe UI", 13, "bold"),
        bg="#eef3fa",
        fg="#1d3557",
        anchor="w",
        wraplength=460,
        justify="left",
    )
    etiqueta_aviso.grid(row=1, column=0, pady=(6, 4), sticky="ew")

    marco_razones=tk.Frame(panel, bg="#eef3fa")
    armar_razones(marco_razones)

    marco_filas=tk.Frame(panel, bg="#eef3fa")
    marco_filas.grid(row=3, column=0, pady=(4, 4), sticky="ew")

    etiqueta_resultado=tk.Label(
        panel,
        text="",
        font=("Segoe UI", 13),
        bg="#ffffff",
        fg="#1d3557",
        justify="left",
        anchor="nw",
        padx=12,
        pady=8,
        wraplength=460,
    )
    etiqueta_resultado.grid(row=4, column=0, pady=(0, 6), sticky="ew")

    acciones=tk.Frame(panel, bg="#eef3fa")
    acciones.grid(row=5, column=0, pady=(0, 4), sticky="ew")
    boton_quitar=tk.Button(
        acciones,
        text="Quitar última marca",
        font=("Segoe UI", 13),
        bg="#ffffff",
        command=quitar_ultima_marca,
    )
    boton_quitar.grid(row=0, column=0, padx=(0, 6), sticky="ew")
    boton_borrar=tk.Button(
        acciones,
        text="Borrar todo",
        font=("Segoe UI", 13),
        bg="#f8d7da",
        command=borrar_marcas,
    )
    boton_borrar.grid(row=0, column=1, padx=(6, 0), sticky="ew")
    acciones.grid_columnconfigure(0, weight=1)
    acciones.grid_columnconfigure(1, weight=1)

    marco_comparar.grid_columnconfigure(0, weight=1)
    marco_comparar.grid_rowconfigure(3, weight=1)
    zona.grid_columnconfigure(0, weight=3)
    zona.grid_columnconfigure(1, weight=2, minsize=420)
    zona.grid_rowconfigure(0, weight=1)
    panel.grid_columnconfigure(0, weight=1)

def armar_pantalla_geometria(marco, volver):
    # Recibe el marco de la ventana y la función que vuelve al menú.
    # Arma el inicio, los conceptos y la comparación.
    # No devuelve nada.
    global al_volver_al_menu
    al_volver_al_menu=volver
    marco.grid_columnconfigure(0, weight=1)
    marco.grid_rowconfigure(0, weight=1)
    armar_inicio(marco)
    armar_lista(marco)
    armar_concepto(marco)
    armar_comparar(marco)
    mostrar_inicio_geometria()

def ir_a_comparar():
    # No recibe datos.
    # Abre la pantalla de los dos triángulos.
    # No devuelve nada. Sirve para probar los clics.
    mostrar_comparar()

def obtener_filas():
    # No recibe datos.
    # Lee las filas que se están mostrando en la tabla.
    # Devuelve la lista de pares afirmación y razón.
    return filas_de_la_comprobacion(marcas)

def obtener_texto_resultado():
    # No recibe datos.
    # Lee el párrafo que está debajo de la tabla.
    # Devuelve ese texto.
    return etiqueta_resultado.cget("text")

def obtener_aviso():
    # No recibe datos.
    # Lee el aviso que guía el siguiente clic.
    # Devuelve ese texto.
    return etiqueta_aviso.cget("text")

def obtener_marcas():
    # No recibe datos.
    # Lee las marcas guardadas.
    # Devuelve la lista.
    return marcas
