# Caso de suma o diferencia de cubos perfectos.
# Este archivo no hace diferencia de cuadrados ni cubo de un binomio.

from collections import Counter
from algebra.expresiones import obtener_coeficiente, obtener_letras, letras_a_texto


def es_binomio(division_de_datos):
    # Recibe los términos de la expresión.
    # Revisa cuántos términos hay.
    # Devuelve verdadero si hay exactamente dos.
    if len(division_de_datos)==2:
        return True
    return False

def texto_de_termino(coeficiente,letras):
    # Recibe el número y las letras de un término.
    # Arma el texto. El 1 no se escribe si hay letras.
    # Devuelve "4x^2", "2x" o "4".
    letras_texto=letras_a_texto(letras)
    if coeficiente!=1 or letras_texto=="":
        return str(coeficiente)+letras_texto
    return letras_texto

def raiz_de_numero(numero):
    # Recibe un número positivo, por ejemplo 8.
    # Busca un entero que multiplicado tres veces por sí mismo dé ese número.
    # Devuelve 2. Si no es un cubo perfecto, devuelve 0.
    if numero<=0:
        return 0
    candidato=1
    while candidato*candidato*candidato<numero:
        candidato=candidato+1
    if candidato*candidato*candidato==numero:
        return candidato
    return 0

def tiene_raiz_cubica(termino):
    # Recibe un término, por ejemplo "x^3" o "-8".
    # Mira el número sin el signo y revisa si cada potencia se puede dividir entre 3.
    # Devuelve verdadero si tiene raíz cúbica.
    coeficiente=abs(obtener_coeficiente(termino))
    if raiz_de_numero(coeficiente)==0:
        return False
    letras=obtener_letras(termino)
    for letra in letras:
        if letras[letra]%3!=0:
            return False
    return True

def raiz_cubica(termino):
    # Recibe un término con raíz cúbica, por ejemplo "8x^3" o "-8".
    # Saca la raíz del número, sin el signo, y divide cada potencia entre 3.
    # Devuelve la raíz positiva, por ejemplo "2x" o "2".
    coeficiente=raiz_de_numero(abs(obtener_coeficiente(termino)))
    letras=Counter()
    for letra,potencia in obtener_letras(termino).items():
        letras[letra]=potencia//3
    return texto_de_termino(coeficiente,letras)

def elevar_al_cuadrado(termino):
    # Recibe una raíz, por ejemplo "2x" o "3".
    # La multiplica por sí misma.
    # Devuelve "4x^2" o "9".
    coeficiente=abs(obtener_coeficiente(termino))
    letras=Counter()
    for letra,potencia in obtener_letras(termino).items():
        letras[letra]=potencia*2
    return texto_de_termino(coeficiente*coeficiente,letras)

def producto_de_raices(raiz1,raiz2):
    # Recibe las dos raíces, por ejemplo "x" y "2".
    # Multiplica la primera por la segunda.
    # Devuelve "2x".
    coeficiente=abs(obtener_coeficiente(raiz1))*abs(obtener_coeficiente(raiz2))
    letras=Counter()
    for letra,potencia in obtener_letras(raiz1).items():
        letras[letra]=letras[letra]+potencia
    for letra,potencia in obtener_letras(raiz2).items():
        letras[letra]=letras[letra]+potencia
    return texto_de_termino(coeficiente,letras)

def es_una_suma(division_de_datos):
    # Recibe los dos términos, por ejemplo ["x^3","+8"].
    # Una suma tiene los dos términos positivos.
    # Devuelve verdadero si el segundo también es positivo.
    if obtener_coeficiente(division_de_datos[1])>0:
        return True
    return False

def nombre_del_caso(division_de_datos):
    # Recibe los dos términos.
    # Mira si la expresión suma o resta.
    # Devuelve el nombre que se muestra en la pantalla.
    if es_una_suma(division_de_datos):
        return "suma de cubos perfectos"
    return "diferencia de cubos perfectos"

def resolver_suma_o_diferencia_de_cubos(division_de_datos):
    # Recibe los términos, por ejemplo ["x^3","-8"].
    # Revisa que sea un binomio y que los dos términos tengan raíz cúbica.
    # Arma un paréntesis con las raíces y otro con el trinomio.
    # Devuelve "(x-2)(x^2+2x+4)". Si no es este caso, devuelve "".
    if not es_binomio(division_de_datos):
        return ""
    primero=division_de_datos[0]
    segundo=division_de_datos[1]
    if obtener_coeficiente(primero)<0:
        return ""
    if not tiene_raiz_cubica(primero) or not tiene_raiz_cubica(segundo):
        return ""
    raiz1=raiz_cubica(primero)
    raiz2=raiz_cubica(segundo)
    cuadrado1=elevar_al_cuadrado(raiz1)
    producto=producto_de_raices(raiz1,raiz2)
    cuadrado2=elevar_al_cuadrado(raiz2)
    signo="+"
    signo_producto="-"
    signo_cuadrado2="+"
    if not es_una_suma(division_de_datos):
        signo="-"
        signo_producto="+"
        signo_cuadrado2="+"
    parentesis1="("+raiz1+signo+raiz2+")"
    parentesis2="("+cuadrado1+signo_producto+producto+signo_cuadrado2+cuadrado2+")"
    return parentesis1+parentesis2

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos de la suma o diferencia de cubos perfectos.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa con un binomio. Los dos términos tienen raíz cúbica. Puede sumar o restar."
    texto=texto+"\n\n1. El primer paréntesis lleva la raíz cúbica de cada término y el signo de la expresión."
    texto=texto+"\n2. El segundo paréntesis es un trinomio: el primero al cuadrado, el producto de las dos raíces y el segundo al cuadrado."
    texto=texto+"\n3. Si la expresión suma, los signos del trinomio se intercalan y el menos va primero."
    texto=texto+"\n4. Si la expresión resta, los tres signos del trinomio son más."
    texto=texto+"\n\nEjemplo de suma: x³ + 8 = (x + 2)(x² - 2x + 4)."
    texto=texto+"\nEjemplo de resta: x³ - 8 = (x - 2)(x² + 2x + 4)."
    return texto
