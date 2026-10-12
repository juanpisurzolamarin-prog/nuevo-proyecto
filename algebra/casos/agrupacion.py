# Caso de factorización por agrupación de términos.
# El paso 2 pide el factor común a casos/factor_comun.py. No vuelve a escribir ese caso.

from algebra.expresiones import obtener_coeficiente, obtener_letras, letras_a_texto, separar_terminos
from algebra.casos.factor_comun import calcular_factor_comun


def texto_de_termino(coeficiente,letras):
    # Recibe el número y las letras de un término, por ejemplo -3 y "y".
    # Arma el texto con el signo. El número 1 no se escribe si hay letras.
    # Devuelve "-3" o "-y" o "+2".
    texto=""
    if coeficiente<0:
        texto="-"
    else:
        texto="+"
    if abs(coeficiente)!=1 or letras=="":
        texto=texto+str(abs(coeficiente))
    texto=texto+letras
    return texto

def lista_de_terminos(interior):
    # Recibe lo de adentro de un paréntesis, por ejemplo "y+2" o "3-y".
    # Convierte cada término en un texto con signo y los ordena.
    # Devuelve la lista. Sirve para comparar sin importar el orden.
    terminos=[]
    for parte in separar_terminos(interior):
        coeficiente=obtener_coeficiente(parte)
        letras=letras_a_texto(obtener_letras(parte))
        terminos.append(texto_de_termino(coeficiente,letras))
    terminos.sort()
    return terminos

def parentesis_son_iguales(interior1,interior2):
    # Recibe lo de adentro de los dos paréntesis, por ejemplo "y+2" y "2+y".
    # Compara sus términos sin importar el orden.
    # Devuelve verdadero si son el mismo paréntesis.
    return lista_de_terminos(interior1)==lista_de_terminos(interior2)

def cambiar_signos(interior):
    # Recibe lo de adentro de un paréntesis, por ejemplo "3-y".
    # Cambia cada signo: el más pasa a menos y el menos pasa a más.
    # Devuelve el paréntesis cambiado, por ejemplo "-3+y".
    nuevo=""
    partes=separar_terminos(interior)
    for posicion,parte in enumerate(partes):
        coeficiente=obtener_coeficiente(parte)*-1
        letras=letras_a_texto(obtener_letras(parte))
        numero=""
        if abs(coeficiente)!=1 or letras=="":
            numero=str(abs(coeficiente))
        signo=""
        if coeficiente<0:
            signo="-"
        elif posicion>0:
            signo="+"
        nuevo=nuevo+signo+numero+letras
    return nuevo

def sacar_factor_de_grupo(grupo):
    # Recibe un grupo de dos términos, por ejemplo ["xy","+2x"].
    # Pide el factor común de ese grupo a casos/factor_comun.py.
    # Devuelve el factor de afuera y lo de adentro, por ejemplo "x" y "y+2".
    factor,interior,letras_en_comun=calcular_factor_comun(grupo)
    return factor,interior

def los_parentesis_coinciden(grupo1,grupo2):
    # Recibe los dos grupos.
    # Saca el factor de cada uno y compara lo de adentro.
    # Devuelve verdadero si son iguales o si quedan iguales al cambiar los signos del segundo.
    factor1,interior1=sacar_factor_de_grupo(grupo1)
    factor2,interior2=sacar_factor_de_grupo(grupo2)
    if parentesis_son_iguales(interior1,interior2):
        return True
    if parentesis_son_iguales(interior1,cambiar_signos(interior2)):
        return True
    return False

def buscar_grupos(division_de_datos):
    # Recibe los términos de la expresión.
    # Prueba tres formas de armar dos grupos de dos.
    # Devuelve los dos grupos de la primera forma cuyos paréntesis coinciden.
    # Si no hay 4 términos, o ninguna forma sirve, devuelve una lista vacía.
    if len(division_de_datos)!=4:
        return []
    formas=[
        [[0,1],[2,3]],
        [[0,2],[1,3]],
        [[0,3],[1,2]],
    ]
    for forma in formas:
        grupo1=[division_de_datos[forma[0][0]],division_de_datos[forma[0][1]]]
        grupo2=[division_de_datos[forma[1][0]],division_de_datos[forma[1][1]]]
        if los_parentesis_coinciden(grupo1,grupo2):
            return [grupo1,grupo2]
    return []

def resolver_agrupacion(division_de_datos):
    # Recibe los términos, por ejemplo ["xy","+2x","+3y","+6"].
    # Organiza dos grupos, saca el factor de cada uno y junta afuera con afuera.
    # Si los paréntesis tienen signos contrarios, cambia el signo que los separa y el segundo paréntesis.
    # Devuelve el resultado, por ejemplo "(x+3)(y+2)". Si no se puede, devuelve "".
    grupos=buscar_grupos(division_de_datos)
    if len(grupos)==0:
        return ""

    factor1,interior1=sacar_factor_de_grupo(grupos[0])
    factor2,interior2=sacar_factor_de_grupo(grupos[1])

    operacion="+"
    if not parentesis_son_iguales(interior1,interior2):
        operacion="-"

    afuera=factor1+operacion+factor2
    return "("+afuera+")("+interior1+")"

def plan_del_caso():
    # No recibe datos.
    # Escribe los pasos de la factorización por agrupación.
    # Devuelve el texto que se muestra al entrar a este caso.
    texto="Se usa con cuatro términos. No se mezcla con el factor común de toda la expresión."
    texto=texto+"\n\n1. Se arman dos grupos que tengan factor común."
    texto=texto+"\n2. Se factoriza cada grupo."
    texto=texto+"\n3. Los paréntesis de adentro deben quedar iguales."
    texto=texto+"\n4. Si tienen signos contrarios, se cambia el signo que separa los grupos y todo el segundo paréntesis."
    texto=texto+"\n5. Se juntan los factores de afuera en un paréntesis y se deja el paréntesis de adentro."
    texto=texto+"\n\nEjemplo: xy + 2x + 3y + 6 = (x + 3)(y + 2)."
    return texto
