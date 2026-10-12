# Caso del trinomio cuadrado perfecto por adición y sustracción.
# Suma y resta el término que falta, y lo que queda es una diferencia de cuadrados.

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
    # Recibe un término, por ejemplo "4x^2" o "x^4".
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

def texto_de_termino(coeficiente,letras):
    # Recibe el número y las letras de un término.
    # Arma el texto. El 1 no se escribe si hay letras. El -1 se escribe solo con menos.
    # Devuelve "2x^2", "x" o "-1".
    letras_texto=letras_a_texto(letras)
    if coeficiente==-1 and letras_texto!="":
        return "-"+letras_texto
    if coeficiente!=1 or letras_texto=="":
        return str(coeficiente)+letras_texto
    return letras_texto

def copiar_letras(letras):
    # Recibe las letras de un término.
    # Hace otra copia, para no cambiar las originales.
    # Devuelve la copia.
    copia=Counter()
    for letra,potencia in letras.items():
        copia[letra]=potencia
    return copia

def raiz_cuadrada(termino):
    # Recibe un término con raíz, por ejemplo "4x^4" o "9".
    # Saca la raíz del número y divide cada potencia entre 2.
    # Devuelve la raíz, por ejemplo "2x^2" o "3".
    coeficiente=raiz_de_numero(obtener_coeficiente(termino))
    letras_raiz=Counter()
    for letra,potencia in obtener_letras(termino).items():
        letras_raiz[letra]=potencia//2
    return texto_de_termino(coeficiente,letras_raiz)

def doble_producto(raiz1,raiz3):
    # Recibe las dos raíces, por ejemplo "x^2" y "1".
    # Las multiplica y luego multiplica por 2.
    # Devuelve el término, por ejemplo "2x^2".
    coeficiente=2*abs(obtener_coeficiente(raiz1))*abs(obtener_coeficiente(raiz3))
    letras=Counter()
    for letra,potencia in obtener_letras(raiz1).items():
        letras[letra]=letras[letra]+potencia
    for letra,potencia in obtener_letras(raiz3).items():
        letras[letra]=letras[letra]+potencia
    return texto_de_termino(coeficiente,letras)

def mismas_letras(texto1,texto2):
    # Recibe dos textos, por ejemplo "2x^2" y "x^2".
    # Compara las letras y sus potencias, sin mirar el número ni el signo.
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
    # Recibe el doble producto y el término del medio, por ejemplo "2x^2" y "x^2".
    # Compara el número y las letras, sin mirar el signo.
    # Devuelve verdadero si el doble producto ya es el término del medio.
    if obtener_coeficiente(doble)!=abs(obtener_coeficiente(termino_medio)):
        return False
    return mismas_letras(doble,termino_medio)

def con_signo_menos(termino):
    # Recibe un término positivo, por ejemplo "2x^2".
    # Le cambia el signo.
    # Devuelve "-2x^2".
    coeficiente=-abs(obtener_coeficiente(termino))
    return texto_de_termino(coeficiente,obtener_letras(termino))

def termino_que_falta(deseado,medio):
    # Recibe el término que se quiere en el medio y el que está escrito.
    # Resta el del medio. El resultado tiene que ser un cuadrado positivo.
    # Devuelve ese término, por ejemplo "x^2". Si no sirve, devuelve "".
    if not mismas_letras(deseado,medio):
        return ""
    coeficiente=obtener_coeficiente(deseado)-obtener_coeficiente(medio)
    if coeficiente<=0:
        return ""
    faltante=texto_de_termino(coeficiente,obtener_letras(deseado))
    if not tiene_raiz_cuadrada(faltante):
        return ""
    return faltante

def partes_de_termino(termino,signo):
    # Recibe un término positivo y el signo con el que entra al paréntesis.
    # Separa el número y las letras. Si el signo es menos, el número queda negativo.
    # Devuelve el número y una copia de las letras.
    coeficiente=abs(obtener_coeficiente(termino))
    if signo=="-":
        coeficiente=-coeficiente
    return coeficiente,copiar_letras(obtener_letras(termino))

def letras_iguales(letras1,letras2):
    # Recibe las letras de dos términos.
    # Compara cada potencia.
    # Devuelve verdadero si son las mismas.
    if len(letras1)!=len(letras2):
        return False
    for letra in letras1:
        if letra not in letras2:
            return False
        if letras1[letra]!=letras2[letra]:
            return False
    return True

def sumar_iguales(terminos):
    # Recibe una lista de términos, cada uno con su número y sus letras.
    # Si dos tienen las mismas letras, suma sus números.
    # Devuelve la lista sin los que quedaron en cero.
    resultado=[]
    for coeficiente,letras in terminos:
        indice=0
        encontrado=False
        while indice<len(resultado):
            if letras_iguales(resultado[indice][1],letras):
                suma=resultado[indice][0]+coeficiente
                resultado[indice]=(suma,resultado[indice][1])
                encontrado=True
            indice=indice+1
        if not encontrado:
            resultado.append((coeficiente,letras))
    limpia=[]
    for coeficiente,letras in resultado:
        if coeficiente!=0:
            limpia.append((coeficiente,letras))
    return limpia

def grado_de_termino(letras):
    # Recibe las letras de un término.
    # Suma sus potencias. Un número suelto tiene grado 0.
    # Devuelve el grado.
    grado=0
    for letra in letras:
        grado=grado+letras[letra]
    return grado

def va_antes(termino1,termino2):
    # Recibe dos términos ya separados en número y letras.
    # El de mayor exponente va primero. Si empatan, gana el orden alfabético.
    # Devuelve verdadero si el primero debe escribirse antes.
    grado1=grado_de_termino(termino1[1])
    grado2=grado_de_termino(termino2[1])
    if grado1>grado2:
        return True
    if grado1<grado2:
        return False
    if letras_a_texto(termino1[1])<letras_a_texto(termino2[1]):
        return True
    return False

def ordenar_por_exponente(terminos):
    # Recibe la lista de términos de un paréntesis.
    # Los ordena de mayor exponente a menor.
    # Devuelve la misma lista ya ordenada.
    indice=0
    while indice<len(terminos):
        siguiente=indice+1
        while siguiente<len(terminos):
            if va_antes(terminos[siguiente],terminos[indice]):
                guardado=terminos[indice]
                terminos[indice]=terminos[siguiente]
                terminos[siguiente]=guardado
            siguiente=siguiente+1
        indice=indice+1
    return terminos

def parentesis_ordenado(raiz1,signo,raiz3,raiz_falta,signo_falta):
    # Recibe las dos raíces, el signo del trinomio y la raíz de lo que sobra.
    # Arma los tres términos, suma los que sean iguales y los ordena.
    # Devuelve el paréntesis, por ejemplo "(x^2+x+1)".
    terminos=[]
    terminos.append(partes_de_termino(raiz1,"+"))
    terminos.append(partes_de_termino(raiz3,signo))
    terminos.append(partes_de_termino(raiz_falta,signo_falta))
    terminos=sumar_iguales(terminos)
    terminos=ordenar_por_exponente(terminos)
    texto=""
    indice=0
    while indice<len(terminos):
        coeficiente=terminos[indice][0]
        letras=terminos[indice][1]
        if indice==0:
            texto=texto+texto_de_termino(coeficiente,letras)
        else:
            if coeficiente<0:
                texto=texto+"-"+texto_de_termino(abs(coeficiente),letras)
            else:
                texto=texto+"+"+texto_de_termino(coeficiente,letras)
        indice=indice+1
    return "("+texto+")"

def resolver_trinomio_por_adicion_y_sustraccion(division_de_datos):
    # Recibe los términos, por ejemplo ["x^4","+x^2","+1"].
    # Busca el término que falta para armar un trinomio cuadrado perfecto.
    # Factoriza ese cuadrado y la diferencia de cuadrados que queda.
    # Devuelve "(x^2+x+1)(x^2-x+1)". Si no es este caso, devuelve "".
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
            continue
        faltante=termino_que_falta(doble,division_de_datos[medio])
        signo="+"
        if faltante=="":
            faltante=termino_que_falta(con_signo_menos(doble),division_de_datos[medio])
            signo="-"
        if faltante=="":
            continue
        raiz_falta=raiz_cuadrada(faltante)
        parentesis1=parentesis_ordenado(raiz1,signo,raiz3,raiz_falta,"+")
        parentesis2=parentesis_ordenado(raiz1,signo,raiz3,raiz_falta,"-")
        return parentesis1+parentesis2
    return ""

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos del trinomio cuadrado perfecto por adición y sustracción.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa con tres términos. El primero y el tercero tienen raíz cuadrada."
    texto=texto+"\nEl doble producto de esas raíces no es el término del medio. Por eso no es un trinomio cuadrado perfecto todavía."
    texto=texto+"\n\n1. Se busca el término que falta para que el del medio se convierta en el doble producto, sumando o restando."
    texto=texto+"\n2. Ese término se añade sumando y restando. Quedan cuatro términos."
    texto=texto+"\n3. Tres forman un trinomio cuadrado perfecto. El que sobra queda con el signo menos."
    texto=texto+"\n4. El trinomio se factoriza y queda un binomio al cuadrado."
    texto=texto+"\n5. Eso, junto con lo que sobra, es una diferencia de cuadrados. Se factoriza."
    texto=texto+"\n6. Dentro de cada paréntesis, el término de mayor exponente queda primero."
    texto=texto+"\n\nEjemplo: x⁴ + x² + 1 = (x² + x + 1)(x² - x + 1)."
    return texto
