# Prueba temporal de los criterios y de los clics.
# Se borra después de correr.

from geometria.criterios import (
    se_cumple_lll,
    se_cumple_lal,
    se_cumple_ala,
    criterios_que_se_cumplen,
    razon_de_la_congruencia,
    filas_de_la_comprobacion,
    texto_del_resultado,
)
from geometria.conceptos import lista_de_conceptos
from geometria.dibujos import (
    vertices_abc,
    vertices_def,
    letras_de_los_vertices,
    punto_medio,
    parte_bajo_el_clic,
)


def marca(tipo, parte_abc, parte_def, razon="Dado"):
    # Arma una marca como las que guarda la pantalla.
    hecha={}
    hecha["tipo"]=tipo
    hecha["parte_abc"]=parte_abc
    hecha["parte_def"]=parte_def
    hecha["razon"]=razon
    return hecha


def revisar(condicion, mensaje):
    # Si la condición falla, corta la prueba con un mensaje claro.
    if condicion==False:
        raise SystemExit("FALLO: "+mensaje)


lll=[
    marca("lado", "AB", "DE"),
    marca("lado", "BC", "EF"),
    marca("lado", "CA", "FD"),
]
revisar(se_cumple_lll(lll), "tres lados deberían cumplir LLL")
revisar(se_cumple_lal(lll)==False, "tres lados no son LAL")
revisar(se_cumple_ala(lll)==False, "tres lados no son ALA")
revisar(razon_de_la_congruencia(lll)=="Criterio LLL", "la razón de tres lados es LLL")
revisar(filas_de_la_comprobacion(lll)[-1][1]=="Criterio LLL", "la última fila de LLL")

lal=[
    marca("lado", "AB", "DE"),
    marca("angulo", "B", "E"),
    marca("lado", "BC", "EF"),
]
revisar(se_cumple_lal(lal), "AB, ángulo B y BC deberían cumplir LAL")
revisar(se_cumple_lll(lal)==False, "LAL no es LLL")
revisar(se_cumple_ala(lal)==False, "ese LAL no es ALA")
revisar("criterio LAL" in texto_del_resultado(lal), "el texto de LAL")

lal_en_a=[
    marca("lado", "CA", "FD"),
    marca("angulo", "A", "D"),
    marca("lado", "AB", "DE"),
]
revisar(se_cumple_lal(lal_en_a), "LAL en el ángulo A")

ala=[
    marca("angulo", "A", "D"),
    marca("lado", "AB", "DE"),
    marca("angulo", "B", "E"),
]
revisar(se_cumple_ala(ala), "ángulos A y B con el lado AB deberían cumplir ALA")
revisar(se_cumple_lal(ala)==False, "ese ALA no es LAL")
revisar(se_cumple_lll(ala)==False, "ALA no es LLL")
revisar(filas_de_la_comprobacion(ala)[-1]==["△ABC ≅ △DEF", "Criterio ALA"], "fila final de ALA")

incompleto=[marca("lado", "AB", "DE")]
revisar(se_cumple_lll(incompleto)==False, "un lado no es LLL")
revisar(se_cumple_lal(incompleto)==False, "un lado no es LAL")
revisar(se_cumple_ala(incompleto)==False, "un lado no es ALA")
texto_incompleto=texto_del_resultado(incompleto)
revisar("no hay información suficiente" in texto_incompleto, "falta información")
revisar("Lados correspondientes: 1 de 3." in texto_incompleto, "cuenta de lados")
revisar("Ángulos correspondientes: 0 de 3." in texto_incompleto, "cuenta de ángulos")

sin_marcas=texto_del_resultado([])
revisar("Todavía no hay marcas" in sin_marcas, "tabla vacía")

malo=[marca("lado", "AB", "EF")]
texto_malo=texto_del_resultado(malo)
revisar("AB no corresponde a EF" in texto_malo, "lado que no corresponde")
revisar("corresponde a DE" in texto_malo, "dice el lado correcto")
revisar(se_cumple_lll(malo)==False, "un lado cruzado no es LLL")

angulo_malo=[marca("angulo", "A", "F")]
texto_angulo=texto_del_resultado(angulo_malo)
revisar("no corresponde a" in texto_angulo, "ángulo que no corresponde")
revisar("corresponde a D" in texto_angulo, "dice el ángulo correcto")

ambos=lll+[marca("angulo", "B", "E")]
nombres=criterios_que_se_cumplen(ambos)
revisar(nombres[0]=="LLL", "si hay varios, la tabla usa LLL primero")
revisar("LAL" in nombres, "también se nota LAL")
revisar("También se cumple LAL" in texto_del_resultado(ambos), "frase de los otros criterios")

revisar(len(lista_de_conceptos())==13, "faltan conceptos")
print("Criterios: bien")

import interfaz
from geometria import pantalla

ventana=interfaz.crear_ventana()
ventana.update_idletasks()
ventana.update()
revisar(ventana.title()=="Matemáticas 8C", "título de la ventana")

interfaz.mostrar_geometria()
ventana.update()
for concepto in lista_de_conceptos():
    pantalla.mostrar_un_concepto(concepto["nombre"])
    ventana.update()
    revisar(pantalla.titulo_concepto.cget("text")==concepto["nombre"], "título "+concepto["nombre"])
    revisar(len(pantalla.lienzo_concepto.find_all())>0, "dibujo "+concepto["nombre"])
print("Conceptos: bien")

pantalla.ir_a_comparar()
ventana.update()
pantalla.borrar_marcas()
ventana.update()

def figuras_actuales():
    # Lee el tamaño del lienzo en este momento y calcula los dos triángulos.
    ancho, alto=pantalla.tamano_usado()
    abc=vertices_abc(ancho, alto)
    otro=vertices_def(ancho, alto)
    return ancho, alto, abc, otro


def clic_en(punto):
    # Hace el mismo clic que el ratón en ese punto del lienzo.
    pantalla.procesar_clic(punto[0], punto[1])
    ventana.update()


def clic_lado(triangulo, vertice_1, vertice_2):
    # Calcula el medio del lado con el tamaño actual y hace clic ahí.
    ancho, alto, abc, otro=figuras_actuales()
    if triangulo=="ABC":
        punto=punto_medio(abc[vertice_1], abc[vertice_2])
    else:
        punto=punto_medio(otro[vertice_1], otro[vertice_2])
    parte=parte_bajo_el_clic(punto[0], punto[1], ancho, alto)
    if parte==None:
        raise SystemExit("FALLO: no encontré el lado "+vertice_1+vertice_2)
    clic_en(punto)


def clic_angulo(triangulo, vertice):
    # Calcula la letra con el tamaño actual y hace clic ahí.
    ancho, alto, abc, otro=figuras_actuales()
    if triangulo=="ABC":
        letras=letras_de_los_vertices(abc)
    else:
        letras=letras_de_los_vertices(otro)
    punto=letras[vertice]
    parte=parte_bajo_el_clic(punto[0], punto[1], ancho, alto)
    if parte==None or parte["nombre"]!=vertice:
        raise SystemExit("FALLO: no encontré el ángulo "+vertice)
    clic_en(punto)


ancho, alto, abc, otro=figuras_actuales()
medio_ab=punto_medio(abc["A"], abc["B"])
revisar(parte_bajo_el_clic(medio_ab[0], medio_ab[1], ancho, alto)["nombre"]=="AB", "el clic del medio cae en AB")
letra_b=letras_de_los_vertices(abc)["B"]
revisar(parte_bajo_el_clic(letra_b[0], letra_b[1], ancho, alto)["nombre"]=="B", "el clic de la letra cae en B")

clic_lado("ABC", "A", "B")
clic_lado("ABC", "B", "C")
revisar("mismo triángulo" in pantalla.obtener_aviso(), "aviso de mismo triángulo")
revisar(len(pantalla.obtener_marcas())==0, "mismo triángulo no agrega fila")
pantalla.borrar_marcas()

clic_lado("ABC", "A", "B")
clic_angulo("DEF", "D")
revisar("Un lado se compara con un lado" in pantalla.obtener_aviso(), "aviso de lado con ángulo")
revisar(len(pantalla.obtener_marcas())==0, "lado con ángulo no agrega fila")

clic_lado("DEF", "D", "E")
pantalla.confirmar_razon("Dado")
clic_lado("ABC", "A", "B")
clic_lado("DEF", "D", "E")
pantalla.confirmar_razon("Punto medio")
revisar(len(pantalla.obtener_marcas())==1, "repetir el par no duplica la fila")
revisar(pantalla.obtener_marcas()[0]["razon"]=="Punto medio", "cambia la razón")
clic_lado("ABC", "A", "B")
clic_lado("DEF", "D", "E")
pantalla.confirmar_razon("Dado")

clic_angulo("ABC", "B")
clic_angulo("DEF", "E")
pantalla.confirmar_razon("Bisectriz")

clic_lado("ABC", "B", "C")
clic_lado("DEF", "E", "F")
pantalla.confirmar_razon("Punto medio")
ventana.update()

filas=pantalla.obtener_filas()
revisar(filas[0]==["AB ≅ DE", "Dado"], "primera fila")
revisar(filas[1]==["∠B ≅ ∠E", "Bisectriz"], "fila del ángulo")
revisar(filas[2]==["BC ≅ EF", "Punto medio"], "fila del segundo lado")
revisar(filas[-1]==["△ABC ≅ △DEF", "Criterio LAL"], "fila de la congruencia")
revisar("criterio LAL" in pantalla.obtener_texto_resultado(), "resultado LAL")

textos=[]
for hijo in pantalla.marco_filas.winfo_children():
    textos.append(hijo.cget("text"))
revisar("Afirmación" in textos, "encabezado afirmación")
revisar("Razón" in textos, "encabezado razón")
revisar("△ABC ≅ △DEF" in textos, "la tabla dibuja la congruencia")
revisar(len(pantalla.lienzo_comparar.find_all())>6, "el lienzo tiene los triángulos y las marcas")

clic_lado("ABC", "C", "A")
clic_lado("DEF", "E", "F")
pantalla.confirmar_razon("Dado")
texto=pantalla.obtener_texto_resultado()
revisar("CA no corresponde a EF" in texto, "avisa el lado que no corresponde")
revisar("corresponde a FD" in texto, "dice que CA va con FD")
revisar(len(pantalla.obtener_filas())==5, "la fila mala queda en la tabla")

pantalla.quitar_ultima_marca()
ventana.update()
filas=pantalla.obtener_filas()
revisar(len(filas)==4, "quitar última saca la fila mala")
revisar(filas[-1][1]=="Criterio LAL", "sigue cumpliéndose LAL")
revisar("no corresponde" not in pantalla.obtener_texto_resultado(), "ya no queda el aviso del lado cruzado")

pantalla.procesar_clic(2, 2)
ventana.update()
revisar("Haz clic sobre la línea" in pantalla.obtener_aviso(), "clic fuera de las figuras")

interfaz.mostrar_menu()
ventana.update()
revisar(interfaz.marco_menu.winfo_ismapped(), "volvió el menú de factorización")
revisar(interfaz.marco_geometria.winfo_ismapped()==False, "se escondió la geometría")
revisar(interfaz.marco_factorizar.winfo_ismapped()==False, "la factorización sigue escondida")

ventana.destroy()
print("Clics: bien")
