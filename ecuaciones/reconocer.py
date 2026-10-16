# Revisa si el texto es una ecuación de primer grado.
# La única letra permitida es x, y debe haber un solo igual.


def preparar_ecuacion(ecuacion):
    # Recibe el texto escrito, por ejemplo "2(x + 3) = 10".
    # Quita los espacios y usa la x minúscula.
    # Devuelve "2(x+3)=10".
    ecuacion=ecuacion.replace(" ","")
    ecuacion=ecuacion.replace("X","x")
    return ecuacion

def contar_iguales(ecuacion):
    # Recibe la ecuación ya preparada.
    # Cuenta cuántos signos igual tiene.
    # Devuelve ese número. En "2x=4" devuelve 1.
    cantidad=0
    for caracter in ecuacion:
        if caracter=="=":
            cantidad=cantidad+1
    return cantidad

def aviso_de_las_letras(ecuacion):
    # Recibe la ecuación ya preparada.
    # Revisa que la única letra sea x y que x no tenga potencia.
    # Devuelve un aviso si no sirve. Si sirve, devuelve "".
    hay_x=False
    for caracter in ecuacion:
        if caracter=="x":
            hay_x=True
        elif caracter.isalpha():
            return "Solo puede haber una incógnita, la x."
        elif caracter=="^" or caracter in "⁰¹²³⁴⁵⁶⁷⁸⁹":
            return "La x no puede tener potencia. Eso no es de primer grado."
    if hay_x==False:
        return "La ecuación debe tener la incógnita x."
    return ""

def aviso_de_los_caracteres(ecuacion):
    # Recibe la ecuación ya preparada.
    # Deja pasar números, x, signos, paréntesis y el igual.
    # Devuelve un aviso si hay otro carácter. Si no, devuelve "".
    permitidos="0123456789x+-()[]{}="
    for caracter in ecuacion:
        if caracter not in permitidos:
            return "No pude leer esa ecuación.\nEjemplo: 2(x+3)-4=10"
    return ""

def aviso_si_no_es_de_primer_grado(ecuacion):
    # Recibe la ecuación ya preparada, por ejemplo "2(x+3)=10".
    # Comprueba el igual, la x y los caracteres.
    # Devuelve un aviso si no es de primer grado. Si lo es, devuelve "".
    if ecuacion=="":
        return "Escribe una ecuación.\nEjemplo: 2(x+3)=10"
    cantidad=contar_iguales(ecuacion)
    if cantidad==0:
        return "La ecuación debe tener un igual."
    if cantidad>1:
        return "La ecuación debe tener un solo igual."
    aviso=aviso_de_las_letras(ecuacion)
    if aviso!="":
        return aviso
    return aviso_de_los_caracteres(ecuacion)
