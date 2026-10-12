# Pantalla de congruencia de triángulos.
# Primero explica los conceptos.
# Después deja marcar lados y ángulos con clics y arma la tabla.

import tkinter as tk
from geometria.conceptos import lista_de_conceptos, buscar_concepto
from geometria.criterios import filas_de_la_comprobacion, texto_de_los_triangulos, texto_del_resultado, usar_misma_figura, usar_triangulos_separados
from geometria.dibujos import dibujar_concepto, dibujar_dos_triangulos, dibujar_figura_compartida, dibujar_marcas, dibujar_marcas_compartidas, dibujar_parte_compartida, dibujar_parte_resaltada, parte_bajo_el_clic, parte_de_la_figura_compartida

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
aviso="Toca un lado o una letra."
modo_figura="separados"
titulo_comparar=None
etiqueta_pasos=None
etiqueta_pares=None
boton_separados=None
boton_misma=None


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

def resaltar_parte_compartida(ancho, alto, tipo, nombre):
    # Recibe el tamaño del lienzo, el tipo y el nombre de la parte.
    # La pinta de azul en la figura compartida.
    # No devuelve nada.
    parte={}
    parte["tipo"]=tipo
    parte["nombre"]=nombre
    dibujar_parte_compartida(lienzo_comparar, ancho, alto, parte, "#2f6fed")

def redibujar_figura_compartida(ancho, alto):
    # Recibe el ancho y el alto del lienzo.
    # Dibuja △ABD y △ACD, las marcas y lo que está elegido.
    # No devuelve nada.
    dibujar_figura_compartida(lienzo_comparar, ancho, alto)
    dibujar_marcas_compartidas(lienzo_comparar, ancho, alto, marcas)
    if par_pendiente!=None:
        resaltar_parte_compartida(ancho, alto, par_pendiente["tipo"], par_pendiente["parte_abc"])
        if par_pendiente["parte_abc"]!=par_pendiente["parte_def"]:
            resaltar_parte_compartida(ancho, alto, par_pendiente["tipo"], par_pendiente["parte_def"])
        return
    if parte_elegida!=None:
        dibujar_parte_compartida(lienzo_comparar, ancho, alto, parte_elegida, "#2f6fed")

def redibujar_triangulos_separados(ancho, alto):
    # Recibe el ancho y el alto del lienzo.
    # Dibuja △ABC y △DEF, las marcas y lo que está elegido.
    # No devuelve nada.
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
        return
    if parte_elegida!=None:
        dibujar_parte_resaltada(lienzo_comparar, ancho, alto, parte_elegida, "#2f6fed")

def redibujar_comparacion():
    # No recibe datos.
    # Vuelve a dibujar la figura activa, las marcas y la parte elegida.
    # No devuelve nada.
    ancho, alto=tamano_usado()
    lienzo_comparar.delete("all")
    if modo_figura=="misma":
        redibujar_figura_compartida(ancho, alto)
        return
    redibujar_triangulos_separados(ancho, alto)

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
        es_conclusion=fila[0]==texto_de_los_triangulos()
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

def es_del_primer_triangulo(parte):
    # Recibe una parte tocada en el dibujo.
    # Dice si pertenece a △ABC o a △ABD, el triángulo de la izquierda.
    # Devuelve True o False.
    if parte["triangulo"]=="ABC":
        return True
    if parte["triangulo"]=="ABD":
        return True
    return False

def es_lado_comun(parte):
    # Recibe una parte tocada en el dibujo.
    # Dice si es el lado AD, que está en los dos triángulos.
    # Devuelve True o False.
    if "comun" in parte:
        if parte["comun"]==True:
            return True
    return False

def guardar_par_pendiente(primera, segunda):
    # Recibe las dos partes elegidas, una de cada triángulo.
    # Las ordena: primero △ABC o △ABD, después el otro triángulo.
    # No devuelve nada. Deja el par listo para la razón.
    global par_pendiente
    if es_del_primer_triangulo(primera):
        parte_abc=primera["nombre"]
        parte_def=segunda["nombre"]
    else:
        parte_abc=segunda["nombre"]
        parte_def=primera["nombre"]
    par_pendiente={}
    par_pendiente["tipo"]=primera["tipo"]
    par_pendiente["parte_abc"]=parte_abc
    par_pendiente["parte_def"]=parte_def

def preparar_lado_comun(parte):
    # Recibe el lado AD, tocado una sola vez.
    # Deja listo el par AD ≅ AD para elegir la razón.
    # No devuelve nada.
    global par_pendiente
    global parte_elegida
    global aviso
    par_pendiente={}
    par_pendiente["tipo"]="lado"
    par_pendiente["parte_abc"]=parte["nombre"]
    par_pendiente["parte_def"]=parte["nombre"]
    parte_elegida=parte
    aviso="Este lado está en los dos triángulos. Elige el porqué."
    mostrar_razones()

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

def parte_bajo_el_clic_actual(x, y, ancho, alto):
    # Recibe el clic y el tamaño del lienzo.
    # Busca la parte en la figura que está activa.
    # Devuelve la parte. Si el clic cayó fuera, devuelve None.
    if modo_figura=="misma":
        return parte_de_la_figura_compartida(x, y, ancho, alto)
    return parte_bajo_el_clic(x, y, ancho, alto)

def procesar_clic(x, y):
    # Recibe las coordenadas del clic en el lienzo.
    # Elige la primera parte, completa el par, o marca AD con un solo clic.
    # No devuelve nada. Si el par está listo, pide la razón.
    global parte_elegida
    global par_pendiente
    global aviso
    if par_pendiente!=None:
        par_pendiente=None
        parte_elegida=None
        ocultar_razones()
    ancho, alto=tamano_usado()
    parte=parte_bajo_el_clic_actual(x, y, ancho, alto)
    if parte==None:
        if modo_figura=="misma":
            aviso="Toca un lado o el nombre de un ángulo."
        else:
            aviso="Toca la línea del lado, o la letra."
        actualizar_comparacion()
        return
    if es_lado_comun(parte):
        preparar_lado_comun(parte)
        actualizar_comparacion()
        return
    if parte_elegida==None:
        parte_elegida=parte
        if modo_figura=="misma":
            aviso="Ahora toca la parte igual en el otro triángulo."
        else:
            aviso="Ahora toca el otro triángulo."
        actualizar_comparacion()
        return
    if parte["triangulo"]==parte_elegida["triangulo"]:
        parte_elegida=parte
        aviso="Ese es el mismo triángulo. Toca el otro."
        actualizar_comparacion()
        return
    if parte["tipo"]!=parte_elegida["tipo"]:
        if modo_figura=="misma":
            aviso="Un lado va con un lado. Un ángulo va con un ángulo."
        else:
            aviso="Un lado va con un lado. Una letra va con una letra."
        actualizar_comparacion()
        return
    guardar_par_pendiente(parte_elegida, parte)
    aviso="Elige por qué son iguales."
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
        aviso="Cambié el porqué de esa marca."
    else:
        marca={}
        marca["tipo"]=par_pendiente["tipo"]
        marca["parte_abc"]=par_pendiente["parte_abc"]
        marca["parte_def"]=par_pendiente["parte_def"]
        marca["razon"]=razon
        marcas.append(marca)
        aviso="Listo. Puedes marcar otro."
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
        aviso="No hay nada para quitar."
        actualizar_comparacion()
        return
    del marcas[len(marcas)-1]
    aviso="Quité la última marca."
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
    aviso="Borré las marcas."
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

def razones_del_modo():
    # No recibe datos.
    # En separados solo ofrece Dado. En la misma figura ofrece las cinco razones.
    # Devuelve los grupos de botones.
    if modo_figura=="separados":
        return [["Dado"]]
    return [
        ["Punto medio", "Bisectriz"],
        ["Lado común", "Propiedad reflexiva"],
        ["Dado"],
    ]

def armar_razones(marco):
    # Recibe el marco de las razones.
    # Borra los botones y pone los de la figura activa.
    # No devuelve nada.
    hijos=marco.winfo_children()
    for hijo in hijos:
        hijo.destroy()
    razones=razones_del_modo()
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

def armar_instrucciones(panel):
    # Recibe el panel de la derecha.
    # Escribe los pasos, en frases cortas, arriba de la tabla.
    # No devuelve nada. Guarda las etiquetas para cambiarlas al cambiar de figura.
    global etiqueta_pasos
    global etiqueta_pares
    caja=tk.Frame(panel, bg="#ffffff", highlightbackground="#cbd5e1", highlightthickness=1)
    caja.grid(row=0, column=0, sticky="ew", pady=(0, 6))

    titulo=tk.Label(
        caja,
        text="Cómo hacerlo",
        font=("Segoe UI", 15, "bold"),
        bg="#ffffff",
        fg="#1d3557",
        anchor="w",
    )
    titulo.grid(row=0, column=0, sticky="ew", padx=12, pady=(8, 2))

    etiqueta_pasos=tk.Label(
        caja,
        text="",
        font=("Segoe UI", 13),
        bg="#ffffff",
        fg="#1d3557",
        justify="left",
        anchor="w",
    )
    etiqueta_pasos.grid(row=1, column=0, sticky="ew", padx=12)

    etiqueta_pares=tk.Label(
        caja,
        text="",
        font=("Segoe UI", 12),
        bg="#ffffff",
        fg="#33415c",
        justify="left",
        anchor="w",
    )
    etiqueta_pares.grid(row=2, column=0, sticky="ew", padx=12, pady=(6, 10))

def escribir_instrucciones():
    # No recibe datos.
    # Cambia los pasos y la nota según Separados o Misma figura.
    # No devuelve nada.
    if modo_figura=="separados":
        etiqueta_pasos.config(text="1. Toca un lado o una letra.\n2. Toca lo mismo en el otro triángulo.\n3. Elige por qué son iguales.")
        etiqueta_pares.config(text="A va con D.   B va con E.   C va con F.\nEl tamaño del dibujo no importa.")
        titulo_comparar.config(text="Comparar △ABC y △DEF")
        return
    etiqueta_pasos.config(text="1. Toca dos partes iguales, o toca AD si es el lado de en medio.\n2. Elige el porqué: punto medio, bisectriz, lado común o reflexiva.")
    etiqueta_pares.config(text="D está en la mitad de BC.\nAD parte el ángulo A y está en los dos triángulos.")
    titulo_comparar.config(text="Comparar △ABD y △ACD")

def pintar_botones_de_modo():
    # No recibe datos.
    # Pinta de color el botón de la figura que está activa.
    # No devuelve nada.
    if modo_figura=="separados":
        boton_separados.config(bg="#2f6fed", fg="#ffffff", activebackground="#2f6fed", activeforeground="#ffffff")
        boton_misma.config(bg="#ffffff", fg="#1d3557", activebackground="#d9e6fb", activeforeground="#1d3557")
        return
    boton_separados.config(bg="#ffffff", fg="#1d3557", activebackground="#d9e6fb", activeforeground="#1d3557")
    boton_misma.config(bg="#0f766e", fg="#ffffff", activebackground="#0f766e", activeforeground="#ffffff")

def poner_modo(modo):
    # Recibe "separados" o "misma".
    # Cambia la figura, borra las marcas y cambia las razones.
    # No devuelve nada.
    global modo_figura
    global marcas
    global parte_elegida
    global par_pendiente
    global aviso
    if modo_figura==modo:
        return
    modo_figura=modo
    marcas=[]
    parte_elegida=None
    par_pendiente=None
    if modo=="separados":
        usar_triangulos_separados()
        aviso="Toca un lado o una letra."
    else:
        usar_misma_figura()
        aviso="Toca dos partes, o toca el lado AD."
    armar_razones(marco_razones)
    ocultar_razones()
    escribir_instrucciones()
    pintar_botones_de_modo()
    actualizar_comparacion()

def al_elegir_separados():
    # No recibe datos.
    # Pasa a los dos triángulos separados.
    # No devuelve nada.
    poner_modo("separados")

def al_elegir_misma():
    # No recibe datos.
    # Pasa a △ABD y △ACD en la misma figura.
    # No devuelve nada.
    poner_modo("misma")

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
    global titulo_comparar
    global boton_separados
    global boton_misma
    usar_triangulos_separados()
    marco_comparar=tk.Frame(marco, bg="#eef3fa")

    titulo_comparar=tk.Label(
        marco_comparar,
        text="Comparar △ABC y △DEF",
        font=("Segoe UI", 20, "bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo_comparar.grid(row=0, column=0, pady=(8, 2))

    barra=tk.Frame(marco_comparar, bg="#eef3fa")
    barra.grid(row=1, column=0, sticky="ew", padx=16)
    boton_conceptos=crear_boton_blanco(barra, "Conceptos", mostrar_lista_de_conceptos)
    boton_conceptos.grid(row=0, column=0, padx=(0, 8), sticky="w")
    boton_inicio=crear_boton_blanco(barra, "Inicio", mostrar_inicio_geometria)
    boton_inicio.grid(row=0, column=1, padx=(0, 8), sticky="w")
    boton_menu=crear_boton_blanco(barra, "Volver al menú", volver_al_menu)
    boton_menu.grid(row=0, column=3, sticky="e")
    barra.grid_columnconfigure(2, weight=1)

    modos=tk.Frame(marco_comparar, bg="#eef3fa")
    modos.grid(row=2, column=0, sticky="w", padx=16, pady=(4, 0))
    texto_modo=tk.Label(
        modos,
        text="Figura:",
        font=("Segoe UI", 14, "bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    texto_modo.grid(row=0, column=0, padx=(0, 8))
    boton_separados=crear_boton_blanco(modos, "Separados", al_elegir_separados)
    boton_separados.grid(row=0, column=1, padx=(0, 8))
    boton_misma=crear_boton_blanco(modos, "Misma figura", al_elegir_misma)
    boton_misma.grid(row=0, column=2)
    pintar_botones_de_modo()

    zona=tk.Frame(marco_comparar, bg="#eef3fa")
    zona.grid(row=3, column=0, padx=16, pady=(8, 10), sticky="nsew")

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

    armar_instrucciones(panel)
    escribir_instrucciones()

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
    zona.grid_columnconfigure(0, weight=1)
    zona.grid_columnconfigure(1, weight=1, minsize=480)
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
