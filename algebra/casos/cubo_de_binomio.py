# Caso del cubo perfecto de un binomio.
# Desarrolla (a+b)^3 o (a-b)^3, y también factoriza ese polinomio.

from collections import Counter
from algebra.expresiones import preparar_expresion, obtener_coeficiente, obtener_letras, letras_a_texto


def es_cubo_de_binomio(expresion):
    # Recibe la expresión ya preparada, por ejemplo "(x+2)^3".
    # Revisa que empiece con ( y termine con )^3.
    # Devuelve verdadero si adentro hay dos términos separados por + o por -.
    if len(expresion)<6:
        return False
    if expresion[0]!="(":
        return False
    if expresion[len(expresion)-3:]!=")^3":
        return False
    termino1,signo,termino2=separar_binomio(expresion)
    if termino1=="" or termino2=="":
        return False
    if signo!="+" and signo!="-":
        return False
    return True

def separar_binomio(expresion):
    # Recibe "(x-2)^3".
    # Busca el + o el - que separa los dos términos de adentro.
    # Devuelve "x", "-" y "2". Si no puede, devuelve tres textos vacíos.
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
    # Recibe el número y las letras de un término.
    # Arma el texto. El 1 no se escribe si hay letras.
    # Devuelve "8x^3", "6x^2" o "8".
    letras_texto=letras_a_texto(letras)
    if coeficiente!=1 or letras_texto=="":
        return str(coeficiente)+letras_texto
    return letras_texto

def letras_por_numero(letras,veces):
    # Recibe las letras de un término y un número, por ejemplo 3.
    # Multiplica cada potencia por ese número.
    # Devuelve las potencias nuevas. x pasa a x^3 si veces es 3.
    nuevas=Counter()
    for letra,potencia in letras.items():
        nuevas[letra]=potencia*veces
    return nuevas

def sumar_letras(letras1,letras2):
    # Recibe las letras de dos términos.
    # Suma las potencias de cada letra, porque se están multiplicando.
    # Devuelve las letras del producto.
    letras=Counter()
    for letra,potencia in letras1.items():
        letras[letra]=letras[letra]+potencia
    for letra,potencia in letras2.items():
        letras[letra]=letras[letra]+potencia
    return letras

def elevar_al_cubo(termino):
    # Recibe un término, por ejemplo "2x" o "2".
    # Lo multiplica por sí mismo tres veces.
    # Devuelve "8x^3" o "8".
    coeficiente=abs(obtener_coeficiente(termino))
    letras=letras_por_numero(obtener_letras(termino),3)
    return texto_de_termino(coeficiente*coeficiente*coeficiente,letras)

def triple_primero_cuadrado(termino1,termino2):
    # Recibe el primer término y el segundo, por ejemplo "x" y "2".
    # Calcula tres veces el primero al cuadrado por el segundo.
    # Devuelve "6x^2".
    coeficiente1=abs(obtener_coeficiente(termino1))
    coeficiente2=abs(obtener_coeficiente(termino2))
    coeficiente=3*coeficiente1*coeficiente1*coeficiente2
    primero_cuadrado=letras_por_numero(obtener_letras(termino1),2)
    letras=sumar_letras(primero_cuadrado,obtener_letras(termino2))
    return texto_de_termino(coeficiente,letras)

def triple_segundo_cuadrado(termino1,termino2):
    # Recibe el primer término y el segundo, por ejemplo "x" y "2".
    # Calcula tres veces el primero por el segundo al cuadrado.
    # Devuelve "12x".
    coeficiente1=abs(obtener_coeficiente(termino1))
    coeficiente2=abs(obtener_coeficiente(termino2))
    coeficiente=3*coeficiente1*coeficiente2*coeficiente2
    segundo_cuadrado=letras_por_numero(obtener_letras(termino2),2)
    letras=sumar_letras(obtener_letras(termino1),segundo_cuadrado)
    return texto_de_termino(coeficiente,letras)

def resolver_cubo_de_binomio(expresion):
    # Recibe "(x-2)^3" o "(x-2)³".
    # Arma el cubo del primero, los dos términos del medio y el cubo del segundo.
    # Si el signo es +, todos quedan con más. Si es -, van menos, más y menos.
    # Devuelve "x^3-6x^2+12x-8". Si no es este caso, devuelve "".
    expresion=preparar_expresion(expresion)
    if not es_cubo_de_binomio(expresion):
        return ""
    termino1,signo,termino2=separar_binomio(expresion)
    cubo1=elevar_al_cubo(termino1)
    primero=triple_primero_cuadrado(termino1,termino2)
    segundo=triple_segundo_cuadrado(termino1,termino2)
    cubo2=elevar_al_cubo(termino2)
    signo_primero="+"
    signo_segundo="+"
    signo_tercero="+"
    if signo=="-":
        signo_primero="-"
        signo_segundo="+"
        signo_tercero="-"
    return cubo1+signo_primero+primero+signo_segundo+segundo+signo_tercero+cubo2

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

def terminos_iguales_sin_signo(termino1,termino2):
    # Recibe dos términos, por ejemplo "-6x^2" y "6x^2".
    # Compara el número y las letras, sin mirar el signo.
    # Devuelve verdadero si son el mismo término.
    if abs(obtener_coeficiente(termino1))!=abs(obtener_coeficiente(termino2)):
        return False
    letras1=obtener_letras(termino1)
    letras2=obtener_letras(termino2)
    if len(letras1)!=len(letras2):
        return False
    for letra in letras1:
        if letra not in letras2:
            return False
        if letras1[letra]!=letras2[letra]:
            return False
    return True

def resolver_cubo_perfecto(division_de_datos):
    # Recibe cuatro términos, por ejemplo ["x^3","-6x^2","+12x","-8"].
    # El primero y el último deben ser cubos. El segundo y el tercero deben cumplir la regla del cubo.
    # El signo del paréntesis es el signo del segundo término.
    # Devuelve "(x-2)^3". Si no es este caso, devuelve "".
    if len(division_de_datos)!=4:
        return ""
    primero=division_de_datos[0]
    segundo=division_de_datos[1]
    tercero=division_de_datos[2]
    ultimo=division_de_datos[3]
    if obtener_coeficiente(primero)<0:
        return ""
    if not tiene_raiz_cubica(primero) or not tiene_raiz_cubica(ultimo):
        return ""
    # El cuaderno pone el cubo del primer término al inicio.
    # 8-12x+6x^2-x^3 empieza por el número y termina por la letra, así que no entra.
    if len(obtener_letras(primero))==0 and len(obtener_letras(ultimo))>0:
        return ""
    if obtener_coeficiente(tercero)<=0:
        return ""
    raiz1=raiz_cubica(primero)
    raiz2=raiz_cubica(ultimo)
    esperado_segundo=triple_primero_cuadrado(raiz1,raiz2)
    esperado_tercero=triple_segundo_cuadrado(raiz1,raiz2)
    if not terminos_iguales_sin_signo(segundo,esperado_segundo):
        return ""
    if not terminos_iguales_sin_signo(tercero,esperado_tercero):
        return ""
    if obtener_coeficiente(ultimo)<0 and obtener_coeficiente(segundo)>0:
        return ""
    if obtener_coeficiente(ultimo)>0 and obtener_coeficiente(segundo)<0:
        return ""
    signo="+"
    if obtener_coeficiente(segundo)<0:
        signo="-"
    return "("+raiz1+signo+raiz2+")^3"

def plan_del_desarrollo():
    # No recibe datos.
    # Escribe los pasos para desarrollar el cubo de un binomio.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa cuando toda la expresión es un paréntesis elevado al cubo, por ejemplo (x + 2)³."
    texto=texto+"\n\n1. El primer término es el primero del paréntesis elevado al cubo."
    texto=texto+"\n2. El segundo es tres veces el primero al cuadrado por el segundo."
    texto=texto+"\n3. El tercero es tres veces el primero por el segundo al cuadrado."
    texto=texto+"\n4. El último es el segundo término elevado al cubo."
    texto=texto+"\n5. Si el signo de adentro es más, los cuatro términos quedan con más."
    texto=texto+"\n6. Si el signo es menos, quedan menos, más y menos. El primero sigue positivo, porque es un cubo."
    texto=texto+"\n\nEjemplo: (x - 2)³ = x³ - 6x² + 12x - 8."
    return texto

def plan_de_la_factorizacion():
    # No recibe datos.
    # Escribe los pasos para factorizar un cubo perfecto de un binomio.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa con cuatro términos. El primero y el último tienen raíz cúbica."
    texto=texto+"\nEl cubo del primer término va al inicio y el cubo del segundo va al final."
    texto=texto+"\n\n1. Se saca la raíz cúbica del primero y la del último. El signo del último no importa: -8 tiene raíz 2."
    texto=texto+"\n2. El segundo término, con más o con menos, debe ser tres veces el cuadrado de la primera raíz por la segunda."
    texto=texto+"\n3. El tercer término debe ser positivo y debe ser tres veces la primera raíz por el cuadrado de la segunda."
    texto=texto+"\n4. El resultado es un paréntesis al cubo. Su signo es el signo del segundo término."
    texto=texto+"\n\nEjemplo: x³ - 6x² + 12x - 8 = (x - 2)³."
    return texto
