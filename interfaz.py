# Pantalla para escribir una expresión y ver su factorización.
# Al abrir, muestra un menú. Cada caso enseña el plan con el que se desarrolló.
# La matemática queda en la carpeta casos. La congruencia está en geometria.

import os
import tkinter as tk
from algebra.expresiones import preparar_expresion, encontrar_el_tipo_de_expresion, letras_a_texto
from algebra.casos.factor_comun import determinar_si_es_factor_comun, resolver_factor_comun, plan_del_caso as plan_factor_comun
from algebra.casos.agrupacion import resolver_agrupacion, plan_del_caso as plan_agrupacion
from algebra.casos.diferencia_de_cuadrados import resolver_diferencia_de_cuadrados, plan_del_caso as plan_diferencia
from algebra.casos.trinomio_cuadrado_perfecto import resolver_trinomio_cuadrado_perfecto, plan_del_caso as plan_trinomio_cuadrado
from algebra.casos.trinomio_x2_bx_c import resolver_trinomio_x2_bx_c, plan_del_caso as plan_x2
from algebra.casos.trinomio_ax2_bx_c import resolver_trinomio_ax2_bx_c, plan_del_caso as plan_ax2
from algebra.casos.trinomio_por_adicion_y_sustraccion import resolver_trinomio_por_adicion_y_sustraccion, plan_del_caso as plan_adicion
from algebra.casos.suma_o_diferencia_de_cubos import resolver_suma_o_diferencia_de_cubos, nombre_del_caso, plan_del_caso as plan_cubos
from algebra.casos.suma_o_diferencia_de_potencias import resolver_suma_o_diferencia_de_potencias, nombre_de_potencias_iguales, plan_del_caso as plan_potencias
from algebra.casos.cuadrado_de_binomio import resolver_cuadrado_de_binomio, plan_del_caso as plan_cuadrado
from algebra.casos.cubo_de_binomio import resolver_cubo_de_binomio, resolver_cubo_perfecto, plan_del_desarrollo, plan_de_la_factorizacion
from geometria.pantalla import armar_pantalla_geometria, mostrar_inicio_geometria

# Estos se llenan cuando se abre la ventana.
# Los botones los usan para escribir y para mostrar el resultado.
# El logo se guarda aquí para que la imagen no desaparezca.
cuadro_expresion=None
etiqueta_resultado=None
logos_guardados=[]
marco_inicio=None
marco_menu=None
marco_factorizar=None
marco_plan=None
marco_geometria=None
titulo_del_plan=None
cuadro_del_plan=None


def poner_potencias_bonitas(texto):
    # Recibe un texto como "3x^2(2x+3y)".
    # Cambia ^2 por ² para que se lea como en el cuaderno.
    # Devuelve "3x²(2x+3y)".
    digitos={
        "0":"⁰",
        "1":"¹",
        "2":"²",
        "3":"³",
        "4":"⁴",
        "5":"⁵",
        "6":"⁶",
        "7":"⁷",
        "8":"⁸",
        "9":"⁹",
    }
    resultado=""
    posicion=0
    while posicion<len(texto):
        es_potencia=texto[posicion]=="^"
        sigue_un_numero=posicion+1<len(texto) and texto[posicion+1].isdigit()
        if es_potencia and sigue_un_numero:
            posicion=posicion+1
            while posicion<len(texto) and texto[posicion].isdigit():
                resultado=resultado+digitos[texto[posicion]]
                posicion=posicion+1
        else:
            resultado=resultado+texto[posicion]
            posicion=posicion+1
    return resultado

def armar_respuesta(expresion):
    # Recibe la expresión escrita, por ejemplo "6x^2 + 9xy".
    # Pregunta primero si es el cuadrado o el cubo de un binomio. Si no, pregunta el factor común y los demás casos.
    # Devuelve el texto que se muestra en la pantalla.
    expresion=preparar_expresion(expresion)
    if expresion=="":
        return "Escribe una expresión.\nEjemplo: 6x² + 9xy"

    try:
        resultado_cuadrado=resolver_cuadrado_de_binomio(expresion)
        if resultado_cuadrado!="":
            texto="Tipo: binomio"
            texto=texto+"\nCaso: cuadrado de un binomio"
            texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_cuadrado)
            return texto

        resultado_cubo=resolver_cubo_de_binomio(expresion)
        if resultado_cubo!="":
            texto="Tipo: binomio"
            texto=texto+"\nCaso: cubo de un binomio"
            texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_cubo)
            return texto

        el_tipo,division_de_datos=encontrar_el_tipo_de_expresion(expresion)
        if el_tipo=="":
            return "No pude leer esa expresión.\nEjemplo: 6x² + 9xy"

        texto="Tipo: "+el_tipo
        if determinar_si_es_factor_comun(division_de_datos):
            resultado,letras_en_comun=resolver_factor_comun(division_de_datos)
            texto=texto+"\nCaso: factor común"
            if len(letras_en_comun)>0:
                texto=texto+"\nLetras en común: "+poner_potencias_bonitas(letras_a_texto(letras_en_comun))
            texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado)
        else:
            resultado_diferencia=resolver_diferencia_de_cuadrados(division_de_datos)
            if resultado_diferencia!="":
                texto=texto+"\nCaso: diferencia de cuadrados"
                texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_diferencia)
            else:
                resultado_cubos=resolver_suma_o_diferencia_de_cubos(division_de_datos)
                if resultado_cubos!="":
                    texto=texto+"\nCaso: "+nombre_del_caso(division_de_datos)
                    texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_cubos)
                else:
                    resultado_potencias=resolver_suma_o_diferencia_de_potencias(division_de_datos)
                    if resultado_potencias!="":
                        texto=texto+"\nCaso: "+nombre_de_potencias_iguales(division_de_datos)
                        texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_potencias)
                    else:
                        resultado_trinomio=resolver_trinomio_cuadrado_perfecto(division_de_datos)
                        if resultado_trinomio!="":
                            texto=texto+"\nCaso: trinomio cuadrado perfecto"
                            texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_trinomio)
                        else:
                            resultado_adicion=resolver_trinomio_por_adicion_y_sustraccion(division_de_datos)
                            if resultado_adicion!="":
                                texto=texto+"\nCaso: trinomio cuadrado perfecto por adición y sustracción"
                                texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_adicion)
                            else:
                                resultado_forma=resolver_trinomio_x2_bx_c(division_de_datos)
                                if resultado_forma!="":
                                    texto=texto+"\nCaso: trinomio de la forma x² + bx + c"
                                    texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_forma)
                                else:
                                    resultado_ax2=resolver_trinomio_ax2_bx_c(division_de_datos)
                                    if resultado_ax2!="":
                                        texto=texto+"\nCaso: trinomio de la forma ax² + bx + c"
                                        texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_ax2)
                                    else:
                                        resultado_cubo_perfecto=resolver_cubo_perfecto(division_de_datos)
                                        if resultado_cubo_perfecto!="":
                                            texto=texto+"\nCaso: cubo perfecto de un binomio"
                                            texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_cubo_perfecto)
                                        else:
                                            resultado_agrupacion=resolver_agrupacion(division_de_datos)
                                            if resultado_agrupacion!="":
                                                texto=texto+"\nCaso: factorización por agrupación"
                                                texto=texto+"\nResultado: "+poner_potencias_bonitas(resultado_agrupacion)
                                            else:
                                                texto=texto+"\nCaso: no se pudo factorizar con los casos del programa"
        return texto
    except Exception:
        return "No pude leer esa expresión.\nRevisa los signos y las potencias.\nEjemplo: 6x² + 9xy"

def insertar_texto(texto):
    # Recibe el texto de un botón, por ejemplo "x" o "²".
    # Lo escribe en el cuadro, en el lugar del cursor.
    # No devuelve nada.
    cuadro_expresion.insert(tk.INSERT,texto)
    cuadro_expresion.focus()

def borrar_un_caracter():
    # No recibe datos.
    # Borra el carácter que está justo antes del cursor.
    # No devuelve nada.
    posicion=cuadro_expresion.index(tk.INSERT)
    if posicion>0:
        cuadro_expresion.delete(posicion-1,posicion)
    cuadro_expresion.focus()

def borrar_todo():
    # No recibe datos.
    # Deja el cuadro vacío y limpia el resultado.
    # No devuelve nada.
    cuadro_expresion.delete(0,tk.END)
    etiqueta_resultado.config(text="Aquí aparece el tipo, el caso y el resultado.")
    cuadro_expresion.focus()

def mostrar_resultado():
    # No recibe datos.
    # Lee lo que hay en el cuadro y lo muestra factorizado.
    # No devuelve nada.
    expresion=cuadro_expresion.get()
    etiqueta_resultado.config(text=armar_respuesta(expresion))

def texto_para_insertar(texto):
    # Recibe el texto de un botón, por ejemplo "x¹¹" o "7".
    # Si el botón es una potencia, devuelve solo el número de arriba, "¹¹".
    # Si es otro botón, devuelve el mismo texto.
    if len(texto)>1 and texto[0]=="x":
        return texto[1:]
    return texto

def al_pulsar_boton(evento):
    # Recibe el clic de un botón del teclado de la pantalla.
    # Escribe el número, la letra o la potencia. La flecha borra un carácter.
    # No devuelve nada.
    texto=evento.widget["text"]
    if texto=="←":
        borrar_un_caracter()
    else:
        insertar_texto(texto_para_insertar(texto))

def crear_boton(ventana,texto,fila,columna,columnas=1):
    # Recibe la ventana, el texto del botón, la fila, la columna y cuántas columnas ocupa.
    # Crea el botón y lo pone en la cuadrícula.
    # Devuelve el botón.
    boton=tk.Button(
        ventana,
        text=texto,
        font=("Segoe UI",14),
        height=1,
        bg="#ffffff",
        activebackground="#d9e6fb",
    )
    boton.grid(row=fila,column=columna,columnspan=columnas,padx=3,pady=3,sticky="nsew")
    boton.bind("<Button-1>",al_pulsar_boton)
    return boton

def al_presionar_enter(evento):
    # Recibe la tecla Enter.
    # Muestra el resultado de la expresión que está escrita.
    # No devuelve nada.
    mostrar_resultado()

def cargar_logo(ventana):
    # Recibe la ventana o el marco donde va el logo.
    # Busca el logo en la carpeta imagenes y lo muestra más pequeño.
    # No le cambia los colores. Si no está el archivo, devuelve nada.
    carpeta=os.path.dirname(os.path.abspath(__file__))
    ruta=os.path.join(carpeta,"imagenes","Logo_corazonistas_png-1.png")
    if not os.path.exists(ruta):
        return None
    imagen=tk.PhotoImage(file=ruta)
    pequeno=imagen.subsample(4,4)
    logos_guardados.append(pequeno)
    etiqueta=tk.Label(ventana,image=pequeno,bg="#eef3fa")
    return etiqueta

def nombres_de_los_casos():
    # No recibe datos.
    # Arma la lista del menú, en el orden en que se enseñan los casos.
    # Devuelve cada nombre junto con la función que escribe su plan.
    casos=[]
    casos.append(("Factor común",plan_factor_comun))
    casos.append(("Factorización por agrupación",plan_agrupacion))
    casos.append(("Diferencia de cuadrados",plan_diferencia))
    casos.append(("Trinomio cuadrado perfecto",plan_trinomio_cuadrado))
    casos.append(("Trinomio de la forma x² + bx + c",plan_x2))
    casos.append(("Trinomio de la forma ax² + bx + c",plan_ax2))
    casos.append(("Trinomio cuadrado perfecto por adición y sustracción",plan_adicion))
    casos.append(("Suma o diferencia de cubos perfectos",plan_cubos))
    casos.append(("Cubo perfecto de un binomio",plan_de_la_factorizacion))
    casos.append(("Suma o diferencia de dos potencias iguales",plan_potencias))
    casos.append(("Cuadrado de un binomio",plan_cuadrado))
    casos.append(("Cubo de un binomio",plan_del_desarrollo))
    return casos

def ocultar_marcos():
    # No recibe datos.
    # Esconde el inicio, el álgebra, la factorización, el plan y la geometría.
    # No devuelve nada.
    marco_inicio.grid_remove()
    marco_menu.grid_remove()
    marco_factorizar.grid_remove()
    marco_plan.grid_remove()
    marco_geometria.grid_remove()

def mostrar_geometria():
    # No recibe datos.
    # Abre la congruencia de triángulos en el inicio de esa sección.
    # No devuelve nada.
    ocultar_marcos()
    marco_geometria.grid(row=0, column=0, sticky="nsew")
    mostrar_inicio_geometria()

def mostrar_menu():
    # No recibe datos.
    # Muestra los dos temas: álgebra y geometría.
    # No devuelve nada.
    ocultar_marcos()
    marco_inicio.grid(row=0,column=0,sticky="nsew")

def mostrar_algebra():
    # No recibe datos.
    # Muestra los casos de factorización y el botón para factorizar.
    # No devuelve nada.
    ocultar_marcos()
    marco_menu.grid(row=0,column=0,sticky="nsew")

def mostrar_factorizar():
    # No recibe datos.
    # Muestra el cuadro para escribir una expresión.
    # No devuelve nada.
    ocultar_marcos()
    marco_factorizar.grid(row=0,column=0,sticky="nsew")
    cuadro_expresion.focus()

def mostrar_plan(nombre):
    # Recibe el nombre del caso, por ejemplo "Factor común".
    # Busca su plan y lo escribe en la pantalla.
    # No devuelve nada.
    texto=""
    for nombre_caso,escribir_plan in nombres_de_los_casos():
        if nombre_caso==nombre:
            texto=escribir_plan()
    titulo_del_plan.config(text=nombre)
    cuadro_del_plan.config(state="normal")
    cuadro_del_plan.delete("1.0",tk.END)
    cuadro_del_plan.insert("1.0",texto)
    cuadro_del_plan.config(state="disabled")
    ocultar_marcos()
    marco_plan.grid(row=0,column=0,sticky="nsew")

def al_abrir_caso(evento):
    # Recibe el clic de un caso del menú.
    # Abre el plan de ese caso.
    # No devuelve nada.
    mostrar_plan(evento.widget["text"])

def crear_boton_de_caso(marco,nombre,fila,columna):
    # Recibe el marco, el nombre del caso, la fila y la columna.
    # Crea el botón que abre el plan de ese caso.
    # Devuelve el botón.
    boton=tk.Button(
        marco,
        text=nombre,
        font=("Segoe UI",13),
        bg="#ffffff",
        activebackground="#d9e6fb",
        wraplength=420,
        justify="center",
    )
    boton.grid(row=fila,column=columna,padx=8,pady=6,sticky="nsew")
    boton.bind("<Button-1>",al_abrir_caso)
    return boton

def dibujar_icono_algebra(lienzo):
    # Recibe el lienzo del botón de álgebra.
    # Dibuja x al cuadrado para reconocer la factorización.
    # No devuelve nada.
    lienzo.create_text(90,46,text="x²",font=("Segoe UI",40,"bold"),fill="#2f6fed")
    lienzo.create_text(90,96,text="+ bx + c",font=("Segoe UI",16),fill="#1d3557")

def dibujar_icono_geometria(lienzo):
    # Recibe el lienzo del botón de geometría.
    # Dibuja dos triángulos para reconocer la congruencia.
    # No devuelve nada.
    lienzo.create_polygon(34,30,16,102,86,102,fill="#e7f0ff",outline="#1d3557",width=3)
    lienzo.create_polygon(118,30,100,102,170,102,fill="#e8f6ef",outline="#0f766e",width=3)
    lienzo.create_text(34,16,text="A",font=("Segoe UI",12,"bold"),fill="#c1121f")
    lienzo.create_text(118,16,text="D",font=("Segoe UI",12,"bold"),fill="#c1121f")

def enlazar_clic(widget,funcion):
    # Recibe un cuadro y la función que debe correr al hacer clic.
    # Pone ese clic en el cuadro y en lo que tiene dentro, como el icono.
    # No devuelve nada.
    widget.bind("<Button-1>",funcion)
    for hijo in widget.winfo_children():
        enlazar_clic(hijo,funcion)

def al_pulsar_algebra(evento):
    # Recibe el clic de la tarjeta de álgebra.
    # Abre los casos de factorización.
    # No devuelve nada.
    mostrar_algebra()

def al_pulsar_geometria(evento):
    # Recibe el clic de la tarjeta de geometría.
    # Abre la congruencia de triángulos.
    # No devuelve nada.
    mostrar_geometria()

def crear_tarjeta(marco,titulo,detalle,color,dibujar,al_pulsar,columna):
    # Recibe el marco, los textos, el color, el dibujo del icono y la columna.
    # Arma un botón grande con icono para un tema.
    # No devuelve nada.
    tarjeta=tk.Frame(marco,bg="#ffffff",highlightbackground=color,highlightthickness=3,cursor="hand2")
    tarjeta.grid(row=4,column=columna,padx=24,pady=12,sticky="nsew")
    lienzo=tk.Canvas(tarjeta,width=180,height=120,bg="#ffffff",highlightthickness=0,cursor="hand2")
    lienzo.grid(row=0,column=0,padx=36,pady=(18,0))
    dibujar(lienzo)
    nombre=tk.Label(tarjeta,text=titulo,font=("Segoe UI",22,"bold"),bg="#ffffff",fg=color,cursor="hand2")
    nombre.grid(row=1,column=0,pady=(8,0))
    texto=tk.Label(tarjeta,text=detalle,font=("Segoe UI",14),bg="#ffffff",fg="#33415c",cursor="hand2")
    texto.grid(row=2,column=0,pady=(0,18))
    tarjeta.grid_columnconfigure(0,weight=1)
    enlazar_clic(tarjeta,al_pulsar)

def armar_inicio(marco):
    # Recibe el marco de la pantalla inicial.
    # Pone el nombre del estudiante y los dos temas, cada uno con su icono.
    # No devuelve nada.
    logo=cargar_logo(marco)
    if logo!=None:
        logo.grid(row=0,column=0,columnspan=2,pady=(16,0))

    titulo=tk.Label(
        marco,
        text="Matemáticas 8C",
        font=("Segoe UI",26,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=1,column=0,columnspan=2,pady=(8,0))

    estudiante=tk.Label(
        marco,
        text="Juan Pablo Urzola Marin",
        font=("Segoe UI",16),
        bg="#eef3fa",
        fg="#1d3557",
    )
    estudiante.grid(row=2,column=0,columnspan=2,pady=(0,4))

    ayuda=tk.Label(
        marco,
        text="Elige un tema.",
        font=("Segoe UI",14),
        bg="#eef3fa",
        fg="#33415c",
    )
    ayuda.grid(row=3,column=0,columnspan=2,pady=(0,8))

    crear_tarjeta(marco,"Álgebra","Factorización","#2f6fed",dibujar_icono_algebra,al_pulsar_algebra,0)
    crear_tarjeta(marco,"Geometría","Congruencia de triángulos","#0f766e",dibujar_icono_geometria,al_pulsar_geometria,1)
    marco.grid_columnconfigure(0,weight=1)
    marco.grid_columnconfigure(1,weight=1)

def armar_menu(marco):
    # Recibe el marco del álgebra.
    # Pone el logo, el botón para factorizar y un botón por cada caso.
    # No devuelve nada.
    logo=cargar_logo(marco)
    if logo!=None:
        logo.grid(row=0,column=0,columnspan=2,pady=(12,0))

    titulo=tk.Label(
        marco,
        text="Casos de factorización",
        font=("Segoe UI",22,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
    )
    titulo.grid(row=1,column=0,columnspan=2,pady=(8,4))

    estudiante=tk.Label(
        marco,
        text="Juan Pablo Urzola Marin\nCurso 8C",
        font=("Segoe UI",14),
        bg="#eef3fa",
        fg="#1d3557",
        justify="center",
    )
    estudiante.grid(row=2,column=0,columnspan=2,pady=(0,8))

    boton_factorizar=tk.Button(
        marco,
        text="Factorizar una expresión",
        font=("Segoe UI",14,"bold"),
        bg="#2f6fed",
        fg="#ffffff",
        activebackground="#1d4ed8",
        activeforeground="#ffffff",
        command=mostrar_factorizar,
    )
    boton_factorizar.grid(row=3,column=0,columnspan=2,padx=16,pady=(0,12),sticky="ew")

    casos=nombres_de_los_casos()
    indice=0
    while indice<len(casos):
        nombre=casos[indice][0]
        fila=4+(indice//2)
        columna=indice%2
        crear_boton_de_caso(marco,nombre,fila,columna)
        indice=indice+1

    boton_inicio=tk.Button(
        marco,
        text="Volver al inicio",
        font=("Segoe UI",14),
        bg="#ffffff",
        command=mostrar_menu,
    )
    boton_inicio.grid(row=10,column=0,columnspan=2,padx=16,pady=(8,12),sticky="ew")

    marco.grid_columnconfigure(0,weight=1)
    marco.grid_columnconfigure(1,weight=1)

def armar_plan(marco):
    # Recibe el marco del plan.
    # Prepara el título, el texto de los pasos y el botón para volver.
    # No devuelve nada.
    global titulo_del_plan
    global cuadro_del_plan

    titulo_del_plan=tk.Label(
        marco,
        text="",
        font=("Segoe UI",22,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
        wraplength=900,
    )
    titulo_del_plan.grid(row=0,column=0,columnspan=2,padx=16,pady=(16,8),sticky="ew")

    cuadro_del_plan=tk.Text(
        marco,
        font=("Segoe UI",16),
        bg="#ffffff",
        fg="#1d3557",
        wrap="word",
        padx=16,
        pady=16,
        relief="solid",
        borderwidth=1,
    )
    cuadro_del_plan.grid(row=1,column=0,padx=(16,0),pady=8,sticky="nsew")
    cuadro_del_plan.config(state="disabled")

    barra=tk.Scrollbar(marco,command=cuadro_del_plan.yview)
    barra.grid(row=1,column=1,padx=(0,16),pady=8,sticky="ns")
    cuadro_del_plan.config(yscrollcommand=barra.set)

    boton_volver=tk.Button(
        marco,
        text="Volver a álgebra",
        font=("Segoe UI",14),
        bg="#ffffff",
        command=mostrar_algebra,
    )
    boton_volver.grid(row=2,column=0,columnspan=2,padx=16,pady=(8,16),sticky="ew")

    marco.grid_columnconfigure(0,weight=1)
    marco.grid_rowconfigure(1,weight=1)

def armar_encabezado(marco):
    # Recibe el marco de la factorización.
    # Pone el logo a la izquierda y el nombre y el curso a la derecha.
    # No devuelve nada. Así la zona del resultado queda más alta.
    encabezado=tk.Frame(marco,bg="#eef3fa")
    encabezado.grid(row=0,column=0,columnspan=10,sticky="ew",padx=16,pady=(8,4))

    logo=cargar_logo(encabezado)
    if logo!=None:
        logo.grid(row=0,column=0,rowspan=3,sticky="w")

    titulo=tk.Label(
        encabezado,
        text="Factorización",
        font=("Segoe UI",22,"bold"),
        bg="#eef3fa",
        fg="#1d3557",
        anchor="e",
    )
    titulo.grid(row=0,column=1,sticky="e")

    estudiante=tk.Label(
        encabezado,
        text="Juan Pablo Urzola Marin\nCurso 8C",
        font=("Segoe UI",14),
        bg="#eef3fa",
        fg="#1d3557",
        justify="right",
        anchor="e",
    )
    estudiante.grid(row=1,column=1,sticky="e")

    ayuda=tk.Label(
        encabezado,
        text="Escribe la expresión. Las potencias van de x² hasta x¹¹.\nEjemplo: 6x² + 9xy",
        font=("Segoe UI",11),
        bg="#eef3fa",
        fg="#33415c",
        justify="right",
        anchor="e",
    )
    ayuda.grid(row=2,column=1,sticky="e")
    encabezado.grid_columnconfigure(1,weight=1)

def armar_factorizar(marco):
    # Recibe el marco de la factorización.
    # Arma el encabezado, el cuadro, los botones y el resultado.
    # No devuelve nada.
    global cuadro_expresion
    global etiqueta_resultado

    armar_encabezado(marco)

    cuadro_expresion=tk.Entry(
        marco,
        font=("Segoe UI",20),
        justify="center",
        bg="#ffffff",
        relief="solid",
        borderwidth=1,
    )
    cuadro_expresion.grid(row=1,column=0,columnspan=10,padx=16,pady=(0,8),sticky="ew")

    teclas=[
        ["1","2","3","4","5","6","7","8","9","0"],
        ["a","b","c","d","e","f","g","h","i","j"],
        ["x²","x³","x⁴","x⁵","x⁶","x⁷","x⁸","x⁹","x¹⁰","x¹¹"],
    ]
    fila=2
    for grupo in teclas:
        columna=0
        for tecla in grupo:
            crear_boton(marco,tecla,fila,columna)
            columna=columna+1
        fila=fila+1

    crear_boton(marco,"(",5,0,2)
    crear_boton(marco,")",5,2,2)
    crear_boton(marco,"+",5,4,2)
    crear_boton(marco,"-",5,6,2)
    crear_boton(marco,"←",5,8,2)

    boton_factorizar=tk.Button(
        marco,
        text="Factorizar",
        font=("Segoe UI",14,"bold"),
        bg="#2f6fed",
        fg="#ffffff",
        activebackground="#1d4ed8",
        activeforeground="#ffffff",
        command=mostrar_resultado,
    )
    boton_factorizar.grid(row=6,column=0,columnspan=6,padx=8,pady=8,sticky="ew")

    boton_borrar=tk.Button(
        marco,
        text="Borrar",
        font=("Segoe UI",14),
        bg="#f8d7da",
        command=borrar_todo,
    )
    boton_borrar.grid(row=6,column=6,columnspan=4,padx=8,pady=8,sticky="ew")

    etiqueta_resultado=tk.Label(
        marco,
        text="Aquí aparece el tipo, el caso y el resultado.",
        font=("Segoe UI",16),
        bg="#ffffff",
        fg="#1d3557",
        justify="left",
        anchor="nw",
        padx=12,
        pady=12,
        wraplength=920,
    )
    etiqueta_resultado.grid(row=7,column=0,columnspan=10,padx=16,pady=(0,8),sticky="nsew")

    boton_menu=tk.Button(
        marco,
        text="Volver a álgebra",
        font=("Segoe UI",14),
        bg="#ffffff",
        command=mostrar_algebra,
    )
    boton_menu.grid(row=8,column=0,columnspan=10,padx=16,pady=(0,12),sticky="ew")

    columna=0
    while columna<10:
        marco.grid_columnconfigure(columna,weight=1)
        columna=columna+1
    marco.grid_rowconfigure(7,weight=1,minsize=180)

def crear_ventana():
    # No recibe datos.
    # Arma el inicio, el álgebra, la factorización, el plan y la congruencia.
    # Devuelve la ventana para poder mostrarla.
    global marco_inicio
    global marco_menu
    global marco_factorizar
    global marco_plan
    global marco_geometria

    ventana=tk.Tk()
    ventana.title("Matemáticas 8C")
    ventana.configure(bg="#eef3fa")
    ventana.geometry("980x740")
    ventana.minsize(980,740)

    marco_inicio=tk.Frame(ventana,bg="#eef3fa")
    marco_menu=tk.Frame(ventana,bg="#eef3fa")
    marco_factorizar=tk.Frame(ventana,bg="#eef3fa")
    marco_plan=tk.Frame(ventana,bg="#eef3fa")
    marco_geometria=tk.Frame(ventana,bg="#eef3fa")
    armar_inicio(marco_inicio)
    armar_menu(marco_menu)
    armar_factorizar(marco_factorizar)
    armar_plan(marco_plan)
    armar_pantalla_geometria(marco_geometria, mostrar_menu)

    ventana.grid_columnconfigure(0,weight=1)
    ventana.grid_rowconfigure(0,weight=1)
    mostrar_menu()

    ventana.bind("<Return>",al_presionar_enter)
    ventana.state("zoomed")
    return ventana

if __name__=="__main__":
    ventana=crear_ventana()
    ventana.mainloop()
