# Criterios de congruencia LLL, LAL y ALA.
# Cada criterio está en su propia función.
# La correspondencia usada es △ABC ≅ △DEF.

lados_correspondientes={
    "AB":"DE",
    "BC":"EF",
    "CA":"FD",
}

angulos_correspondientes={
    "A":"D",
    "B":"E",
    "C":"F",
}

grupos_lal=[
    ["AB","B","BC"],
    ["BC","C","CA"],
    ["CA","A","AB"],
]

grupos_ala=[
    ["A","AB","B"],
    ["B","BC","C"],
    ["C","CA","A"],
]


def lado_que_corresponde(lado_abc):
    # Recibe un lado de ABC, por ejemplo "AB".
    # Busca el lado de DEF que le corresponde.
    # Devuelve "DE".
    return lados_correspondientes[lado_abc]

def angulo_que_corresponde(angulo_abc):
    # Recibe un ángulo de ABC, por ejemplo "B".
    # Busca el ángulo de DEF que le corresponde.
    # Devuelve "E".
    return angulos_correspondientes[angulo_abc]

def tiene_lado(marcas, lado_abc):
    # Recibe las marcas y un lado de ABC, por ejemplo "AB".
    # Busca si ese lado está marcado con su lado correspondiente.
    # Devuelve True si el par está. Si no está, devuelve False.
    esperado=lado_que_corresponde(lado_abc)
    for marca in marcas:
        es_lado=marca["tipo"]=="lado"
        es_el_lado=marca["parte_abc"]==lado_abc
        es_el_correspondiente=marca["parte_def"]==esperado
        if es_lado and es_el_lado and es_el_correspondiente:
            return True
    return False

def tiene_angulo(marcas, angulo_abc):
    # Recibe las marcas y un ángulo de ABC, por ejemplo "B".
    # Busca si ese ángulo está marcado con su ángulo correspondiente.
    # Devuelve True si el par está. Si no está, devuelve False.
    esperado=angulo_que_corresponde(angulo_abc)
    for marca in marcas:
        es_angulo=marca["tipo"]=="angulo"
        es_el_angulo=marca["parte_abc"]==angulo_abc
        es_el_correspondiente=marca["parte_def"]==esperado
        if es_angulo and es_el_angulo and es_el_correspondiente:
            return True
    return False

def se_cumple_lll(marcas):
    # Recibe la lista de marcas.
    # Revisa si los tres pares de lados correspondientes están marcados.
    # Devuelve True si se cumple LLL. Si falta un lado, devuelve False.
    if tiene_lado(marcas,"AB")==False:
        return False
    if tiene_lado(marcas,"BC")==False:
        return False
    if tiene_lado(marcas,"CA")==False:
        return False
    return True

def se_cumple_lal(marcas):
    # Recibe la lista de marcas.
    # Revisa si hay dos lados correspondientes y el ángulo comprendido entre ellos.
    # Devuelve True si se cumple LAL. Si falta una parte, devuelve False.
    for grupo in grupos_lal:
        lado_1=grupo[0]
        angulo=grupo[1]
        lado_2=grupo[2]
        lados_listos=tiene_lado(marcas, lado_1) and tiene_lado(marcas, lado_2)
        angulo_listo=tiene_angulo(marcas, angulo)
        if lados_listos and angulo_listo:
            return True
    return False

def se_cumple_ala(marcas):
    # Recibe la lista de marcas.
    # Revisa si hay dos ángulos correspondientes y el lado comprendido entre ellos.
    # Devuelve True si se cumple ALA. Si falta una parte, devuelve False.
    for grupo in grupos_ala:
        angulo_1=grupo[0]
        lado=grupo[1]
        angulo_2=grupo[2]
        angulos_listos=tiene_angulo(marcas, angulo_1) and tiene_angulo(marcas, angulo_2)
        lado_listo=tiene_lado(marcas, lado)
        if angulos_listos and lado_listo:
            return True
    return False

def criterios_que_se_cumplen(marcas):
    # Recibe la lista de marcas.
    # Prueba LLL, luego LAL y luego ALA.
    # Devuelve los nombres que sí se cumplen, por ejemplo ["LLL"].
    nombres=[]
    if se_cumple_lll(marcas):
        nombres.append("LLL")
    if se_cumple_lal(marcas):
        nombres.append("LAL")
    if se_cumple_ala(marcas):
        nombres.append("ALA")
    return nombres

def razon_de_la_congruencia(marcas):
    # Recibe la lista de marcas.
    # Elige el primer criterio que se cumple, en el orden LLL, LAL, ALA.
    # Devuelve "Criterio LAL". Si no se cumple ninguno, devuelve "".
    nombres=criterios_que_se_cumplen(marcas)
    if len(nombres)==0:
        return ""
    return "Criterio "+nombres[0]

def texto_de_afirmacion(marca):
    # Recibe una marca, por ejemplo el lado AB con el lado DE.
    # Escribe la congruencia con el símbolo ≅.
    # Devuelve "AB ≅ DE" o "∠B ≅ ∠E".
    if marca["tipo"]=="lado":
        return marca["parte_abc"]+" ≅ "+marca["parte_def"]
    return "∠"+marca["parte_abc"]+" ≅ ∠"+marca["parte_def"]

def filas_de_la_comprobacion(marcas):
    # Recibe la lista de marcas.
    # Arma la tabla de afirmación y razón. Si ya hay criterio, agrega la última fila.
    # Devuelve una lista de pares, por ejemplo [["AB ≅ DE", "Dado"]].
    filas=[]
    for marca in marcas:
        filas.append([texto_de_afirmacion(marca), marca["razon"]])
    razon=razon_de_la_congruencia(marcas)
    if razon!="":
        filas.append(["△ABC ≅ △DEF", razon])
    return filas

def contar_lados_correspondientes(marcas):
    # Recibe la lista de marcas.
    # Cuenta cuántos lados de ABC están con su lado correspondiente.
    # Devuelve un número de 0 a 3.
    total=0
    for lado in lados_correspondientes:
        if tiene_lado(marcas, lado):
            total=total+1
    return total

def contar_angulos_correspondientes(marcas):
    # Recibe la lista de marcas.
    # Cuenta cuántos ángulos de ABC están con su ángulo correspondiente.
    # Devuelve un número de 0 a 3.
    total=0
    for angulo in angulos_correspondientes:
        if tiene_angulo(marcas, angulo):
            total=total+1
    return total

def frases_de_marcas_sin_correspondencia(marcas):
    # Recibe la lista de marcas.
    # Busca las que unen partes que no se corresponden en △ABC ≅ △DEF.
    # Devuelve una frase por cada una.
    frases=[]
    for marca in marcas:
        if marca["tipo"]=="lado":
            esperado=lado_que_corresponde(marca["parte_abc"])
            if marca["parte_def"]!=esperado:
                frase=marca["parte_abc"]+" no corresponde a "+marca["parte_def"]+"."
                frase=frase+" En △ABC ≅ △DEF, el lado "+marca["parte_abc"]+" corresponde a "+esperado+"."
                frases.append(frase)
        else:
            esperado=angulo_que_corresponde(marca["parte_abc"])
            if marca["parte_def"]!=esperado:
                frase="∠"+marca["parte_abc"]+" no corresponde a ∠"+marca["parte_def"]+"."
                frase=frase+" En △ABC ≅ △DEF, el ángulo "+marca["parte_abc"]+" corresponde a "+esperado+"."
                frases.append(frase)
    return frases

def frase_de_otros_criterios(nombres):
    # Recibe los criterios que también se cumplen, por ejemplo ["LAL"].
    # Arma la frase que va después del criterio principal.
    # Devuelve "También se cumple LAL."
    if len(nombres)==1:
        return "También se cumple "+nombres[0]+"."
    return "También se cumplen "+nombres[0]+" y "+nombres[1]+"."

def texto_del_resultado(marcas):
    # Recibe la lista de marcas.
    # Dice si los triángulos ya son congruentes o si todavía falta información.
    # Devuelve el párrafo que va debajo de la tabla.
    if len(marcas)==0:
        return "Todavía no hay marcas.\nHaz clic en un lado o en la letra de un ángulo."

    nombres=criterios_que_se_cumplen(marcas)
    if len(nombres)==0:
        texto="Todavía no hay información suficiente para concluir que △ABC ≅ △DEF."
        lados=contar_lados_correspondientes(marcas)
        angulos=contar_angulos_correspondientes(marcas)
        texto=texto+"\nLados correspondientes: "+str(lados)+" de 3."
        texto=texto+"\nÁngulos correspondientes: "+str(angulos)+" de 3."
    else:
        texto="Los triángulos son congruentes por el criterio "+nombres[0]+"."
        if len(nombres)>1:
            texto=texto+" "+frase_de_otros_criterios(nombres[1:])

    frases=frases_de_marcas_sin_correspondencia(marcas)
    for frase in frases:
        texto=texto+"\n"+frase
    return texto
