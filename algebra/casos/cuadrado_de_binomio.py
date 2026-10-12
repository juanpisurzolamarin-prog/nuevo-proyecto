# Caso del cuadrado de un binomio.
# Este archivo desarrolla (a+b)^2 o (a-b)^2. No factoriza.

from collections import Counter
from algebra.expresiones import preparar_expresion, obtener_coeficiente, obtener_letras, letras_a_texto


def es_cuadrado_de_binomio(expresion):
    # Recibe la expresión ya preparada, por ejemplo "(x+3)^2".
    # Revisa que empiece con ( y termine con )^2.
    # Devuelve verdadero si adentro hay dos términos separados por + o por -.
    if len(expresion)<6:
        return False
    if expresion[0]!="(":
        return False
    if expresion[len(expresion)-3:]!=")^2":
        return False
    termino1,signo,termino2=separar_binomio(expresion)
    if termino1=="" or termino2=="":
        return False
    if signo!="+" and signo!="-":
        return False
    return True

def separar_binomio(expresion):
    # Recibe "(2x-5)^2".
    # Busca el + o el - que separa los dos términos de adentro.
    # Devuelve "2x", "-" y "5". Si no puede, devuelve tres textos vacíos.
    interior=expresion[1:len(expresion)-3]
    posicion=1
    while posicion<len(interior):
        if interior[posicion]=="+" or interior[posicion]=="-":
            termino1=interior[0:posicion]
            signo=interior[posicion]
            termino2=interior[posicion+1:]
            if termino1!="" and termino2!="" and "+" not in termino2 and "-" not in termino2:
                return termino1,signo,termino2
        posicion=posicion+1
    return "","",""

def texto_de_termino(coeficiente,letras):
    # Recibe el número y las letras de un término, por ejemplo 4 y x al cuadrado.
    # Arma el texto. El 1 no se escribe si hay letras.
    # Devuelve "4x^2" o "x" o "25".
    letras_texto=letras_a_texto(letras)
    if coeficiente!=1 or letras_texto=="":
        return str(coeficiente)+letras_texto
    return letras_texto

def elevar_al_cuadrado(termino):
    # Recibe un término, por ejemplo "2x" o "5".
    # Lo multiplica por sí mismo: el número por el número y cada potencia por 2.
    # Devuelve "4x^2" o "25".
    coeficiente=abs(obtener_coeficiente(termino))
    letras_cuadrado=Counter()
    for letra,potencia in obtener_letras(termino).items():
        letras_cuadrado[letra]=potencia*2
    return texto_de_termino(coeficiente*coeficiente,letras_cuadrado)

def doble_producto(termino1,termino2):
    # Recibe los dos términos del paréntesis, por ejemplo "2x" y "5".
    # Calcula dos veces el primero por el segundo.
    # Devuelve "20x".
    coeficiente=2*abs(obtener_coeficiente(termino1))*abs(obtener_coeficiente(termino2))
    letras=Counter()
    for letra,potencia in obtener_letras(termino1).items():
        letras[letra]=letras[letra]+potencia
    for letra,potencia in obtener_letras(termino2).items():
        letras[letra]=letras[letra]+potencia
    return texto_de_termino(coeficiente,letras)

def resolver_cuadrado_de_binomio(expresion):
    # Recibe "(x-3)^2" o "(x-3)²".
    # Arma el cuadrado del primero, el doble producto y el cuadrado del segundo.
    # Si el signo es +, los tres quedan con más. Si es -, el del medio queda con menos.
    # Devuelve "x^2-6x+9". Si no es este caso, devuelve "".
    expresion=preparar_expresion(expresion)
    if not es_cuadrado_de_binomio(expresion):
        return ""
    termino1,signo,termino2=separar_binomio(expresion)
    cuadrado1=elevar_al_cuadrado(termino1)
    producto=doble_producto(termino1,termino2)
    cuadrado2=elevar_al_cuadrado(termino2)
    signo_del_medio="+"
    if signo=="-":
        signo_del_medio="-"
    return cuadrado1+signo_del_medio+producto+"+"+cuadrado2

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos del cuadrado de un binomio.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa cuando toda la expresión es un paréntesis elevado al cuadrado, por ejemplo (x + 3)²."
    texto=texto+"\n\n1. El primer término del resultado es el primero del paréntesis elevado al cuadrado."
    texto=texto+"\n2. El del medio es el doble producto de los dos términos."
    texto=texto+"\n3. El último es el segundo término elevado al cuadrado."
    texto=texto+"\n4. Si el signo de adentro es más, los tres términos quedan con más."
    texto=texto+"\n5. Si el signo es menos, el del medio queda con menos y el último con más."
    texto=texto+"\n6. El primer término queda positivo, porque es un cuadrado."
    texto=texto+"\n\nEjemplo: (x - 3)² = x² - 6x + 9."
    return texto
