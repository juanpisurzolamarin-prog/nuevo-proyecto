# Caso de suma o diferencia de dos potencias iguales.
# Este archivo no hace diferencia de cuadrados ni suma o diferencia de cubos.

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
    # Devuelve "2x^3", "x^4" o "16".
    letras_texto=letras_a_texto(letras)
    if coeficiente!=1 or letras_texto=="":
        return str(coeficiente)+letras_texto
    return letras_texto

def exponente_de_termino(termino):
    # Recibe un término, por ejemplo "x^5" o "32" o "x^5y^2".
    # Si no hay letras, devuelve 0. Si todas las letras tienen el mismo exponente, lo devuelve.
    # Si las letras tienen exponentes distintos, devuelve -1.
    letras=obtener_letras(termino)
    if len(letras)==0:
        return 0
    exponente=0
    for letra in letras:
        if exponente==0:
            exponente=letras[letra]
        if letras[letra]!=exponente:
            return -1
    return exponente

def exponente_comun(division_de_datos):
    # Recibe los dos términos, por ejemplo ["x^5","-32"].
    # Busca el exponente que los dos comparten. Un número suelto usa el del otro.
    # Devuelve 5. Si no hay un exponente común mayor que 1, devuelve 0.
    primero=exponente_de_termino(division_de_datos[0])
    segundo=exponente_de_termino(division_de_datos[1])
    if primero==-1 or segundo==-1:
        return 0
    if primero>0 and segundo>0 and primero!=segundo:
        return 0
    if primero>1 and (segundo==0 or segundo==primero):
        return primero
    if segundo>1 and primero==0:
        return segundo
    return 0

def numero_elevado(numero,veces):
    # Recibe un número y cuántas veces se multiplica, por ejemplo 2 y 5.
    # Lo multiplica por sí mismo esas veces.
    # Devuelve 32. Si veces es 0, devuelve 1.
    if veces==0:
        return 1
    resultado=1
    repeticion=0
    while repeticion<veces:
        resultado=resultado*numero
        repeticion=repeticion+1
    return resultado

def raiz_de_numero(numero,exponente):
    # Recibe un número positivo y el exponente, por ejemplo 32 y 5.
    # Busca un entero que elevado a ese exponente dé el número.
    # Devuelve 2. Si no existe, devuelve 0.
    if numero<=0 or exponente<=1:
        return 0
    candidato=1
    while numero_elevado(candidato,exponente)<numero:
        candidato=candidato+1
    if numero_elevado(candidato,exponente)==numero:
        return candidato
    return 0

def tiene_raiz(termino,exponente):
    # Recibe un término y el exponente, por ejemplo "x^5" y 5, o "-32" y 5.
    # Mira el número sin el signo y revisa si cada potencia se puede dividir entre el exponente.
    # Devuelve verdadero si tiene esa raíz.
    coeficiente=abs(obtener_coeficiente(termino))
    if raiz_de_numero(coeficiente,exponente)==0:
        return False
    letras=obtener_letras(termino)
    for letra in letras:
        if letras[letra]%exponente!=0:
            return False
    return True

def raiz_del_exponente(termino,exponente):
    # Recibe un término con raíz, por ejemplo "x^5" o "-32", y el exponente.
    # Saca la raíz del número, sin el signo, y divide cada potencia entre el exponente.
    # Devuelve la raíz positiva, por ejemplo "x" o "2".
    coeficiente=raiz_de_numero(abs(obtener_coeficiente(termino)),exponente)
    letras=Counter()
    for letra,potencia in obtener_letras(termino).items():
        letras[letra]=potencia//exponente
    return texto_de_termino(coeficiente,letras)

def letras_elevadas(letras,veces):
    # Recibe las letras de una raíz y un exponente.
    # Multiplica cada potencia por ese exponente.
    # Si el exponente es 0, devuelve las letras vacías, porque esa raíz no se escribe.
    nuevas=Counter()
    if veces==0:
        return nuevas
    for letra,potencia in letras.items():
        nuevas[letra]=potencia*veces
    return nuevas

def termino_con_dos_raices(raiz1,exp1,raiz2,exp2):
    # Recibe las dos raíces y el exponente de cada una, por ejemplo "x", 3, "2" y 1.
    # Multiplica la primera raíz elevada a exp1 por la segunda elevada a exp2.
    # Devuelve "2x^3".
    coeficiente1=abs(obtener_coeficiente(raiz1))
    coeficiente2=abs(obtener_coeficiente(raiz2))
    coeficiente=numero_elevado(coeficiente1,exp1)*numero_elevado(coeficiente2,exp2)
    letras=Counter()
    for letra,potencia in letras_elevadas(obtener_letras(raiz1),exp1).items():
        letras[letra]=letras[letra]+potencia
    for letra,potencia in letras_elevadas(obtener_letras(raiz2),exp2).items():
        letras[letra]=letras[letra]+potencia
    return texto_de_termino(coeficiente,letras)

def es_una_suma(division_de_datos):
    # Recibe los dos términos, por ejemplo ["x^5","+32"].
    # Una suma tiene los dos términos positivos.
    # Devuelve verdadero si el segundo también es positivo.
    if obtener_coeficiente(division_de_datos[1])>0:
        return True
    return False

def nombre_de_potencias_iguales(division_de_datos):
    # Recibe los dos términos.
    # Mira si la expresión suma o resta.
    # Devuelve el nombre que se muestra en la pantalla.
    if es_una_suma(division_de_datos):
        return "suma de dos potencias iguales"
    return "diferencia de dos potencias iguales"

def parentesis_largo(raiz1,raiz2,exponente,suma):
    # Recibe las dos raíces, el exponente y si la expresión suma.
    # El exponente de la primera raíz baja y el de la segunda sube.
    # Si suma, los signos se intercalan empezando por menos. Si resta, todos son más.
    # Devuelve "x^4+2x^3+4x^2+8x+16".
    texto=termino_con_dos_raices(raiz1,exponente-1,raiz2,0)
    indice=1
    signo="+"
    if suma:
        signo="-"
    while indice<exponente:
        exp1=(exponente-1)-indice
        exp2=indice
        termino=termino_con_dos_raices(raiz1,exp1,raiz2,exp2)
        texto=texto+signo+termino
        if suma:
            if signo=="-":
                signo="+"
            else:
                signo="-"
        indice=indice+1
    return texto

def resolver_suma_o_diferencia_de_potencias(division_de_datos):
    # Recibe los términos, por ejemplo ["x^5","-32"].
    # Revisa que sea un binomio, que el exponente sea el mismo y que los dos tengan raíz.
    # Arma el paréntesis de las raíces y el paréntesis largo.
    # Devuelve "(x-2)(x^4+2x^3+4x^2+8x+16)". Si no es este caso, devuelve "".
    if not es_binomio(division_de_datos):
        return ""
    primero=division_de_datos[0]
    segundo=division_de_datos[1]
    if obtener_coeficiente(primero)<0:
        return ""
    exponente=exponente_comun(division_de_datos)
    if exponente==0:
        return ""
    if es_una_suma(division_de_datos) and exponente%2==0:
        return ""
    if not tiene_raiz(primero,exponente) or not tiene_raiz(segundo,exponente):
        return ""
    raiz1=raiz_del_exponente(primero,exponente)
    raiz2=raiz_del_exponente(segundo,exponente)
    signo="+"
    if not es_una_suma(division_de_datos):
        signo="-"
    primero_parentesis="("+raiz1+signo+raiz2+")"
    segundo_parentesis="("+parentesis_largo(raiz1,raiz2,exponente,es_una_suma(division_de_datos))+")"
    return primero_parentesis+segundo_parentesis

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos de la suma o diferencia de dos potencias iguales.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa con un binomio. Al menos un término está elevado a un exponente mayor que 1."
    texto=texto+"\nSi los dos tienen letras, todas llevan el mismo exponente. Los dos tienen raíz de ese exponente."
    texto=texto+"\n\n1. El primer paréntesis lleva la raíz de cada término y el signo de la expresión."
    texto=texto+"\n2. En el segundo paréntesis, el exponente de la primera raíz empieza en el exponente menos uno y va bajando."
    texto=texto+"\n3. El exponente de la segunda raíz empieza en cero y va subiendo, hasta el exponente menos uno."
    texto=texto+"\n4. Si la expresión resta, todos los signos de ese paréntesis son más."
    texto=texto+"\n5. Si la expresión suma, se intercalan y el menos empieza en el segundo término."
    texto=texto+"\n6. Si el exponente es par y la expresión suma, no entra en este caso."
    texto=texto+"\n\nEjemplo: x⁵ - 32 = (x - 2)(x⁴ + 2x³ + 4x² + 8x + 16)."
    texto=texto+"\nLa diferencia de cuadrados y los cubos se preguntan antes, así que x² - 9 y x³ - 8 se quedan en sus casos."
    return texto
