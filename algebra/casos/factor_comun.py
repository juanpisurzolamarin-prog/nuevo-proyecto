# Caso de factor común.
# Este archivo no agrupa términos. La agrupación está en casos/agrupacion.py.

import math
from collections import Counter
from algebra.expresiones import obtener_coeficiente, obtener_letras, letras_a_texto


def encontrar_mcd(division_de_datos):
    # Recibe los términos, por ejemplo ["6x^2","9xy"].
    # Toma el número de cada término, sin el signo.
    # Devuelve el máximo común divisor de esos números.
    conjunto_de_numeros=[]
    for parte in division_de_datos:
        conjunto_de_numeros.append(abs(obtener_coeficiente(parte)))
    mcd=conjunto_de_numeros[0]
    for numero in conjunto_de_numeros[1:]:
        mcd=math.gcd(mcd,numero)
    return mcd

def potencia_de_letra(letras,letra):
    # Recibe las letras de un término y una letra, por ejemplo x.
    # Busca la potencia de esa letra.
    # Devuelve la potencia. Si la letra no está, devuelve 0.
    if letra in letras:
        return letras[letra]
    return 0

def encontrar_letras_en_comun(division_de_datos):
    # Recibe los términos, por ejemplo ["6x^3y","9x^2"].
    # Para cada letra, la potencia común es la más pequeña.
    # Si en algún término la potencia es 0, esa letra no es común.
    # Devuelve un contador. En el ejemplo, x tiene potencia 2.
    letras_de_cada_termino=[]
    for parte in division_de_datos:
        letras_de_cada_termino.append(obtener_letras(parte))

    letras_en_comun=Counter()
    primera=letras_de_cada_termino[0]
    for letra in primera:
        menor=potencia_de_letra(primera,letra)
        aparece_en_todos=True
        for letras in letras_de_cada_termino[1:]:
            potencia=potencia_de_letra(letras,letra)
            if potencia==0:
                aparece_en_todos=False
            if potencia<menor:
                menor=potencia
        if aparece_en_todos and menor>0:
            letras_en_comun[letra]=menor
    return letras_en_comun

def restar_potencias(letras_del_termino,letras_en_comun):
    # Recibe las potencias del término y las del factor común.
    # Resta las potencias, porque dividir potencias de la misma base es restar exponentes.
    # Devuelve lo que queda. Ejemplo: x^5 entre x^2 deja x^3.
    restantes=Counter()
    for letra in letras_del_termino:
        potencia=letras_del_termino[letra]
        potencia_comun=potencia_de_letra(letras_en_comun,letra)
        potencia=potencia-potencia_comun
        if potencia>0:
            restantes[letra]=potencia
    return restantes

def determinar_si_es_factor_comun(division_de_datos):
    # Recibe los términos de la expresión.
    # Revisa si hay letras en común o si el mcd de los números es mayor que 1.
    # Devuelve verdadero si la expresión tiene factor común.
    letras_en_comun=encontrar_letras_en_comun(division_de_datos)
    mcd=encontrar_mcd(division_de_datos)
    if len(letras_en_comun)>0 or mcd>1:
        return True
    else:
        return False

def calcular_factor_comun(division_de_datos):
    # Recibe los términos, por ejemplo ["xy","+2x"].
    # Saca el mcd y la menor potencia de cada letra.
    # Devuelve tres cosas: el factor de afuera, lo de adentro y las letras comunes.
    # En el ejemplo devuelve "x", "y+2" y la letra x.
    letras_en_comun=encontrar_letras_en_comun(division_de_datos)
    mcd=encontrar_mcd(division_de_datos)

    factor=""
    if mcd>1 or not letras_en_comun:
        factor=factor+str(mcd)
    factor=factor+letras_a_texto(letras_en_comun)

    interior=""
    for posicion,parte in enumerate(division_de_datos):
        coeficiente=obtener_coeficiente(parte)//mcd
        letras_que_quedan=restar_potencias(obtener_letras(parte),letras_en_comun)
        letras_restantes=letras_a_texto(letras_que_quedan)

        numero=""
        if abs(coeficiente)!=1 or letras_restantes=="":
            numero=str(abs(coeficiente))

        signo=""
        if coeficiente<0:
            signo="-"
        elif posicion>0:
            signo="+"

        interior=interior+signo+numero+letras_restantes

    return factor,interior,letras_en_comun

def resolver_factor_comun(division_de_datos):
    # Recibe los términos, por ejemplo ["8x^3y^2","-12x^2y^3"].
    # Usa calcular_factor_comun y junta el factor con el paréntesis.
    # Devuelve el resultado, por ejemplo "4x^2y^2(2x-3y)", y las letras comunes.
    factor,interior,letras_en_comun=calcular_factor_comun(division_de_datos)
    resultado=factor+"("+interior+")"
    return resultado,letras_en_comun

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos del factor común.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa cuando todos los términos comparten un número o una letra."
    texto=texto+"\n\n1. El número común es el máximo común divisor."
    texto=texto+"\n2. Si una letra está en todos los términos, se queda con la potencia más pequeña."
    texto=texto+"\n3. Al dividir, las potencias de la misma letra se restan."
    texto=texto+"\n4. El resultado es el factor de afuera y un paréntesis con lo que queda."
    texto=texto+"\n\nEjemplo: 6x² + 9xy = 3x(2x + 3y)."
    texto=texto+"\nSi toda la expresión tiene factor común, este caso se muestra primero."
    return texto
