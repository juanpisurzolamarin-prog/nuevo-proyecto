# Quita las fracciones de una ecuación con denominadores monomios.
# Primero saca el MCM. Después multiplica cada numerador y resuelve como primer grado.

from ecuaciones.reconocer import preparar_ecuacion,contar_iguales,aviso_de_las_letras
from ecuaciones.parentesis import quitar_todos_los_parentesis,separar_terminos
from ecuaciones.mcm import mcm_de_monomios
from ecuaciones.resolver import separar_lados,coeficiente_y_numero
from ecuaciones.despejar import texto_de_la_respuesta


def aviso_de_los_caracteres(ecuacion):
    # Recibe la ecuación ya preparada.
    # Deja pasar números, x, signos, paréntesis, la barra y el igual.
    # Devuelve un aviso si hay otro carácter. Si no, devuelve "".
    permitidos="0123456789x+-()[]{}=/"
    for caracter in ecuacion:
        if caracter not in permitidos:
            return "No pude leer esa ecuación.\nEjemplo: x/2+1/3=5/6"
    return ""

def aviso_si_no_es_fraccionaria(ecuacion):
    # Recibe la ecuación ya preparada, por ejemplo "x/2+1/3=5/6".
    # Comprueba el igual, la x y los caracteres.
    # Devuelve un aviso si no se puede leer. Si se puede, devuelve "".
    if ecuacion=="":
        return "Escribe una ecuación.\nEjemplo: x/2+1/3=5/6"
    cantidad=contar_iguales(ecuacion)
    if cantidad==0:
        return "La ecuación debe tener un igual."
    if cantidad>1:
        return "La ecuación debe tener un solo igual."
    aviso=aviso_de_las_letras(ecuacion)
    if aviso!="":
        return aviso
    return aviso_de_los_caracteres(ecuacion)

def partir_en_terminos(lado):
    # Recibe un lado, por ejemplo "x/2+1/3".
    # Corta en cada más o menos que no esté dentro de paréntesis.
    # Devuelve la lista y un aviso. En el ejemplo, ["x/2","+1/3"] y "".
    if lado=="":
        return [],"Falta un lado de la ecuación."
    terminos=[]
    actual=""
    profundidad=0
    indice=0
    while indice<len(lado):
        caracter=lado[indice]
        if caracter in "([{":
            profundidad=profundidad+1
            actual=actual+caracter
        elif caracter in ")]}":
            profundidad=profundidad-1
            if profundidad<0:
                return [],"Revisa los signos de agrupación."
            actual=actual+caracter
        elif profundidad==0 and (caracter=="+" or caracter=="-") and actual!="":
            terminos.append(actual)
            actual=caracter
        else:
            actual=actual+caracter
        indice=indice+1
    if profundidad!=0:
        return [],"Revisa los signos de agrupación."
    if actual!="":
        terminos.append(actual)
    if len(terminos)==0:
        return [],"Falta un lado de la ecuación."
    return terminos,""

def separar_numerador_y_denominador(termino):
    # Recibe un término, por ejemplo "+1/3" o "(x+1)/2" o "3".
    # Separa el signo, el numerador y el denominador. Si no hay barra, el denominador es 1.
    # Devuelve el signo, los dos textos y un aviso. Si sale bien, el aviso es "".
    if termino=="":
        return 0,"","","Falta un término."
    signo=1
    texto=termino
    if texto[0]=="+":
        texto=texto[1:]
    elif texto[0]=="-":
        signo=-1
        texto=texto[1:]
    if texto=="":
        return 0,"","","Falta el numerador."
    profundidad=0
    posicion_barra=-1
    indice=0
    while indice<len(texto):
        caracter=texto[indice]
        if caracter in "([{":
            profundidad=profundidad+1
        elif caracter in ")]}":
            profundidad=profundidad-1
            if profundidad<0:
                return 0,"","","Revisa los signos de agrupación."
        elif caracter=="/" and profundidad==0:
            if posicion_barra!=-1:
                return 0,"","","Cada término puede tener una sola fracción."
            posicion_barra=indice
        indice=indice+1
    if profundidad!=0:
        return 0,"","","Revisa los signos de agrupación."
    if posicion_barra==-1:
        return signo,texto,"1",""
    numerador=texto[0:posicion_barra]
    denominador=texto[posicion_barra+1:]
    if numerador=="":
        return 0,"","","Falta el numerador."
    if denominador=="":
        return 0,"","","Falta el denominador."
    return signo,numerador,denominador,""

def cierre_de(apertura):
    # Recibe una apertura, por ejemplo "(".
    # Busca el cierre del mismo tipo.
    # Devuelve ")", "]" o "}".
    if apertura=="(":
        return ")"
    if apertura=="[":
        return "]"
    return "}"

def es_un_grupo_completo(texto):
    # Recibe un texto, por ejemplo "(2x)" o "2x".
    # Mira si todo el texto es un solo paréntesis, corchete o llave.
    # Devuelve True si lo es. Si no, devuelve False.
    if len(texto)<2:
        return False
    if texto[0] not in "([{":
        return False
    if texto[len(texto)-1]!=cierre_de(texto[0]):
        return False
    profundidad=0
    indice=0
    while indice<len(texto):
        if texto[indice] in "([{":
            profundidad=profundidad+1
        elif texto[indice] in ")]}":
            profundidad=profundidad-1
            if profundidad==0 and indice!=len(texto)-1:
                return False
        indice=indice+1
    if profundidad!=0:
        return False
    return True

def quitar_el_grupo_externo(texto):
    # Recibe un denominador, por ejemplo "(2x)".
    # Le quita un paréntesis que lo envuelva por completo.
    # Devuelve "2x". Si no había grupo, devuelve el mismo texto.
    if es_un_grupo_completo(texto):
        return texto[1:len(texto)-1]
    return texto

def leer_monomio(texto):
    # Recibe un denominador, por ejemplo "2", "x", "2x" o "(2x)".
    # Lee el entero positivo y si lleva x. El signo queda aparte.
    # Devuelve el monomio, el signo y un aviso. Si el denominador es 0, avisa.
    texto=quitar_el_grupo_externo(texto)
    if texto=="":
        return [],0,"Falta el denominador."
    signo=1
    indice=0
    if texto[0]=="+":
        indice=1
    elif texto[0]=="-":
        signo=-1
        indice=1
    inicio=indice
    while indice<len(texto) and texto[indice].isdigit():
        indice=indice+1
    numero_texto=texto[inicio:indice]
    lleva_x=0
    if indice<len(texto) and texto[indice]=="x":
        lleva_x=1
        indice=indice+1
    if indice!=len(texto):
        return [],0,"El denominador debe ser un monomio, como 2, x o 2x."
    if numero_texto=="" and lleva_x==0:
        return [],0,"El denominador debe ser un monomio, como 2, x o 2x."
    if numero_texto=="":
        numero=1
    else:
        numero=int(numero_texto)
    if numero==0:
        return [],0,"El denominador no puede ser 0."
    return [numero,lleva_x],signo,""

def terminos_del_numerador(numerador,signo):
    # Recibe el numerador, por ejemplo "(x+1)", y el signo de delante.
    # Quita paréntesis y aplica el signo a cada término.
    # Devuelve la lista y un aviso. En el ejemplo, [[1,1],[1,0]] si el signo es 1.
    numerador,aviso=quitar_todos_los_parentesis(numerador)
    if aviso!="":
        return [],aviso
    terminos,aviso=separar_terminos(numerador)
    if aviso!="":
        return [],aviso
    nuevos=[]
    for termino in terminos:
        nuevos.append([termino[0]*signo,termino[1]])
    return nuevos,""

def leer_fraccion(termino):
    # Recibe un término ya cortado, por ejemplo "x/2" o "+3".
    # Guarda el numerador en términos y el denominador como monomio.
    # Devuelve [terminos, numero, lleva_x] y un aviso.
    signo,numerador,denominador,aviso=separar_numerador_y_denominador(termino)
    if aviso!="":
        return [],aviso
    monomio,signo_denominador,aviso=leer_monomio(denominador)
    if aviso!="":
        return [],aviso
    terminos,aviso=terminos_del_numerador(numerador,signo*signo_denominador)
    if aviso!="":
        return [],aviso
    return [terminos,monomio[0],monomio[1]],""

def fracciones_de_un_lado(lado):
    # Recibe un lado de la ecuación, por ejemplo "x/2+3".
    # Lee cada término. Si no tiene barra, el denominador queda en 1.
    # Devuelve la lista de fracciones y un aviso.
    pedazos,aviso=partir_en_terminos(lado)
    if aviso!="":
        return [],aviso
    fracciones=[]
    for pedazo in pedazos:
        fraccion,aviso=leer_fraccion(pedazo)
        if aviso!="":
            return [],aviso
        fracciones.append(fraccion)
    return fracciones,""

def multiplicar_numerador(terminos,multiplicador,x_extra):
    # Recibe los términos del numerador, el entero MCM/denominador y 1 si todavía falta una x.
    # Multiplica. Si x por x, ya no es de primer grado.
    # Devuelve los términos nuevos y un aviso.
    nuevos=[]
    for termino in terminos:
        numero=termino[0]*multiplicador
        con_x=termino[1]
        if x_extra==1:
            if con_x==1:
                return [],"Eso ya no es de primer grado."
            con_x=1
        nuevos.append([numero,con_x])
    return nuevos,""

def quitar_fracciones_de_un_lado(fracciones,mcm):
    # Recibe las fracciones de un lado y el MCM, por ejemplo [6,0].
    # A cada una la multiplica por el MCM dividido entre su denominador.
    # Devuelve todos los términos ya sin denominador, y un aviso.
    todos=[]
    for fraccion in fracciones:
        numero_denominador=fraccion[1]
        if mcm[0]%numero_denominador!=0:
            return [],"No pude sacar el mínimo común múltiplo."
        multiplicador=mcm[0]//numero_denominador
        x_extra=0
        if mcm[1]==1 and fraccion[2]==0:
            x_extra=1
        nuevos,aviso=multiplicar_numerador(fraccion[0],multiplicador,x_extra)
        if aviso!="":
            return [],aviso
        for termino in nuevos:
            todos.append(termino)
    return todos,""

def hay_x_en_los_denominadores(fracciones):
    # Recibe las fracciones de los dos lados.
    # Mira si algún denominador tiene x.
    # Devuelve 1 si la tiene. Si ninguna la tiene, devuelve 0.
    for fraccion in fracciones:
        if fraccion[2]==1:
            return 1
    return 0

def texto_fraccionario(coeficiente,numero,hay_x):
    # Recibe lo que acompaña a la x, el entero y 1 si algún denominador tenía x.
    # Arma el caso. Si la respuesta anula un denominador, lo dice.
    # Devuelve el texto de la pantalla.
    caso="Caso: ecuación fraccionaria con denominadores monomios"
    if hay_x==1 and coeficiente==0 and numero==0:
        return caso+"\nResultado: cualquier número cumple, menos el 0."
    if hay_x==1 and coeficiente!=0 and numero==0:
        return caso+"\nResultado: no tiene solución, porque el 0 anula un denominador."
    return texto_de_la_respuesta(coeficiente,numero,caso)

def texto_de_la_fraccionaria(ecuacion):
    # Recibe lo que se escribió, por ejemplo "x/2+1/3=5/6".
    # Saca el MCM, quita los denominadores y resuelve como primer grado.
    # Devuelve el caso y el resultado, o el aviso si no se puede.
    ecuacion=preparar_ecuacion(ecuacion)
    aviso=aviso_si_no_es_fraccionaria(ecuacion)
    if aviso!="":
        return aviso
    izquierda,derecha=separar_lados(ecuacion)
    fracciones_izquierda,aviso=fracciones_de_un_lado(izquierda)
    if aviso!="":
        return aviso
    fracciones_derecha,aviso=fracciones_de_un_lado(derecha)
    if aviso!="":
        return aviso
    denominadores=[]
    for fraccion in fracciones_izquierda:
        denominadores.append([fraccion[1],fraccion[2]])
    for fraccion in fracciones_derecha:
        denominadores.append([fraccion[1],fraccion[2]])
    mcm=mcm_de_monomios(denominadores)
    if mcm[0]==0:
        return "No pude sacar el mínimo común múltiplo."
    terminos_izquierda,aviso=quitar_fracciones_de_un_lado(fracciones_izquierda,mcm)
    if aviso!="":
        return aviso
    terminos_derecha,aviso=quitar_fracciones_de_un_lado(fracciones_derecha,mcm)
    if aviso!="":
        return aviso
    coeficiente,numero=coeficiente_y_numero(terminos_izquierda,terminos_derecha)
    hay_x=hay_x_en_los_denominadores(fracciones_izquierda+fracciones_derecha)
    return texto_fraccionario(coeficiente,numero,hay_x)
