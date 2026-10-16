# Quita los signos de agrupación, de adentro hacia afuera.
# El número de la izquierda multiplica cada término de adentro.


def tiene_signo_de_agrupacion(texto):
    # Recibe un texto, por ejemplo "2(x+1)".
    # Busca paréntesis, corchetes o llaves.
    # Devuelve True si hay alguno. Si no hay, devuelve False.
    if "(" in texto:
        return True
    if "[" in texto:
        return True
    if "{" in texto:
        return True
    if ")" in texto or "]" in texto or "}" in texto:
        return True
    return False

def posicion_del_primer_cierre(texto):
    # Recibe un texto con signos de agrupación.
    # Busca el primer cierre: ), ] o }.
    # Devuelve su posición. Si no hay cierre, devuelve -1.
    indice=0
    while indice<len(texto):
        if texto[indice] in ")]}":
            return indice
        indice=indice+1
    return -1

def apertura_que_corresponde(cierre):
    # Recibe un cierre, por ejemplo ")".
    # Busca la apertura del mismo tipo.
    # Devuelve "(", "[" o "{".
    if cierre==")":
        return "("
    if cierre=="]":
        return "["
    return "{"

def posicion_de_la_apertura(texto,posicion_cierre):
    # Recibe el texto y la posición del primer cierre.
    # Camina hacia la izquierda hasta la apertura de ese grupo.
    # Devuelve su posición. Si no está, devuelve -1.
    buscada=apertura_que_corresponde(texto[posicion_cierre])
    indice=posicion_cierre-1
    while indice>=0:
        if texto[indice]==buscada:
            return indice
        indice=indice-1
    return -1

def leer_factor(texto,posicion_apertura):
    # Recibe el texto y dónde abre el grupo, como en "2(x+3)".
    # Lee el entero que está pegado a la izquierda. Si solo hay un menos, el factor es -1.
    # Devuelve el factor, la posición donde empieza y un aviso. Si sale bien, el aviso es "".
    if posicion_apertura==0:
        return 1,0,""
    indice=posicion_apertura-1
    if texto[indice]=="x" or texto[indice] in ")]}":
        return 0,0,"El número va antes del paréntesis. Ejemplo: 2(x+3)."
    fin=indice
    while indice>=0 and texto[indice].isdigit():
        indice=indice-1
    numero_texto=texto[indice+1:fin+1]
    if numero_texto!="" and indice>=0 and texto[indice]=="x":
        return 0,0,"El número va antes del paréntesis. Ejemplo: 2(x+3)."
    signo=1
    inicio=indice+1
    if indice>=0 and (texto[indice]=="+" or texto[indice]=="-"):
        if texto[indice]=="-":
            signo=-1
        inicio=indice
    if numero_texto=="":
        factor=signo
    else:
        factor=signo*int(numero_texto)
    return factor,inicio,""

def separar_terminos(texto):
    # Recibe un lado o el interior de un paréntesis, por ejemplo "3x-3+4".
    # Separa cada término y guarda su número y si lleva x.
    # Devuelve la lista y un aviso. En el ejemplo, [[3,1],[-3,0],[4,0]] y "".
    if texto=="":
        return [],"Falta un lado de la ecuación."
    terminos=[]
    indice=0
    while indice<len(texto):
        signo=1
        if texto[indice]=="+":
            indice=indice+1
        elif texto[indice]=="-":
            signo=-1
            indice=indice+1
        elif len(terminos)>0:
            return [],"No pude leer esa ecuación."
        if indice>=len(texto):
            return [],"No pude leer esa ecuación."
        inicio=indice
        while indice<len(texto) and texto[indice].isdigit():
            indice=indice+1
        numero_texto=texto[inicio:indice]
        con_x=0
        if indice<len(texto) and texto[indice]=="x":
            con_x=1
            indice=indice+1
        if indice<len(texto) and texto[indice]=="^":
            return [],"La x no puede tener potencia. Eso no es de primer grado."
        if numero_texto=="" and con_x==0:
            return [],"No pude leer esa ecuación."
        if numero_texto=="":
            numero=signo
        else:
            numero=signo*int(numero_texto)
        terminos.append([numero,con_x])
    return terminos,""

def multiplicar_terminos(terminos,factor):
    # Recibe los términos de adentro y el factor, por ejemplo 3.
    # Multiplica el número de cada término por ese factor.
    # Devuelve la lista nueva. 3 por [1,1] y [-1,0] da [3,1] y [-3,0].
    nuevos=[]
    for termino in terminos:
        nuevos.append([termino[0]*factor,termino[1]])
    return nuevos

def texto_de_un_termino(numero,con_x):
    # Recibe el número y 1 si lleva x, como -3 y 1.
    # Lo escribe como en el cuaderno.
    # Devuelve "-3x". Si el número es 1 y lleva x, devuelve "x".
    if con_x==1:
        if numero==1:
            return "x"
        if numero==-1:
            return "-x"
        return str(numero)+"x"
    return str(numero)

def texto_de_los_terminos(terminos):
    # Recibe la lista de términos ya multiplicados.
    # Los junta con más o con menos.
    # Devuelve un texto, por ejemplo "3x-3".
    if len(terminos)==0:
        return "0"
    texto=texto_de_un_termino(terminos[0][0],terminos[0][1])
    indice=1
    while indice<len(terminos):
        numero=terminos[indice][0]
        if numero<0:
            positivo=-numero
        else:
            positivo=numero
        pedazo=texto_de_un_termino(positivo,terminos[indice][1])
        if numero<0:
            texto=texto+"-"+pedazo
        else:
            texto=texto+"+"+pedazo
        indice=indice+1
    return texto

def quitar_el_parentesis_mas_interno(texto):
    # Recibe un texto, por ejemplo "2[3(x-1)+4]".
    # Quita solo el grupo más interno y multiplica lo de adentro.
    # Devuelve el texto nuevo y un aviso. En el ejemplo, "2[3x-3+4]" y "".
    posicion_cierre=posicion_del_primer_cierre(texto)
    if posicion_cierre==-1:
        return "","Revisa los signos de agrupación."
    posicion_apertura=posicion_de_la_apertura(texto,posicion_cierre)
    if posicion_apertura==-1:
        return "","Revisa los signos de agrupación."
    if posicion_cierre+1<len(texto) and texto[posicion_cierre+1] in "0123456789x([{":
        return "","El número va antes del paréntesis. Ejemplo: 2(x+3)."
    interior=texto[posicion_apertura+1:posicion_cierre]
    if tiene_signo_de_agrupacion(interior):
        return "","Revisa los signos de agrupación."
    factor,inicio,aviso=leer_factor(texto,posicion_apertura)
    if aviso!="":
        return "",aviso
    terminos,aviso=separar_terminos(interior)
    if aviso!="":
        return "",aviso
    terminos=multiplicar_terminos(terminos,factor)
    reemplazo=texto_de_los_terminos(terminos)
    if inicio>0 and reemplazo[0]!="-":
        reemplazo="+"+reemplazo
    nuevo=texto[0:inicio]+reemplazo+texto[posicion_cierre+1:]
    return nuevo,""

def quitar_todos_los_parentesis(texto):
    # Recibe la ecuación, por ejemplo "2[3(x-1)+4]=20".
    # Repite el grupo más interno hasta que no quede ninguno.
    # Devuelve el texto sin agrupación y un aviso. Si sale bien, el aviso es "".
    vueltas=0
    while tiene_signo_de_agrupacion(texto):
        texto,aviso=quitar_el_parentesis_mas_interno(texto)
        if aviso!="":
            return "",aviso
        vueltas=vueltas+1
        if vueltas>40:
            return "","Revisa los signos de agrupación."
    return texto,""
