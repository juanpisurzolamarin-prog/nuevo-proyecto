# Textos de la ecuación de primer grado.
# La pantalla los muestra juntos, en una sola página.


def texto_de_conceptos_y_procesos():
    # No recibe datos.
    # Escribe qué es la ecuación y el orden en que se resuelve.
    # Devuelve el texto completo de la página.
    texto="Una ecuación de primer grado tiene una incógnita y un igual."
    texto=texto+" La incógnita es x. Puede repetirse, como en 2x+3x, pero no puede haber otra letra."
    texto=texto+" La x no lleva potencia."
    texto=texto+"\n\nEl igual separa dos lados que valen lo mismo."
    texto=texto+" Los signos de agrupación son ( ), [ ] y { }."
    texto=texto+" El número que multiplica va antes del paréntesis, como en 2(x+3) o -(x-1)."
    texto=texto+"\n\nTérminos semejantes son los que se pueden sumar."
    texto=texto+" Las x se suman con las x. Los enteros se suman con los enteros."
    texto=texto+"\n\nCómo se resuelve"
    texto=texto+"\n1. Se opera el paréntesis más interno, hasta que no quede ninguno."
    texto=texto+" El número de afuera multiplica cada término de adentro. 3(x-1) pasa a 3x-3."
    texto=texto+"\n2. Se suman los términos semejantes de cada lado."
    texto=texto+"\n3. Las x quedan a la izquierda y los enteros a la derecha."
    texto=texto+" Al cruzar el igual, el término cambia de signo."
    texto=texto+"\n4. Se opera otra vez cada lado."
    texto=texto+"\n5. La x no puede quedar negativa. Si queda negativa, se cambian los signos de los dos lados."
    texto=texto+" -x=2 pasa a x=-2."
    texto=texto+"\n6. Si la x queda multiplicada por un entero, ese entero pasa a dividir al otro lado."
    texto=texto+"\n7. Si la fracción se puede simplificar, se simplifica."
    texto=texto+"\n8. La respuesta queda como entero, por ejemplo x=4, o como fracción, por ejemplo x=3/2."
    return texto

def texto_de_las_fracciones():
    # No recibe datos.
    # Escribe qué es una ecuación fraccionaria y el paso del mínimo común múltiplo.
    # Devuelve el texto completo de esa página.
    texto="Una ecuación fraccionaria tiene fracciones y un igual."
    texto=texto+" La incógnita sigue siendo x. Puede repetirse, pero no puede haber otra letra."
    texto=texto+"\n\nEl denominador es un monomio: un entero, x o un entero por x."
    texto=texto+" Sirven 2, x y 2x. No sirve una suma ni una potencia."
    texto=texto+" El numerador puede ser un entero, x o una expresión entre paréntesis, como (x+1)."
    texto=texto+" Si un término no tiene denominador, el denominador es 1."
    texto=texto+" En x/2+3=5, el 3 y el 5 tienen denominador 1."
    texto=texto+"\n\nPaso previo: el mínimo común múltiplo"
    texto=texto+"\n1. Se sacan los denominadores."
    texto=texto+"\n2. Se dividen por números primos. El primo más pequeño que divida a alguno se usa primero."
    texto=texto+" El que no se pueda dividir se queda igual."
    texto=texto+"\n3. Se repite hasta que todos queden en 1."
    texto=texto+"\n4. El mínimo común múltiplo es el producto de esos primos."
    texto=texto+" Con 4, 6 y 3 se usa 2, otra vez 2 y después 3. El resultado es 12."
    texto=texto+"\n5. Si algún denominador tiene x, el mínimo común múltiplo también lleva x."
    texto=texto+"\n\nCon ese número se divide cada denominador y el resultado multiplica a su numerador."
    texto=texto+" Así desaparecen las fracciones."
    texto=texto+" En x/2+1/3=5/6 el mínimo común múltiplo es 6 y queda 3x+2=5."
    texto=texto+"\n\nDespués se resuelve como una ecuación de primer grado:"
    texto=texto+" se quitan paréntesis, se suman términos semejantes,"
    texto=texto+" las x pasan a un lado y los enteros al otro,"
    texto=texto+" se cambia el signo si la x queda negativa y se divide si hace falta."
    texto=texto+"\n\nEl 0 no puede ser respuesta si anula un denominador."
    texto=texto+" En 1/x=1/x cualquier número cumple, menos el 0."
    return texto
