# Caso del trinomio de la forma x^2 + bx + c.
# Este archivo no hace los otros casos de factorización.

from algebra.expresiones import obtener_coeficiente, obtener_letras


def es_trinomio(division_de_datos):
    # Recibe los términos de la expresión.
    # Revisa cuántos términos hay.
    # Devuelve verdadero si hay exactamente tres.
    if len(division_de_datos)==3:
        return True
    return False

def letra_unica(termino):
    # Recibe un término, por ejemplo "x^2" o "5x".
    # Busca si tiene una sola letra.
    # Devuelve esa letra. Si no hay una sola, devuelve "".
    letras=obtener_letras(termino)
    if len(letras)!=1:
        return ""
    for letra in letras:
        return letra
    return ""

def termino_cuadrado(termino):
    # Recibe un término, por ejemplo "x^2" o "4x^2".
    # Revisa que la letra esté al cuadrado y que no haya un entero escrito.
    # Devuelve verdadero solo para "x^2". Si el número no se escribe, vale 1.
    if obtener_coeficiente(termino)!=1:
        return False
    letra=letra_unica(termino)
    if letra=="":
        return False
    letras=obtener_letras(termino)
    if letras[letra]==2:
        return True
    return False

def termino_independiente(termino):
    # Recibe un término, por ejemplo "6" o "-6" o "6x".
    # Revisa que sea un entero sin letra.
    # Devuelve verdadero si no tiene letras.
    if len(obtener_letras(termino))==0:
        return True
    return False

def termino_del_medio(termino,letra):
    # Recibe un término y la letra del cuadrado, por ejemplo "5x" y "x".
    # La letra debe ser la misma y no debe tener exponente.
    # Devuelve verdadero. "x" también sirve, porque el entero es 1. "5y" no.
    if letra_unica(termino)!=letra:
        return False
    letras=obtener_letras(termino)
    if letras[letra]==1:
        return True
    return False

def separar_la_forma(division_de_datos):
    # Recibe los tres términos, aunque no estén en orden.
    # Busca el cuadrado, el término con la letra y el entero sin letra.
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
    # Recibe un término, por ejemplo "-5x" o "6".
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
    # Recibe el segundo término y el tercero, por ejemplo "-5x" y "+6".
    # El primer paréntesis lleva el signo del segundo término.
    # El segundo paréntesis lleva la multiplicación de los dos signos.
    # Devuelve los dos signos, por ejemplo "-" y "-".
    signo1=signo_de_termino(medio)
    signo2=multiplicar_signos(signo1,signo_de_termino(independiente))
    return signo1,signo2

def buscar_los_dos_numeros(producto,segundo,mismos_signos):
    # Recibe el tercer término sin signo, el segundo término sin signo y si los signos son iguales.
    # Busca dos enteros que multiplicados den el tercero.
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

def resolver_trinomio_x2_bx_c(division_de_datos):
    # Recibe los términos, por ejemplo ["x^2","+5x","-6"].
    # Pone la raíz del primero en dos paréntesis y les pone los signos.
    # El número mayor va en el primer paréntesis y el menor en el segundo.
    # Devuelve "(x+6)(x-1)". Si no es este caso, devuelve "".
    if not es_trinomio(division_de_datos):
        return ""
    cuadrado,medio,independiente=separar_la_forma(division_de_datos)
    if cuadrado=="":
        return ""
    signo1,signo2=signos_de_los_parentesis(medio,independiente)
    mismos_signos=signo1==signo2
    mayor,menor=buscar_los_dos_numeros(abs(obtener_coeficiente(independiente)),abs(obtener_coeficiente(medio)),mismos_signos)
    if mayor==0:
        return ""
    letra=letra_unica(cuadrado)
    return "("+letra+signo1+str(mayor)+")("+letra+signo2+str(menor)+")"

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos del trinomio de la forma x² + bx + c.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa con tres términos. El primero es una letra al cuadrado y su número no se escribe, así que vale 1."
    texto=texto+"\nEl segundo es esa misma letra, sin exponente. El tercero es un entero sin letra."
    texto=texto+"\n\n1. Los dos paréntesis reciben la raíz del primer término."
    texto=texto+"\n2. El primer paréntesis lleva el signo del segundo término."
    texto=texto+"\n3. El segundo paréntesis lleva la multiplicación de ese signo por el signo del tercero."
    texto=texto+"\n4. Si los signos de los paréntesis son iguales, se buscan dos números que sumen el segundo término."
    texto=texto+"\n5. Si son distintos, esos números restan el segundo término. Su producto siempre es el tercero."
    texto=texto+"\n6. El número mayor va en el primer paréntesis y el menor en el segundo."
    texto=texto+"\n\nEjemplo: x² + 5x + 6 = (x + 3)(x + 2)."
    texto=texto+"\nSi también es trinomio cuadrado perfecto, se muestra ese caso primero."
    return texto
