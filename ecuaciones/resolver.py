# Resuelve la ecuación en el orden de la clase.
# La pantalla solo muestra el texto que devuelve este archivo.

from ecuaciones.reconocer import preparar_ecuacion,aviso_si_no_es_de_primer_grado
from ecuaciones.parentesis import quitar_todos_los_parentesis,separar_terminos
from ecuaciones.semejantes import sumar_terminos_semejantes
from ecuaciones.organizar import organizar_lados
from ecuaciones.despejar import cambiar_signo_si_la_x_es_negativa,texto_de_la_respuesta


def separar_lados(ecuacion):
    # Recibe la ecuación sin paréntesis, por ejemplo "2x+2=10".
    # Corta en el igual.
    # Devuelve el lado izquierdo y el derecho, "2x+2" y "10".
    posicion=0
    while posicion<len(ecuacion):
        if ecuacion[posicion]=="=":
            izquierda=ecuacion[0:posicion]
            derecha=ecuacion[posicion+1:]
            return izquierda,derecha
        posicion=posicion+1
    return "",""

def coeficiente_y_numero(terminos_izquierda,terminos_derecha):
    # Recibe los términos de cada lado, ya sin paréntesis ni denominadores.
    # Suma semejantes, pasa las x a la izquierda y cambia el signo si la x queda negativa.
    # Devuelve el número que acompaña a la x y el entero del otro lado.
    x_izquierda,numero_izquierda=sumar_terminos_semejantes(terminos_izquierda)
    x_derecha,numero_derecha=sumar_terminos_semejantes(terminos_derecha)
    x_final,numero_final=organizar_lados(x_izquierda,numero_izquierda,x_derecha,numero_derecha)
    x_final,numero_final=cambiar_signo_si_la_x_es_negativa(x_final,numero_final)
    return x_final,numero_final

def texto_del_resultado(ecuacion):
    # Recibe lo que se escribió, por ejemplo "2(x+3)-4=10".
    # Quita paréntesis, suma semejantes, organiza y despeja la x.
    # Devuelve el caso y el resultado, o el aviso si no se puede resolver.
    ecuacion=preparar_ecuacion(ecuacion)
    aviso=aviso_si_no_es_de_primer_grado(ecuacion)
    if aviso!="":
        return aviso
    ecuacion,aviso=quitar_todos_los_parentesis(ecuacion)
    if aviso!="":
        return aviso
    izquierda,derecha=separar_lados(ecuacion)
    terminos_izquierda,aviso=separar_terminos(izquierda)
    if aviso!="":
        return aviso
    terminos_derecha,aviso=separar_terminos(derecha)
    if aviso!="":
        return aviso
    coeficiente,numero=coeficiente_y_numero(terminos_izquierda,terminos_derecha)
    caso="Caso: ecuación de primer grado con signos de agrupación"
    return texto_de_la_respuesta(coeficiente,numero,caso)
