# Deja la x sola.
# Si queda negativa se cambian los signos. Si tiene un entero, ese entero divide.


def cambiar_signo_si_la_x_es_negativa(coeficiente,numero):
    # Recibe el número que acompaña a la x y el entero del otro lado.
    # Si la x es negativa, cambia el signo de los dos lados. Por ejemplo, -x=2 pasa a x=-2.
    # Devuelve los dos números ya con el signo corregido.
    if coeficiente<0:
        return -coeficiente,-numero
    return coeficiente,numero

def valor_absoluto(numero):
    # Recibe un entero, por ejemplo -6.
    # Le quita el signo.
    # Devuelve 6. Si ya era positivo, lo devuelve igual.
    if numero<0:
        return -numero
    return numero

def mcd(primer_numero,segundo_numero):
    # Recibe dos enteros, por ejemplo 8 y 12.
    # Busca el mayor número que divide a los dos, usando el residuo.
    # Devuelve 4.
    primer_numero=valor_absoluto(primer_numero)
    segundo_numero=valor_absoluto(segundo_numero)
    while segundo_numero!=0:
        resto=primer_numero%segundo_numero
        primer_numero=segundo_numero
        segundo_numero=resto
    if primer_numero==0:
        return 1
    return primer_numero

def simplificar_fraccion(numerador,denominador):
    # Recibe el numerador y el denominador, por ejemplo 8 y 6.
    # Los divide por su máximo común divisor.
    # Devuelve 4 y 3. Si el denominador queda 1, el resultado es un entero.
    if denominador<0:
        numerador=-numerador
        denominador=-denominador
    divisor=mcd(numerador,denominador)
    return numerador//divisor,denominador//divisor

def texto_de_la_respuesta(coeficiente,numero,caso):
    # Recibe lo que acompaña a la x, el entero del otro lado y el nombre del caso.
    # Arma el resultado. Si se puede, simplifica la fracción.
    # Devuelve el texto de la pantalla, por ejemplo "x = 3/2".
    if coeficiente==0 and numero==0:
        return caso+"\nResultado: cualquier número cumple."
    if coeficiente==0:
        return caso+"\nResultado: no tiene solución."
    if coeficiente==1:
        return caso+"\nResultado: x = "+str(numero)
    numerador,denominador=simplificar_fraccion(numero,coeficiente)
    if denominador==1:
        return caso+"\nResultado: x = "+str(numerador)
    return caso+"\nResultado: x = "+str(numerador)+"/"+str(denominador)
