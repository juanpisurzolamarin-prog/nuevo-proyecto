# Este archivo solo lee la expresión.
# Los casos de factorización están en la carpeta casos, dentro de álgebra.

import re
from collections import Counter


def preparar_expresion(expresion):
    # Recibe el texto de la expresión, por ejemplo "6x² + 9xy" o "x¹⁰".
    # Quita los espacios y cambia la potencia escrita arriba por ^ y el número.
    # Si hay varios números arriba seguidos, los junta: x¹⁰ queda x^10.
    # Devuelve el texto listo para leer, por ejemplo "6x^2+9xy".
    numeros_arriba={
        "⁰":"0",
        "¹":"1",
        "²":"2",
        "³":"3",
        "⁴":"4",
        "⁵":"5",
        "⁶":"6",
        "⁷":"7",
        "⁸":"8",
        "⁹":"9",
    }
    expresion=expresion.replace(" ","")
    expresion=expresion.replace("**","^")
    texto=""
    potencia=""
    for caracter in expresion:
        if caracter in numeros_arriba:
            potencia=potencia+numeros_arriba[caracter]
        else:
            if potencia!="":
                texto=texto+"^"+potencia
                potencia=""
            texto=texto+caracter
    if potencia!="":
        texto=texto+"^"+potencia
    return texto

def encontrar_el_tipo_de_expresion(expresion):
    # esta funcion recibe la expresion,
    # divide la expresion con mas y en menos (conservando el signo de cada termino)
    # reconoce la longitud de la expresion
    # los clasifica segun su tamaño
    expresion=preparar_expresion(expresion)
    division_de_datos=re.findall(r"[+-]?[^+-]+",expresion)
    longitud_de_division_de_datos=len(division_de_datos)
    tipo=""
    if longitud_de_division_de_datos ==1:
        tipo="monomio"
    if longitud_de_division_de_datos ==2:
        tipo="binomio"
    if longitud_de_division_de_datos ==3:
        tipo="trinomio"
    if longitud_de_division_de_datos >=4:
        tipo="polinomio"
    return tipo,division_de_datos

def obtener_coeficiente(termino):
    # esta funcion recibe un termino, por ejemplo "-12abe"
    # toma el signo y la parte entera del termino
    # si el termino no tiene numero (ejemplo "ab") el coeficiente es 1
    coincidencia=re.match(r"([+-]?)(\d*)",termino)
    signo=-1 if coincidencia.group(1)=="-" else 1
    numero=int(coincidencia.group(2)) if coincidencia.group(2) else 1
    return signo*numero

def obtener_letras(termino):
    # Recibe un término como "12x^2y" o "-a^2b".
    # Busca cada letra y, si tiene un ^, su potencia.
    # Devuelve un contador. En "12x^2y", x tiene potencia 2 y y tiene potencia 1.
    # Si la letra no tiene ^, la potencia es 1. Por eso "aa" cuenta como a con potencia 2.
    letras=Counter()
    encontradas=re.findall(r"([a-zA-Z])(?:\^(\d+))?",termino)
    for letra,potencia in encontradas:
        if potencia=="":
            letras[letra]=letras[letra]+1
        else:
            letras[letra]=letras[letra]+int(potencia)
    return letras

def letras_a_texto(contador):
    # Recibe un contador de letras y potencias, por ejemplo a:2 y b:1.
    # Lo convierte en texto ordenado.
    # Devuelve "a^2b". Si la potencia es 1, no escribe ^1.
    texto=""
    for letra,potencia in sorted(contador.items()):
        texto=texto+letra
        if potencia>1:
            texto=texto+"^"+str(potencia)
    return texto

def separar_terminos(texto):
    # Recibe un texto como "y+2" o "3-y".
    # Lo divide en términos y conserva el signo de cada uno.
    # Devuelve la lista de términos, por ejemplo ["y","+2"].
    return re.findall(r"[+-]?[^+-]+",texto)
