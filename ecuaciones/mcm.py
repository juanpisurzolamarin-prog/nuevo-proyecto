# Mínimo común múltiplo de los denominadores.
# Se hace con el método de números primos, como en clase.


def es_primo(numero):
    # Recibe un entero, por ejemplo 4 o 5.
    # Revisa si solo se puede dividir por 1 y por sí mismo.
    # Devuelve True si es primo. Si no, devuelve False.
    if numero<2:
        return False
    divisor=2
    while divisor*divisor<=numero:
        if numero%divisor==0:
            return False
        divisor=divisor+1
    return True

def siguiente_primo(actual):
    # Recibe un primo, por ejemplo 2.
    # Busca el primo que le sigue.
    # Devuelve 3.
    candidato=actual+1
    while es_primo(candidato)==False:
        candidato=candidato+1
    return candidato

def copiar_numeros(numeros):
    # Recibe la lista de enteros de los denominadores.
    # Hace otra lista igual, para no cambiar la original.
    # Devuelve la copia.
    copia=[]
    for numero in numeros:
        copia.append(numero)
    return copia

def todos_son_uno(numeros):
    # Recibe la lista que se va dividiendo.
    # Mira si cada número ya quedó en 1.
    # Devuelve True si todos son 1. Si falta alguno, devuelve False.
    for numero in numeros:
        if numero!=1:
            return False
    return True

def alguno_se_divide(numeros,primo):
    # Recibe la lista y un primo, por ejemplo 2.
    # Mira si ese primo divide a alguno.
    # Devuelve True si divide al menos a uno.
    for numero in numeros:
        if numero%primo==0:
            return True
    return False

def mcm_de_numeros(numeros):
    # Recibe enteros positivos, por ejemplo 4, 6 y 3.
    # Los divide por primos. El que no se pueda dividir se queda igual.
    # Devuelve el producto de esos primos. En el ejemplo, 12.
    actuales=copiar_numeros(numeros)
    if len(actuales)==0:
        return 1
    primo=2
    mcm=1
    vueltas=0
    while todos_son_uno(actuales)==False:
        if alguno_se_divide(actuales,primo):
            mcm=mcm*primo
            indice=0
            while indice<len(actuales):
                if actuales[indice]%primo==0:
                    actuales[indice]=actuales[indice]//primo
                indice=indice+1
        else:
            primo=siguiente_primo(primo)
        vueltas=vueltas+1
        if vueltas>80:
            return 0
    return mcm

def mcm_de_monomios(denominadores):
    # Recibe monomios, cada uno con su número y 1 si lleva x. Por ejemplo [2,0], [3,0] y [6,0].
    # Saca el MCM de los números y, si alguno tiene x, el MCM también lleva x.
    # Devuelve el número y 1 o 0. En el ejemplo, [6,0].
    numeros=[]
    lleva_x=0
    for denominador in denominadores:
        numeros.append(denominador[0])
        if denominador[1]==1:
            lleva_x=1
    numero=mcm_de_numeros(numeros)
    return [numero,lleva_x]
