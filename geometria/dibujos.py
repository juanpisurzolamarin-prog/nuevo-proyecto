# Dibujos de congruencia de triángulos.
# El esquema de la comparación y el dibujo de cada concepto.
# También dice qué lado o qué ángulo quedó bajo el clic.

import math

color_linea="#1d3557"
color_suave="#5c6b7a"
color_abc="#e7f0ff"
color_def="#e8f6ef"
radio_de_la_letra=20
distancia_maxima_al_lado=12
colores_de_marca=[
    "#c1121f",
    "#2f6fed",
    "#2d6a4f",
    "#9a3412",
    "#6d28d9",
    "#0f766e",
    "#b45309",
    "#1d4e89",
]


def distancia(x1, y1, x2, y2):
    # Recibe dos puntos.
    # Mide la distancia entre ellos.
    # Devuelve esa distancia.
    avance=x2-x1
    subida=y2-y1
    return math.sqrt(avance*avance+subida*subida)

def distancia_al_segmento(x, y, x1, y1, x2, y2):
    # Recibe un punto y los dos extremos de un segmento.
    # Mide la distancia del punto al segmento, no a la recta infinita.
    # Devuelve esa distancia.
    largo_x=x2-x1
    largo_y=y2-y1
    largo_2=largo_x*largo_x+largo_y*largo_y
    if largo_2==0:
        return distancia(x, y, x1, y1)
    avance=((x-x1)*largo_x+(y-y1)*largo_y)/largo_2
    if avance<0:
        avance=0
    if avance>1:
        avance=1
    cercano_x=x1+avance*largo_x
    cercano_y=y1+avance*largo_y
    return distancia(x, y, cercano_x, cercano_y)

def punto_medio(punto_1, punto_2):
    # Recibe los dos extremos de un segmento.
    # Calcula el punto que queda en la mitad.
    # Devuelve la coordenada (x, y).
    x=(punto_1[0]+punto_2[0])/2
    y=(punto_1[1]+punto_2[1])/2
    return (x, y)

def lados_abc():
    # No recibe datos.
    # Lista los lados del triángulo de la izquierda.
    # Devuelve ["AB", "BC", "CA"].
    return ["AB", "BC", "CA"]

def lados_def():
    # No recibe datos.
    # Lista los lados del triángulo de la derecha.
    # Devuelve ["DE", "EF", "FD"].
    return ["DE", "EF", "FD"]

def vertices_del_esquema(centro_x, alto, arriba, izquierda, derecha):
    # Recibe el centro horizontal, el alto y los tres nombres.
    # Arma un triángulo igual en cualquier lado de la pantalla.
    # Devuelve el diccionario de vértices.
    techo=64
    piso=alto-28
    if piso<techo+80:
        piso=techo+80
    mitad=105
    puntos={}
    puntos[arriba]=(centro_x, techo)
    puntos[izquierda]=(centro_x-mitad, piso)
    puntos[derecha]=(centro_x+mitad-24, piso-16)
    return puntos

def vertices_abc(ancho, alto):
    # Recibe el ancho y el alto del lienzo.
    # Coloca A arriba, B abajo a la izquierda y C abajo a la derecha.
    # Devuelve las tres coordenadas.
    return vertices_del_esquema(ancho*0.27, alto, "A", "B", "C")

def vertices_def(ancho, alto):
    # Recibe el ancho y el alto del lienzo.
    # Coloca D arriba, E abajo a la izquierda y F abajo a la derecha.
    # Devuelve las tres coordenadas.
    return vertices_del_esquema(ancho*0.73, alto, "D", "E", "F")

def puntos_de_un_triangulo(triangulo, ancho, alto):
    # Recibe "ABC" o "DEF" y el tamaño del lienzo.
    # Elige los vértices de ese triángulo.
    # Devuelve el diccionario de coordenadas.
    if triangulo=="ABC":
        return vertices_abc(ancho, alto)
    return vertices_def(ancho, alto)

def posicion_de_la_letra(x, y, centro_x, centro_y):
    # Recibe un vértice y el centro del triángulo.
    # Corre la letra hacia afuera para que no tape el vértice.
    # Devuelve la coordenada de la letra.
    avance=x-centro_x
    subida=y-centro_y
    largo=math.sqrt(avance*avance+subida*subida)
    if largo==0:
        return (x, y-28)
    return (x+avance/largo*28, y+subida/largo*28)

def letras_de_los_vertices(puntos):
    # Recibe los vértices de un triángulo.
    # Calcula el centro y coloca cada letra por fuera.
    # Devuelve un diccionario con la coordenada de cada letra.
    nombres=[]
    for nombre in puntos:
        nombres.append(nombre)
    centro_x=0
    centro_y=0
    for nombre in nombres:
        centro_x=centro_x+puntos[nombre][0]
        centro_y=centro_y+puntos[nombre][1]
    centro_x=centro_x/len(nombres)
    centro_y=centro_y/len(nombres)
    letras={}
    for nombre in nombres:
        x=puntos[nombre][0]
        y=puntos[nombre][1]
        letras[nombre]=posicion_de_la_letra(x, y, centro_x, centro_y)
    return letras

def linea(lienzo, x1, y1, x2, y2, color, grosor):
    # Recibe el lienzo, los extremos, el color y el grosor.
    # Dibuja un segmento.
    # No devuelve nada.
    lienzo.create_line(x1, y1, x2, y2, fill=color, width=grosor, capstyle="round")

def escribir(lienzo, x, y, mensaje, color, tamano):
    # Recibe el lienzo, el lugar, el mensaje, el color y el tamaño.
    # Escribe el texto en ese punto.
    # No devuelve nada.
    lienzo.create_text(x, y, text=mensaje, fill=color, font=("Segoe UI", tamano, "bold"))

def relleno_del_triangulo(lienzo, puntos, color):
    # Recibe los vértices y un color claro.
    # Pinta el interior del triángulo.
    # No devuelve nada.
    coordenadas=[]
    for nombre in puntos:
        coordenadas.append(puntos[nombre][0])
        coordenadas.append(puntos[nombre][1])
    lienzo.create_polygon(coordenadas, fill=color, outline="")

def dibujar_contorno(lienzo, puntos, color):
    # Recibe los vértices y el color de la línea.
    # Dibuja los tres lados.
    # No devuelve nada.
    nombres=[]
    for nombre in puntos:
        nombres.append(nombre)
    linea(lienzo, puntos[nombres[0]][0], puntos[nombres[0]][1], puntos[nombres[1]][0], puntos[nombres[1]][1], color, 3)
    linea(lienzo, puntos[nombres[1]][0], puntos[nombres[1]][1], puntos[nombres[2]][0], puntos[nombres[2]][1], color, 3)
    linea(lienzo, puntos[nombres[2]][0], puntos[nombres[2]][1], puntos[nombres[0]][0], puntos[nombres[0]][1], color, 3)

def dibujar_letras(lienzo, puntos, color):
    # Recibe los vértices y el color.
    # Escribe cada letra por fuera del triángulo.
    # No devuelve nada.
    letras=letras_de_los_vertices(puntos)
    for nombre in letras:
        escribir(lienzo, letras[nombre][0], letras[nombre][1], nombre, color, 16)

def dibujar_triangulo_con_letras(lienzo, puntos, color_relleno):
    # Recibe los vértices y el color del relleno.
    # Dibuja el triángulo y sus letras.
    # No devuelve nada.
    relleno_del_triangulo(lienzo, puntos, color_relleno)
    dibujar_contorno(lienzo, puntos, color_linea)
    dibujar_letras(lienzo, puntos, color_linea)

def dibujar_dos_triangulos(lienzo, ancho, alto):
    # Recibe el lienzo y su tamaño.
    # Dibuja el triángulo ABC a la izquierda y el DEF a la derecha, con la misma forma.
    # No devuelve nada.
    dibujar_triangulo_con_letras(lienzo, vertices_abc(ancho, alto), color_abc)
    dibujar_triangulo_con_letras(lienzo, vertices_def(ancho, alto), color_def)

def grados_desde_el_este(x_centro, y_centro, x_punto, y_punto):
    # Recibe el vértice y un punto sobre un lado.
    # Mide el ángulo como lo pide el lienzo: 0° hacia el este.
    # Devuelve los grados.
    subida=y_centro-y_punto
    avance=x_punto-x_centro
    return math.degrees(math.atan2(subida, avance))

def diferencia_menor(grado_1, grado_2):
    # Recibe dos ángulos en grados.
    # Calcula el giro más corto del primero al segundo.
    # Devuelve un número entre -180 y 180.
    diferencia=grado_2-grado_1
    while diferencia>180:
        diferencia=diferencia-360
    while diferencia<=-180:
        diferencia=diferencia+360
    return diferencia

def dibujar_arco(lienzo, x_centro, y_centro, x1, y1, x2, y2, radio, color):
    # Recibe el vértice, un punto de cada lado y el radio.
    # Dibuja el arco del ángulo interior.
    # No devuelve nada.
    grado_1=grados_desde_el_este(x_centro, y_centro, x1, y1)
    grado_2=grados_desde_el_este(x_centro, y_centro, x2, y2)
    giro=diferencia_menor(grado_1, grado_2)
    lienzo.create_arc(
        x_centro-radio,
        y_centro-radio,
        x_centro+radio,
        y_centro+radio,
        start=grado_1,
        extent=giro,
        style="arc",
        outline=color,
        width=2,
    )

def dibujar_rayitas_del_lado(lienzo, x1, y1, x2, y2, cantidad, color):
    # Recibe los extremos de un lado, cuántas rayitas van y el color.
    # Dibuja una, dos o tres rayitas cruzadas en la mitad del lado.
    # No devuelve nada.
    largo=distancia(x1, y1, x2, y2)
    if largo==0:
        return
    ux=(x2-x1)/largo
    uy=(y2-y1)/largo
    px=-uy
    py=ux
    medio_x=(x1+x2)/2
    medio_y=(y1+y2)/2
    separacion=8
    inicio=-((cantidad-1)*separacion)/2
    indice=0
    while indice<cantidad:
        desplazamiento=inicio+indice*separacion
        cx=medio_x+ux*desplazamiento
        cy=medio_y+uy*desplazamiento
        linea(lienzo, cx-px*11, cy-py*11, cx+px*11, cy+py*11, color, 3)
        indice=indice+1

def vecinos_del_vertice(triangulo, vertice):
    # Recibe el triángulo y un vértice, por ejemplo "B".
    # Busca los otros dos vértices, que son los lados del ángulo.
    # Devuelve esos dos nombres.
    if triangulo=="ABC":
        if vertice=="A":
            return ["B", "C"]
        if vertice=="B":
            return ["C", "A"]
        return ["A", "B"]
    if vertice=="D":
        return ["E", "F"]
    if vertice=="E":
        return ["F", "D"]
    return ["D", "E"]

def color_de_la_marca(indice):
    # Recibe el número de la marca, empezando en 0.
    # Elige un color. Si se acaban, vuelve al primero.
    # Devuelve el color, por ejemplo "#c1121f".
    indice_color=indice
    total=len(colores_de_marca)
    while indice_color>=total:
        indice_color=indice_color-total
    return colores_de_marca[indice_color]

def cantidad_de_rayitas(numero):
    # Recibe 1 para la primera marca de ese tipo, 2 para la segunda, y así.
    # Usa una, dos o tres rayitas y después repite.
    # Devuelve 1, 2 o 3.
    cantidad=numero
    while cantidad>3:
        cantidad=cantidad-3
    return cantidad

def dibujar_lado_marcado(lienzo, ancho, alto, triangulo, nombre, cantidad, color):
    # Recibe el lado, por ejemplo "AB", y cuántas rayitas lleva.
    # Las dibuja en la mitad de ese lado.
    # No devuelve nada.
    puntos=puntos_de_un_triangulo(triangulo, ancho, alto)
    p1=puntos[nombre[0]]
    p2=puntos[nombre[1]]
    dibujar_rayitas_del_lado(lienzo, p1[0], p1[1], p2[0], p2[1], cantidad, color)

def dibujar_angulo_marcado(lienzo, ancho, alto, triangulo, vertice, cantidad, color):
    # Recibe el vértice, por ejemplo "B", y cuántos arcos lleva.
    # Dibuja los arcos del ángulo en ese vértice.
    # No devuelve nada.
    puntos=puntos_de_un_triangulo(triangulo, ancho, alto)
    vecinos=vecinos_del_vertice(triangulo, vertice)
    origen=puntos[vertice]
    p1=puntos[vecinos[0]]
    p2=puntos[vecinos[1]]
    radio=16
    indice=0
    while indice<cantidad:
        dibujar_arco(lienzo, origen[0], origen[1], p1[0], p1[1], p2[0], p2[1], radio, color)
        radio=radio+8
        indice=indice+1

def dibujar_marcas(lienzo, ancho, alto, marcas):
    # Recibe el lienzo, el tamaño y la lista de marcas.
    # Dibuja cada par con el mismo color: rayitas en los lados y arcos en los ángulos.
    # No devuelve nada.
    numero_de_lado=0
    numero_de_angulo=0
    indice=0
    for marca in marcas:
        color=color_de_la_marca(indice)
        if marca["tipo"]=="lado":
            numero_de_lado=numero_de_lado+1
            cantidad=cantidad_de_rayitas(numero_de_lado)
            dibujar_lado_marcado(lienzo, ancho, alto, "ABC", marca["parte_abc"], cantidad, color)
            dibujar_lado_marcado(lienzo, ancho, alto, "DEF", marca["parte_def"], cantidad, color)
        else:
            numero_de_angulo=numero_de_angulo+1
            cantidad=cantidad_de_rayitas(numero_de_angulo)
            dibujar_angulo_marcado(lienzo, ancho, alto, "ABC", marca["parte_abc"], cantidad, color)
            dibujar_angulo_marcado(lienzo, ancho, alto, "DEF", marca["parte_def"], cantidad, color)
        indice=indice+1

def dibujar_parte_resaltada(lienzo, ancho, alto, parte, color):
    # Recibe la parte elegida, por ejemplo el lado AB.
    # La dibuja más gruesa para que se note el clic.
    # No devuelve nada.
    puntos=puntos_de_un_triangulo(parte["triangulo"], ancho, alto)
    if parte["tipo"]=="lado":
        nombre=parte["nombre"]
        p1=puntos[nombre[0]]
        p2=puntos[nombre[1]]
        linea(lienzo, p1[0], p1[1], p2[0], p2[1], color, 6)
        return
    letras=letras_de_los_vertices(puntos)
    letra=letras[parte["nombre"]]
    radio=16
    lienzo.create_oval(letra[0]-radio, letra[1]-radio, letra[0]+radio, letra[1]+radio, outline=color, width=3)
    escribir(lienzo, letra[0], letra[1], parte["nombre"], color, 16)

def letra_bajo_el_clic(x, y, ancho, alto):
    # Recibe el clic y el tamaño del lienzo.
    # Busca si el clic cayó sobre la letra de un ángulo.
    # Devuelve el triángulo y el nombre. Si no cayó en una letra, devuelve None.
    mejor=None
    mejor_distancia=radio_de_la_letra
    grupos=[]
    grupos.append(["ABC", vertices_abc(ancho, alto)])
    grupos.append(["DEF", vertices_def(ancho, alto)])
    for grupo in grupos:
        triangulo=grupo[0]
        letras=letras_de_los_vertices(grupo[1])
        for nombre in letras:
            dist=distancia(x, y, letras[nombre][0], letras[nombre][1])
            if dist<=mejor_distancia:
                mejor_distancia=dist
                mejor={}
                mejor["triangulo"]=triangulo
                mejor["tipo"]="angulo"
                mejor["nombre"]=nombre
    return mejor

def lado_bajo_el_clic(x, y, ancho, alto):
    # Recibe el clic y el tamaño del lienzo.
    # Busca si el clic cayó sobre la línea de un lado.
    # Devuelve el triángulo y el nombre. Si no cayó en un lado, devuelve None.
    mejor=None
    mejor_distancia=distancia_maxima_al_lado
    grupos=[]
    grupos.append(["ABC", vertices_abc(ancho, alto), lados_abc()])
    grupos.append(["DEF", vertices_def(ancho, alto), lados_def()])
    for grupo in grupos:
        triangulo=grupo[0]
        puntos=grupo[1]
        nombres=grupo[2]
        for nombre in nombres:
            p1=puntos[nombre[0]]
            p2=puntos[nombre[1]]
            dist=distancia_al_segmento(x, y, p1[0], p1[1], p2[0], p2[1])
            if dist<=mejor_distancia:
                mejor_distancia=dist
                mejor={}
                mejor["triangulo"]=triangulo
                mejor["tipo"]="lado"
                mejor["nombre"]=nombre
    return mejor

def parte_bajo_el_clic(x, y, ancho, alto):
    # Recibe el clic y el tamaño del lienzo.
    # Mira primero las letras. Si no tocó una letra, mira los lados.
    # Devuelve el triángulo, el tipo y el nombre. Si el clic cayó fuera, devuelve None.
    parte=letra_bajo_el_clic(x, y, ancho, alto)
    if parte!=None:
        return parte
    return lado_bajo_el_clic(x, y, ancho, alto)

def dibujar_triangulo_fijo(lienzo, a, b, c, color):
    # Recibe tres puntos y el color.
    # Dibuja un triángulo pequeño para un concepto.
    # No devuelve nada.
    linea(lienzo, a[0], a[1], b[0], b[1], color, 3)
    linea(lienzo, b[0], b[1], c[0], c[1], color, 3)
    linea(lienzo, c[0], c[1], a[0], a[1], color, 3)

def dibujar_esquema_congruencia(lienzo):
    # Recibe el lienzo del concepto.
    # Dibuja dos triángulos con las mismas marcas en los lados correspondientes.
    # No devuelve nada.
    a=(110, 36)
    b=(36, 168)
    c=(190, 176)
    d=(390, 36)
    e=(316, 168)
    f=(470, 176)
    dibujar_triangulo_fijo(lienzo, a, b, c, color_linea)
    dibujar_triangulo_fijo(lienzo, d, e, f, color_linea)
    escribir(lienzo, 90, 24, "A", color_linea, 13)
    escribir(lienzo, 24, 182, "B", color_linea, 13)
    escribir(lienzo, 206, 188, "C", color_linea, 13)
    escribir(lienzo, 390, 24, "D", color_linea, 13)
    escribir(lienzo, 300, 182, "E", color_linea, 13)
    escribir(lienzo, 486, 188, "F", color_linea, 13)
    dibujar_rayitas_del_lado(lienzo, a[0], a[1], b[0], b[1], 1, "#c1121f")
    dibujar_rayitas_del_lado(lienzo, d[0], d[1], e[0], e[1], 1, "#c1121f")
    dibujar_rayitas_del_lado(lienzo, b[0], b[1], c[0], c[1], 2, "#2f6fed")
    dibujar_rayitas_del_lado(lienzo, e[0], e[1], f[0], f[1], 2, "#2f6fed")
    dibujar_rayitas_del_lado(lienzo, c[0], c[1], a[0], a[1], 3, "#2d6a4f")
    dibujar_rayitas_del_lado(lienzo, f[0], f[1], d[0], d[1], 3, "#2d6a4f")
    escribir(lienzo, 260, 210, "△ABC ≅ △DEF", color_linea, 13)

def dibujar_esquema_correspondencia(lienzo):
    # Recibe el lienzo del concepto.
    # Pinta del mismo color las letras que se corresponden.
    # No devuelve nada.
    a=(110, 50)
    b=(36, 170)
    c=(190, 178)
    d=(400, 50)
    e=(326, 170)
    f=(480, 178)
    dibujar_triangulo_fijo(lienzo, a, b, c, color_linea)
    dibujar_triangulo_fijo(lienzo, d, e, f, color_linea)
    escribir(lienzo, 110, 28, "A", "#c1121f", 14)
    escribir(lienzo, 400, 28, "D", "#c1121f", 14)
    escribir(lienzo, 20, 186, "B", "#2f6fed", 14)
    escribir(lienzo, 310, 186, "E", "#2f6fed", 14)
    escribir(lienzo, 206, 194, "C", "#2d6a4f", 14)
    escribir(lienzo, 496, 194, "F", "#2d6a4f", 14)
    escribir(lienzo, 260, 100, "A con D", "#c1121f", 12)
    escribir(lienzo, 260, 126, "B con E", "#2f6fed", 12)
    escribir(lienzo, 260, 152, "C con F", "#2d6a4f", 12)

def dibujar_esquema_lll(lienzo):
    # Recibe el lienzo del concepto.
    # Muestra los tres pares de lados que pide LLL.
    # No devuelve nada.
    a=(100, 40)
    b=(30, 160)
    c=(180, 168)
    d=(380, 40)
    e=(310, 160)
    f=(460, 168)
    dibujar_triangulo_fijo(lienzo, a, b, c, color_linea)
    dibujar_triangulo_fijo(lienzo, d, e, f, color_linea)
    dibujar_rayitas_del_lado(lienzo, a[0], a[1], b[0], b[1], 1, "#c1121f")
    dibujar_rayitas_del_lado(lienzo, d[0], d[1], e[0], e[1], 1, "#c1121f")
    dibujar_rayitas_del_lado(lienzo, b[0], b[1], c[0], c[1], 2, "#2f6fed")
    dibujar_rayitas_del_lado(lienzo, e[0], e[1], f[0], f[1], 2, "#2f6fed")
    dibujar_rayitas_del_lado(lienzo, c[0], c[1], a[0], a[1], 3, "#2d6a4f")
    dibujar_rayitas_del_lado(lienzo, f[0], f[1], d[0], d[1], 3, "#2d6a4f")
    escribir(lienzo, 260, 210, "AB ≅ DE,  BC ≅ EF,  CA ≅ FD", color_linea, 12)

def dibujar_esquema_lal(lienzo):
    # Recibe el lienzo del concepto.
    # Resalta dos lados y el ángulo comprendido.
    # No devuelve nada.
    a=(100, 36)
    b=(36, 168)
    c=(196, 150)
    d=(390, 36)
    e=(326, 168)
    f=(486, 150)
    linea(lienzo, a[0], a[1], b[0], b[1], "#c1121f", 4)
    linea(lienzo, b[0], b[1], c[0], c[1], "#2f6fed", 4)
    linea(lienzo, c[0], c[1], a[0], a[1], color_suave, 2)
    linea(lienzo, d[0], d[1], e[0], e[1], "#c1121f", 4)
    linea(lienzo, e[0], e[1], f[0], f[1], "#2f6fed", 4)
    linea(lienzo, f[0], f[1], d[0], d[1], color_suave, 2)
    dibujar_arco(lienzo, b[0], b[1], a[0], a[1], c[0], c[1], 22, "#9a3412")
    dibujar_arco(lienzo, e[0], e[1], d[0], d[1], f[0], f[1], 22, "#9a3412")
    escribir(lienzo, 70, 20, "A", color_linea, 12)
    escribir(lienzo, 20, 186, "B", "#9a3412", 12)
    escribir(lienzo, 210, 150, "C", color_linea, 12)
    escribir(lienzo, 390, 20, "D", color_linea, 12)
    escribir(lienzo, 310, 186, "E", "#9a3412", 12)
    escribir(lienzo, 500, 150, "F", color_linea, 12)
    escribir(lienzo, 260, 210, "∠B está entre AB y BC", color_linea, 12)

def dibujar_esquema_ala(lienzo):
    # Recibe el lienzo del concepto.
    # Resalta dos ángulos y el lado comprendido.
    # No devuelve nada.
    a=(110, 40)
    b=(36, 170)
    c=(190, 176)
    d=(400, 40)
    e=(326, 170)
    f=(480, 176)
    linea(lienzo, a[0], a[1], b[0], b[1], "#2d6a4f", 4)
    linea(lienzo, b[0], b[1], c[0], c[1], color_suave, 2)
    linea(lienzo, c[0], c[1], a[0], a[1], color_suave, 2)
    linea(lienzo, d[0], d[1], e[0], e[1], "#2d6a4f", 4)
    linea(lienzo, e[0], e[1], f[0], f[1], color_suave, 2)
    linea(lienzo, f[0], f[1], d[0], d[1], color_suave, 2)
    dibujar_arco(lienzo, a[0], a[1], b[0], b[1], c[0], c[1], 22, "#c1121f")
    dibujar_arco(lienzo, b[0], b[1], a[0], a[1], c[0], c[1], 22, "#2f6fed")
    dibujar_arco(lienzo, d[0], d[1], e[0], e[1], f[0], f[1], 22, "#c1121f")
    dibujar_arco(lienzo, e[0], e[1], d[0], d[1], f[0], f[1], 22, "#2f6fed")
    escribir(lienzo, 110, 18, "A", "#c1121f", 12)
    escribir(lienzo, 18, 186, "B", "#2f6fed", 12)
    escribir(lienzo, 400, 18, "D", "#c1121f", 12)
    escribir(lienzo, 308, 186, "E", "#2f6fed", 12)
    escribir(lienzo, 260, 210, "AB está entre ∠A y ∠B", color_linea, 12)

def dibujar_esquema_aaa(lienzo):
    # Recibe el lienzo del concepto.
    # Dibuja dos triángulos con los mismos ángulos y distinto tamaño.
    # No devuelve nada.
    a=(120, 70)
    b=(70, 150)
    c=(170, 150)
    d=(400, 36)
    e=(300, 190)
    f=(500, 190)
    dibujar_triangulo_fijo(lienzo, a, b, c, color_linea)
    dibujar_triangulo_fijo(lienzo, d, e, f, color_linea)
    dibujar_arco(lienzo, a[0], a[1], b[0], b[1], c[0], c[1], 16, "#c1121f")
    dibujar_arco(lienzo, d[0], d[1], e[0], e[1], f[0], f[1], 16, "#c1121f")
    dibujar_arco(lienzo, b[0], b[1], a[0], a[1], c[0], c[1], 16, "#2f6fed")
    dibujar_arco(lienzo, e[0], e[1], d[0], d[1], f[0], f[1], 16, "#2f6fed")
    dibujar_arco(lienzo, c[0], c[1], a[0], a[1], b[0], b[1], 16, "#2d6a4f")
    dibujar_arco(lienzo, f[0], f[1], d[0], d[1], e[0], e[1], 16, "#2d6a4f")
    escribir(lienzo, 260, 214, "mismos ángulos, distinto tamaño", color_linea, 12)

def dibujar_esquema_dado(lienzo):
    # Recibe el lienzo del concepto.
    # Muestra un dato del enunciado, listo para copiarlo en la tabla.
    # No devuelve nada.
    a=(90, 36)
    b=(30, 130)
    c=(160, 130)
    d=(250, 36)
    e=(210, 130)
    f=(340, 130)
    dibujar_triangulo_fijo(lienzo, a, b, c, color_linea)
    dibujar_triangulo_fijo(lienzo, d, e, f, color_linea)
    dibujar_rayitas_del_lado(lienzo, a[0], a[1], b[0], b[1], 1, "#c1121f")
    dibujar_rayitas_del_lado(lienzo, d[0], d[1], e[0], e[1], 1, "#c1121f")
    escribir(lienzo, 70, 20, "A", color_linea, 12)
    escribir(lienzo, 18, 146, "B", color_linea, 12)
    escribir(lienzo, 250, 20, "D", color_linea, 12)
    escribir(lienzo, 196, 146, "E", color_linea, 12)
    lienzo.create_rectangle(360, 70, 530, 150, outline=color_linea, width=2, fill="#fff7e6")
    escribir(lienzo, 445, 96, "Afirmación", color_suave, 11)
    escribir(lienzo, 445, 122, "AB ≅ DE", color_linea, 13)
    escribir(lienzo, 260, 200, "Razón: Dado", color_linea, 13)

def dibujar_esquema_bisectriz(lienzo):
    # Recibe el lienzo del concepto.
    # Dibuja un ángulo partido en dos ángulos iguales.
    # No devuelve nada.
    a=(260, 200)
    b=(40, 36)
    c=(490, 46)
    m=(270, 24)
    linea(lienzo, a[0], a[1], b[0], b[1], color_linea, 3)
    linea(lienzo, a[0], a[1], c[0], c[1], color_linea, 3)
    linea(lienzo, a[0], a[1], m[0], m[1], "#c1121f", 3)
    dibujar_arco(lienzo, a[0], a[1], b[0], b[1], m[0], m[1], 36, "#2f6fed")
    dibujar_arco(lienzo, a[0], a[1], m[0], m[1], c[0], c[1], 36, "#2f6fed")
    escribir(lienzo, 236, 214, "A", color_linea, 13)
    escribir(lienzo, 40, 20, "B", color_linea, 13)
    escribir(lienzo, 500, 30, "C", color_linea, 13)
    escribir(lienzo, 290, 16, "bisectriz", "#c1121f", 12)

def dibujar_esquema_punto_medio(lienzo):
    # Recibe el lienzo del concepto.
    # Dibuja un segmento partido en dos partes iguales.
    # No devuelve nada.
    a=(50, 110)
    m=(260, 110)
    b=(470, 110)
    linea(lienzo, a[0], a[1], b[0], b[1], color_linea, 3)
    lienzo.create_oval(m[0]-5, m[1]-5, m[0]+5, m[1]+5, fill=color_linea, outline=color_linea)
    dibujar_rayitas_del_lado(lienzo, a[0], a[1], m[0], m[1], 1, "#c1121f")
    dibujar_rayitas_del_lado(lienzo, m[0], m[1], b[0], b[1], 1, "#c1121f")
    escribir(lienzo, 50, 80, "A", color_linea, 14)
    escribir(lienzo, 260, 78, "M", "#c1121f", 14)
    escribir(lienzo, 470, 80, "B", color_linea, 14)
    escribir(lienzo, 260, 170, "AM ≅ MB", color_linea, 14)

def dibujar_esquema_lado_comun(lienzo):
    # Recibe el lienzo del concepto.
    # Dibuja dos triángulos que comparten el lado AC.
    # No devuelve nada.
    a=(260, 30)
    c=(260, 190)
    d=(70, 110)
    b=(460, 120)
    linea(lienzo, a[0], a[1], d[0], d[1], color_linea, 3)
    linea(lienzo, d[0], d[1], c[0], c[1], color_linea, 3)
    linea(lienzo, a[0], a[1], b[0], b[1], color_linea, 3)
    linea(lienzo, b[0], b[1], c[0], c[1], color_linea, 3)
    linea(lienzo, a[0], a[1], c[0], c[1], "#c1121f", 4)
    escribir(lienzo, 260, 16, "A", color_linea, 13)
    escribir(lienzo, 276, 206, "C", color_linea, 13)
    escribir(lienzo, 52, 110, "D", color_linea, 13)
    escribir(lienzo, 478, 120, "B", color_linea, 13)
    escribir(lienzo, 300, 110, "lado común", "#c1121f", 12)

def dibujar_esquema_reflexiva(lienzo):
    # Recibe el lienzo del concepto.
    # Muestra un segmento que es congruente consigo mismo.
    # No devuelve nada.
    a=(80, 100)
    c=(460, 100)
    linea(lienzo, a[0], a[1], c[0], c[1], "#c1121f", 4)
    escribir(lienzo, 80, 70, "A", color_linea, 14)
    escribir(lienzo, 460, 70, "C", color_linea, 14)
    escribir(lienzo, 270, 150, "AC ≅ AC", color_linea, 16)

def dibujar_esquema_perpendicular(lienzo):
    # Recibe el lienzo del concepto.
    # Dibuja dos rectas que se cortan en ángulo recto.
    # No devuelve nada.
    linea(lienzo, 40, 120, 500, 120, color_linea, 3)
    linea(lienzo, 270, 24, 270, 210, color_linea, 3)
    linea(lienzo, 270, 96, 294, 96, "#c1121f", 2)
    linea(lienzo, 294, 96, 294, 120, "#c1121f", 2)
    escribir(lienzo, 250, 36, "A", color_linea, 13)
    escribir(lienzo, 250, 200, "D", color_linea, 13)
    escribir(lienzo, 56, 100, "B", color_linea, 13)
    escribir(lienzo, 490, 100, "C", color_linea, 13)
    escribir(lienzo, 400, 70, "90°", "#c1121f", 14)

def dibujar_esquema_opuestos(lienzo):
    # Recibe el lienzo del concepto.
    # Dibuja dos rectas que se cruzan y marca los ángulos opuestos.
    # No devuelve nada.
    izquierda_arriba=(70, 36)
    derecha_abajo=(470, 200)
    izquierda_abajo=(70, 200)
    derecha_arriba=(470, 36)
    centro=(270, 118)
    linea(lienzo, izquierda_arriba[0], izquierda_arriba[1], derecha_abajo[0], derecha_abajo[1], color_linea, 3)
    linea(lienzo, izquierda_abajo[0], izquierda_abajo[1], derecha_arriba[0], derecha_arriba[1], color_linea, 3)
    dibujar_arco(lienzo, centro[0], centro[1], izquierda_arriba[0], izquierda_arriba[1], izquierda_abajo[0], izquierda_abajo[1], 28, "#c1121f")
    dibujar_arco(lienzo, centro[0], centro[1], derecha_abajo[0], derecha_abajo[1], derecha_arriba[0], derecha_arriba[1], 28, "#c1121f")
    escribir(lienzo, 270, 214, "ángulos opuestos por el vértice", color_linea, 12)

def dibujar_concepto(lienzo, clave):
    # Recibe el lienzo y la clave, por ejemplo "bisectriz".
    # Borra el esquema anterior y dibuja el concepto pedido.
    # No devuelve nada.
    lienzo.delete("all")
    if clave=="congruencia":
        dibujar_esquema_congruencia(lienzo)
    elif clave=="correspondencia":
        dibujar_esquema_correspondencia(lienzo)
    elif clave=="lll":
        dibujar_esquema_lll(lienzo)
    elif clave=="lal":
        dibujar_esquema_lal(lienzo)
    elif clave=="ala":
        dibujar_esquema_ala(lienzo)
    elif clave=="aaa":
        dibujar_esquema_aaa(lienzo)
    elif clave=="dado":
        dibujar_esquema_dado(lienzo)
    elif clave=="bisectriz":
        dibujar_esquema_bisectriz(lienzo)
    elif clave=="punto_medio":
        dibujar_esquema_punto_medio(lienzo)
    elif clave=="lado_comun":
        dibujar_esquema_lado_comun(lienzo)
    elif clave=="reflexiva":
        dibujar_esquema_reflexiva(lienzo)
    elif clave=="perpendicular":
        dibujar_esquema_perpendicular(lienzo)
    elif clave=="opuestos":
        dibujar_esquema_opuestos(lienzo)
    else:
        escribir(lienzo, 260, 110, "Sin dibujo", color_linea, 14)
