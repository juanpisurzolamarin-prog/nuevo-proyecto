# Caso de diferencia de cuadrados.
# Este archivo no hace factor común, ni trinomio, ni agrupación.

from collections import Counter
from algebra.expresiones import obtener_coeficiente, obtener_letras, letras_a_texto


def es_binomio(division_de_datos):
    # Recibe los términos de la expresión.
    # Revisa cuántos términos hay.
    # Devuelve verdadero si hay exactamente dos.
    if len(division_de_datos)==2:
        return True
    return False

def es_una_resta(division_de_datos):
    # Recibe los dos términos, por ejemplo ["x^2","-9"].
    # Una resta tiene un término positivo y otro negativo.
    # Devuelve verdadero si los signos son distintos. "x^2+9" devuelve falso.
    coeficiente1=obtener_coeficiente(division_de_datos[0])
    coeficiente2=obtener_coeficiente(division_de_datos[1])
    if coeficiente1>0 and coeficiente2<0:
        return True
    if coeficiente1<0 and coeficiente2>0:
        return True
    return False

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
    # Mira el número sin el signo y revisa si cada potencia es par.
    # Devuelve verdadero si tiene raíz. "-9" sí, porque 9 es 3 por 3.
    coeficiente=abs(obtener_coeficiente(termino))
    if raiz_de_numero(coeficiente)==0:
        return False
    letras=obtener_letras(termino)
    for letra in letras:
        if letras[letra]%2!=0:
            return False
    return True

def raiz_cuadrada(termino):
    # Recibe un término con raíz, por ejemplo "4x^2" o "-9".
    # Saca la raíz del número, sin el signo, y divide cada potencia entre 2.
    # Devuelve la raíz positiva, por ejemplo "2x" o "3".
    coeficiente=raiz_de_numero(abs(obtener_coeficiente(termino)))
    letras_raiz=Counter()
    for letra,potencia in obtener_letras(termino).items():
        letras_raiz[letra]=potencia//2
    letras_texto=letras_a_texto(letras_raiz)
    if coeficiente!=1 or letras_texto=="":
        return str(coeficiente)+letras_texto
    return letras_texto

def termino_positivo(division_de_datos):
    # Recibe los dos términos.
    # Busca el que tiene signo más.
    # Devuelve ese término.
    if obtener_coeficiente(division_de_datos[0])>0:
        return division_de_datos[0]
    return division_de_datos[1]

def termino_negativo(division_de_datos):
    # Recibe los dos términos.
    # Busca el que tiene signo menos.
    # Devuelve ese término.
    if obtener_coeficiente(division_de_datos[0])<0:
        return division_de_datos[0]
    return division_de_datos[1]

def resolver_diferencia_de_cuadrados(division_de_datos):
    # Recibe los términos, por ejemplo ["4x^2","-9"].
    # Revisa que sea un binomio, que sea una resta y que los dos términos tengan raíz.
    # Arma dos paréntesis iguales: uno con más y otro con menos.
    # Devuelve "(2x+3)(2x-3)". Si no es este caso, devuelve "".
    if not es_binomio(division_de_datos):
        return ""
    if not es_una_resta(division_de_datos):
        return ""
    positivo=termino_positivo(division_de_datos)
    negativo=termino_negativo(division_de_datos)
    if not tiene_raiz_cuadrada(positivo) or not tiene_raiz_cuadrada(negativo):
        return ""
    raiz1=raiz_cuadrada(positivo)
    raiz2=raiz_cuadrada(negativo)
    return "("+raiz1+"+"+raiz2+")("+raiz1+"-"+raiz2+")"

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos de la diferencia de cuadrados.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa con un binomio que es una resta. Los dos términos tienen raíz cuadrada."
    texto=texto+"\n\n1. Se saca la raíz de cada término, sin mirar el signo. -9 tiene raíz 3."
    texto=texto+"\n2. Se arman dos paréntesis iguales."
    texto=texto+"\n3. Uno lleva más y el otro lleva menos."
    texto=texto+"\n4. La raíz del término positivo va primero, para que al multiplicar vuelva la resta."
    texto=texto+"\n\nEjemplo: x² - 9 = (x + 3)(x - 3)."
    texto=texto+"\nEjemplo: 9 - 4x² = (3 + 2x)(3 - 2x)."
    return texto
