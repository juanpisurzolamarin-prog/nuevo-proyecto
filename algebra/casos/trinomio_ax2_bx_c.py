# Caso del trinomio de la forma ax^2 + bx + c.
# El número del primer término es mayor que 1. No usa el otro trinomio.

import math
from algebra.expresiones import obtener_coeficiente, obtener_letras


def es_trinomio(division_de_datos):
    # Recibe los términos de la expresión.
    # Revisa cuántos términos hay.
    # Devuelve verdadero si hay exactamente tres.
    if len(division_de_datos)==3:
        return True
    return False

def letra_unica(termino):
    # Recibe un término, por ejemplo "2x^2" o "7x".
    # Busca si tiene una sola letra.
    # Devuelve esa letra. Si no hay una sola, devuelve "".
    letras=obtener_letras(termino)
    if len(letras)!=1:
        return ""
    for letra in letras:
        return letra
    return ""

def termino_cuadrado(termino):
    # Recibe un término, por ejemplo "2x^2" o "x^2".
    # Revisa que la letra esté al cuadrado y que el entero sea mayor que 1.
    # Devuelve verdadero solo si el primero es positivo y distinto de 1.
    if obtener_coeficiente(termino)<=1:
        return False
    letra=letra_unica(termino)
    if letra=="":
        return False
    letras=obtener_letras(termino)
    if letras[letra]==2:
        return True
    return False

def termino_independiente(termino):
    # Recibe un término, por ejemplo "3" o "-2" o "7x".
    # Revisa que sea un entero sin letra.
    # Devuelve verdadero si no tiene letras.
    if len(obtener_letras(termino))==0:
        return True
    return False

def termino_del_medio(termino,letra):
    # Recibe un término y la letra del cuadrado, por ejemplo "7x" y "x".
    # La letra debe ser la misma, sin exponente, y el entero distinto de 1.
    # Devuelve verdadero. "x" no sirve, porque su número es 1. "7y" tampoco.
    if letra_unica(termino)!=letra:
        return False
    if abs(obtener_coeficiente(termino))==1:
        return False
    letras=obtener_letras(termino)
    if letras[letra]==1:
        return True
    return False

def separar_la_forma(division_de_datos):
    # Recibe los tres términos, aunque no estén en orden.
    # Busca el cuadrado con entero mayor que 1, el término con la letra y el entero sin letra.
    # Devuelve esos tres términos. Si no tienen esa forma, devuelve tres textos vacíos.
    cuadrado=""
    medio=""
    independiente=""
    for termino in division_de_datos:
        if termino_cuadrado(termino) and cuadrado=="":
            cuadrado=termino
        elif termino_independiente(termino) and independiente=="":
            independiente=termino
        elif medio=="":
            medio=termino
        else:
            return "","",""
    if cuadrado=="" or medio=="" or independiente=="":
        return "","",""
    letra=letra_unica(cuadrado)
    if not termino_del_medio(medio,letra):
        return "","",""
    return cuadrado,medio,independiente

def signo_de_termino(termino):
    # Recibe un término, por ejemplo "-5x" o "3".
    # Mira si el número es positivo o negativo.
    # Devuelve "+" o "-".
    if obtener_coeficiente(termino)<0:
        return "-"
    return "+"

def multiplicar_signos(signo1,signo2):
    # Recibe dos signos, por ejemplo "-" y "+".
    # Los multiplica: signos iguales dan más, signos distintos dan menos.
    # Devuelve "+" o "-".
    if signo1==signo2:
        return "+"
    return "-"

def signos_de_los_parentesis(medio,independiente):
    # Recibe el segundo término y el tercero, por ejemplo "-5x" y "+3".
    # El primer paréntesis lleva el signo del segundo término.
    # El segundo paréntesis lleva la multiplicación de los dos signos.
    # Devuelve los dos signos, por ejemplo "-" y "-".
    signo1=signo_de_termino(medio)
    signo2=multiplicar_signos(signo1,signo_de_termino(independiente))
    return signo1,signo2

def buscar_los_dos_numeros(producto,segundo,mismos_signos):
    # Recibe el producto del primero por el tercero, el segundo sin signo y si los signos son iguales.
    # Busca dos enteros que multiplicados den ese producto.
    # Si los signos son iguales, deben sumar el segundo. Si son distintos, deben restar el segundo.
    # Devuelve el mayor y el menor. Si no hay pareja, devuelve 0 y 0.
    numero=1
    while numero<=producto:
        if producto%numero==0:
            otro=producto//numero
            if numero<=otro:
                sirve=False
                if mismos_signos and numero+otro==segundo:
                    sirve=True
                if not mismos_signos and otro-numero==segundo:
                    sirve=True
                if sirve:
                    return otro,numero
        numero=numero+1
    return 0,0

def factor_comun_del_parentesis(coeficiente_a,numero):
    # Recibe el entero de abajo y el número de un paréntesis, por ejemplo 2 y 6.
    # Busca el máximo común divisor de esos dos números.
    # Devuelve ese factor, por ejemplo 2.
    return math.gcd(coeficiente_a,numero)

def parentesis_dividido(letra,coeficiente_a,numero,signo,factor):
    # Recibe la letra, el entero de abajo, el número del paréntesis, su signo y el factor común.
    # Divide el entero de la letra y el número entre ese factor.
    # Devuelve el paréntesis ya dividido, por ejemplo "(x+3)" o "(2x+1)".
    coeficiente_letra=coeficiente_a//factor
    numero_nuevo=numero//factor
    if coeficiente_letra==1:
        base=letra
    else:
        base=str(coeficiente_letra)+letra
    return "("+base+signo+str(numero_nuevo)+")"

def resolver_trinomio_ax2_bx_c(division_de_datos):
    # Recibe los términos, por ejemplo ["2x^2","+7x","+3"].
    # Multiplica por el entero del primero y arma dos paréntesis con la letra y ese entero.
    # Después divide entre ese entero, sacando factor común en cada paréntesis.
    # Devuelve "(x+3)(2x+1)". Si no es este caso, devuelve "".
    if not es_trinomio(division_de_datos):
        return ""
    cuadrado,medio,independiente=separar_la_forma(division_de_datos)
    if cuadrado=="":
        return ""
    coeficiente_a=obtener_coeficiente(cuadrado)
    signo1,signo2=signos_de_los_parentesis(medio,independiente)
    mismos_signos=signo1==signo2
    producto=coeficiente_a*abs(obtener_coeficiente(independiente))
    mayor,menor=buscar_los_dos_numeros(producto,abs(obtener_coeficiente(medio)),mismos_signos)
    if mayor==0:
        return ""
    factor1=factor_comun_del_parentesis(coeficiente_a,mayor)
    factor2=factor_comun_del_parentesis(coeficiente_a,menor)
    if factor1*factor2!=coeficiente_a:
        return ""
    letra=letra_unica(cuadrado)
    parentesis1=parentesis_dividido(letra,coeficiente_a,mayor,signo1,factor1)
    parentesis2=parentesis_dividido(letra,coeficiente_a,menor,signo2,factor2)
    return parentesis1+parentesis2

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos del trinomio de la forma ax² + bx + c.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa con tres términos. El número del primero es mayor que 1 y la letra está al cuadrado."
    texto=texto+"\nEl segundo tiene la misma letra y un número distinto de 1. El tercero es un entero."
    texto=texto+"\n\n1. Se multiplica todo el trinomio por el número del primer término."
    texto=texto+"\n2. En el segundo término se deja escrita la multiplicación y se cambia el entero: queda ese número por la letra y el entero inicial."
    texto=texto+"\n3. El primer término se escribe con la letra y el entero inicial, todo al cuadrado."
    texto=texto+"\n4. Eso se factoriza como un trinomio de la forma x² + bx + c, en dos paréntesis."
    texto=texto+"\n5. Como se multiplicó, también se divide entre el mismo entero."
    texto=texto+"\n6. Se saca factor común en cada paréntesis de arriba para borrar el entero de abajo."
    texto=texto+"\n\nEjemplo: 2x² + 7x + 3 = (x + 3)(2x + 1)."
    return texto
