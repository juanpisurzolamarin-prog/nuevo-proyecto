# Caso de trinomio cuadrado perfecto.
# Este archivo no hace factor común ni agrupación.

from collections import Counter
from algebra.expresiones import obtener_coeficiente, obtener_letras, letras_a_texto


def raiz_de_numero(numero):
    # Recibe un número positivo, por ejemplo 9.
    # Busca un entero que multiplicado por sí mismo dé ese número.
    # Devuelve 3. Si no es un cuadrado perfecto, devuelve 0.
    if numero<=0:
        return 0
    candidato=1
    while candidato*candidato<numero:
        candidato=candidato+1
    if candidato*candidato==numero:
        return candidato
    return 0

def tiene_raiz_cuadrada(termino):
    # Recibe un término, por ejemplo "4x^2" o "-9".
    # Revisa si el número es un cuadrado perfecto y si cada potencia es par.
    # Devuelve verdadero si tiene raíz. Un término negativo no tiene raíz en este curso.
    coeficiente=obtener_coeficiente(termino)
    if raiz_de_numero(coeficiente)==0:
        return False
    letras=obtener_letras(termino)
    for letra in letras:
        if letras[letra]%2!=0:
            return False
    return True

def raiz_cuadrada(termino):
    # Recibe un término con raíz, por ejemplo "4x^2" o "x^4".
    # Saca la raíz del número y divide cada potencia entre 2.
    # Devuelve la raíz, por ejemplo "2x" o "x^2".
    coeficiente=raiz_de_numero(obtener_coeficiente(termino))
    letras_raiz=Counter()
    for letra,potencia in obtener_letras(termino).items():
        letras_raiz[letra]=potencia//2
    letras_texto=letras_a_texto(letras_raiz)
    if coeficiente!=1 or letras_texto=="":
        return str(coeficiente)+letras_texto
    return letras_texto

def doble_producto(raiz1,raiz3):
    # Recibe las dos raíces, por ejemplo "x" y "3".
    # Las multiplica y luego multiplica por 2.
    # Devuelve el término, por ejemplo "6x".
    coeficiente=2*obtener_coeficiente(raiz1)*obtener_coeficiente(raiz3)
    letras=Counter()
    for letra,potencia in obtener_letras(raiz1).items():
        letras[letra]=letras[letra]+potencia
    for letra,potencia in obtener_letras(raiz3).items():
        letras[letra]=letras[letra]+potencia
    letras_texto=letras_a_texto(letras)
    if coeficiente!=1 or letras_texto=="":
        return str(coeficiente)+letras_texto
    return letras_texto

def mismas_letras(texto1,texto2):
    # Recibe dos textos, por ejemplo "12xy" y "-12yx".
    # Compara las letras y sus potencias, sin mirar el orden.
    # Devuelve verdadero si son las mismas letras.
    letras1=obtener_letras(texto1)
    letras2=obtener_letras(texto2)
    if len(letras1)!=len(letras2):
        return False
    for letra in letras1:
        if letra not in letras2:
            return False
        if letras1[letra]!=letras2[letra]:
            return False
    return True

def es_el_termino_del_medio(doble,termino_medio):
    # Recibe el doble producto y el término del medio, por ejemplo "6x" y "-6x".
    # Compara el número y las letras, sin mirar el signo.
    # Devuelve verdadero si el doble producto es el término del medio.
    if obtener_coeficiente(doble)!=abs(obtener_coeficiente(termino_medio)):
        return False
    return mismas_letras(doble,termino_medio)

def signo_del_trinomio(terminos):
    # Recibe los tres términos, por ejemplo ["x^2","-6x","+9"].
    # Multiplica sus signos. Más por menos por más da menos.
    # Devuelve "+" o "-".
    producto=1
    for termino in terminos:
        if obtener_coeficiente(termino)<0:
            producto=producto*-1
    if producto<0:
        return "-"
    return "+"

def resolver_trinomio_cuadrado_perfecto(division_de_datos):
    # Recibe los términos, por ejemplo ["4x^2","+12xy","+9y^2"].
    # Revisa si el primero y el tercero tienen raíz y si el doble producto es el término del medio.
    # Si el del medio no está en el centro, prueba cada término como el de la mitad.
    # Devuelve "(2x+3y)^2". Si no es este caso, devuelve "".
    if len(division_de_datos)!=3:
        return ""

    for medio in [0,1,2]:
        extremos=[]
        for posicion in [0,1,2]:
            if posicion!=medio:
                extremos.append(division_de_datos[posicion])
        primero=extremos[0]
        tercero=extremos[1]
        if not tiene_raiz_cuadrada(primero) or not tiene_raiz_cuadrada(tercero):
            continue
        raiz1=raiz_cuadrada(primero)
        raiz3=raiz_cuadrada(tercero)
        doble=doble_producto(raiz1,raiz3)
        if es_el_termino_del_medio(doble,division_de_datos[medio]):
            signo=signo_del_trinomio(division_de_datos)
            return "("+raiz1+signo+raiz3+")^2"
    return ""

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos del trinomio cuadrado perfecto.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa con tres términos. El primero y el tercero tienen raíz cuadrada."
    texto=texto+"\n\n1. Se multiplican las dos raíces y el resultado se multiplica por 2."
    texto=texto+"\n2. Ese doble producto tiene que ser el término del medio, sin mirar su signo."
    texto=texto+"\n3. El signo del paréntesis es el producto de los tres signos."
    texto=texto+"\n4. El resultado es la raíz del primero, ese signo y la raíz del tercero, todo al cuadrado."
    texto=texto+"\n5. Si el término del medio no está en el centro, se prueba cada término como el de la mitad."
    texto=texto+"\n\nEjemplo: x² + 6x + 9 = (x + 3)²."
    texto=texto+"\nEjemplo: 4x² + 12xy + 9y² = (2x + 3y)²."
    return texto
