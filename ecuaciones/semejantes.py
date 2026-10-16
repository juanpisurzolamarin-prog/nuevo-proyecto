# Suma los términos que se parecen, en un solo lado del igual.


def sumar_terminos_semejantes(terminos):
    # Recibe los términos de un lado, por ejemplo [2,1], [6,0] y [-4,0].
    # Suma los que llevan x entre sí, y los enteros entre sí.
    # Devuelve la x y el entero. En el ejemplo, 2 y 2.
    total_x=0
    total_numero=0
    for termino in terminos:
        if termino[1]==1:
            total_x=total_x+termino[0]
        else:
            total_numero=total_numero+termino[0]
    return total_x,total_numero
