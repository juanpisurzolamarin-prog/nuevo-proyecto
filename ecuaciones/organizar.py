# Pasa las x a la izquierda y los enteros a la derecha.
# Al cruzar el igual, el término cambia de signo.


def organizar_lados(x_izquierda,numero_izquierda,x_derecha,numero_derecha):
    # Recibe la x y el entero de cada lado, ya sumados.
    # Resta las x de la derecha y resta los enteros de la izquierda.
    # Devuelve la x que queda y el entero que queda. En 2x+2=10, devuelve 2 y 8.
    x_final=x_izquierda-x_derecha
    numero_final=numero_derecha-numero_izquierda
    return x_final,numero_final
