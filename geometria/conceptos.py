# Textos de congruencia de triángulos.
# Cada concepto tiene su propio párrafo.
# La pantalla los muestra junto con un dibujo.


def armar_concepto(nombre, texto, dibujo):
    # Recibe el nombre, el párrafo y la clave del dibujo.
    # Guarda los tres datos juntos para la pantalla.
    # Devuelve un diccionario.
    concepto={}
    concepto["nombre"]=nombre
    concepto["texto"]=texto
    concepto["dibujo"]=dibujo
    return concepto

def texto_congruencia():
    # No recibe datos.
    # Explica que dos triángulos congruentes miden lo mismo.
    # Devuelve el párrafo.
    texto="Dos triángulos son congruentes cuando tienen la misma forma y el mismo tamaño."
    texto=texto+" Sus lados y sus ángulos correspondientes son iguales."
    texto=texto+" Se escribe así: △ABC ≅ △DEF."
    texto=texto+" El símbolo ≅ se lee «es congruente con»."
    return texto

def texto_correspondencia():
    # No recibe datos.
    # Explica qué letra de un triángulo va con cuál letra del otro.
    # Devuelve el párrafo.
    texto="El orden de las letras dice la correspondencia."
    texto=texto+" En △ABC ≅ △DEF, A va con D, B va con E y C va con F."
    texto=texto+" Los lados correspondientes son AB con DE, BC con EF y CA con FD."
    texto=texto+" Los ángulos correspondientes son ∠A con ∠D, ∠B con ∠E y ∠C con ∠F."
    return texto

def texto_lll():
    # No recibe datos.
    # Explica el criterio lado, lado, lado.
    # Devuelve el párrafo.
    texto="LLL significa lado, lado, lado."
    texto=texto+" Si los tres lados de un triángulo son iguales a los tres lados del otro, los triángulos son congruentes."
    texto=texto+" En nuestra correspondencia hacen falta AB ≅ DE, BC ≅ EF y CA ≅ FD."
    return texto

def texto_lal():
    # No recibe datos.
    # Explica el criterio lado, ángulo, lado.
    # Devuelve el párrafo.
    texto="LAL significa lado, ángulo, lado."
    texto=texto+" Hacen falta dos lados y el ángulo que está entre ellos, el ángulo comprendido."
    texto=texto+" Por ejemplo: AB ≅ DE, ∠B ≅ ∠E y BC ≅ EF."
    texto=texto+" El ángulo B queda entre los lados AB y BC."
    return texto

def texto_ala():
    # No recibe datos.
    # Explica el criterio ángulo, lado, ángulo.
    # Devuelve el párrafo.
    texto="ALA significa ángulo, lado, ángulo."
    texto=texto+" Hacen falta dos ángulos y el lado que está entre ellos, el lado comprendido."
    texto=texto+" Por ejemplo: ∠A ≅ ∠D, AB ≅ DE y ∠B ≅ ∠E."
    texto=texto+" El lado AB queda entre los ángulos A y B."
    return texto

def texto_aaa():
    # No recibe datos.
    # Explica por qué tres ángulos iguales no alcanzan para la congruencia.
    # Devuelve el párrafo.
    texto="AAA significa ángulo, ángulo, ángulo."
    texto=texto+" Si solo se sabe que los tres ángulos son iguales, los triángulos pueden tener la misma forma y distinto tamaño."
    texto=texto+" Eso es semejanza, no congruencia."
    texto=texto+" AAA no es un criterio de congruencia."
    return texto

def texto_dado():
    # No recibe datos.
    # Explica la razón que se copia del enunciado.
    # Devuelve el párrafo.
    texto="Un dato es una información que el problema ya entrega."
    texto=texto+" En la tabla, la columna Razón dice Dado."
    texto=texto+" No hace falta demostrarlo: se usa tal como viene en el enunciado."
    return texto

def texto_bisectriz():
    # No recibe datos.
    # Explica que la bisectriz parte un ángulo en dos ángulos iguales.
    # Devuelve el párrafo.
    texto="La bisectriz de un ángulo lo divide en dos ángulos iguales."
    texto=texto+" Si una semirrecta es bisectriz, los dos ángulos que forma son congruentes."
    texto=texto+" En la columna Razón se escribe Bisectriz."
    return texto

def texto_punto_medio():
    # No recibe datos.
    # Explica que el punto medio parte un segmento en dos partes iguales.
    # Devuelve el párrafo.
    texto="El punto medio de un segmento lo divide en dos partes iguales."
    texto=texto+" Si M es el punto medio de AB, entonces AM ≅ MB."
    texto=texto+" En la columna Razón se escribe Punto medio."
    return texto

def texto_lado_comun():
    # No recibe datos.
    # Explica el lado que pertenece a los dos triángulos a la vez.
    # Devuelve el párrafo.
    texto="A veces el mismo lado pertenece a los dos triángulos."
    texto=texto+" Ese lado se llama lado común."
    texto=texto+" En la comparación de esta pantalla los triángulos están separados."
    texto=texto+" El lado común se ve en una figura donde los dos triángulos comparten un segmento."
    return texto

def texto_reflexiva():
    # No recibe datos.
    # Explica que un segmento es congruente consigo mismo.
    # Devuelve el párrafo.
    texto="La propiedad reflexiva dice que una cosa es congruente consigo misma."
    texto=texto+" Un segmento es congruente consigo mismo: AC ≅ AC."
    texto=texto+" Sirve para justificar el lado común."
    texto=texto+" En la columna Razón se escribe Propiedad reflexiva."
    return texto

def texto_perpendicular():
    # No recibe datos.
    # Explica que dos rectas perpendiculares forman un ángulo de 90 grados.
    # Devuelve el párrafo.
    texto="Dos rectas perpendiculares se cortan y forman un ángulo de 90 grados."
    texto=texto+" Si AD es perpendicular a BC, los ángulos en D son rectos."
    texto=texto+" Dos ángulos rectos son congruentes."
    texto=texto+" En la columna Razón se escribe Perpendicular."
    return texto

def texto_opuestos():
    # No recibe datos.
    # Explica los ángulos que quedan frente a frente cuando dos rectas se cruzan.
    # Devuelve el párrafo.
    texto="Cuando dos rectas se cruzan, forman cuatro ángulos."
    texto=texto+" Los que quedan frente a frente se llaman ángulos opuestos por el vértice y son iguales."
    texto=texto+" En la columna Razón se escribe Ángulos opuestos por el vértice."
    return texto

def lista_de_conceptos():
    # No recibe datos.
    # Junta el nombre, el texto y el dibujo de cada concepto, en el orden de la clase.
    # Devuelve una lista de diccionarios.
    conceptos=[]
    conceptos.append(armar_concepto("Congruencia", texto_congruencia(), "congruencia"))
    conceptos.append(armar_concepto("Correspondencia de vértices", texto_correspondencia(), "correspondencia"))
    conceptos.append(armar_concepto("Criterio LLL", texto_lll(), "lll"))
    conceptos.append(armar_concepto("Criterio LAL", texto_lal(), "lal"))
    conceptos.append(armar_concepto("Criterio ALA", texto_ala(), "ala"))
    conceptos.append(armar_concepto("AAA no es congruencia", texto_aaa(), "aaa"))
    conceptos.append(armar_concepto("Dado", texto_dado(), "dado"))
    conceptos.append(armar_concepto("Bisectriz", texto_bisectriz(), "bisectriz"))
    conceptos.append(armar_concepto("Punto medio", texto_punto_medio(), "punto_medio"))
    conceptos.append(armar_concepto("Lado común", texto_lado_comun(), "lado_comun"))
    conceptos.append(armar_concepto("Propiedad reflexiva", texto_reflexiva(), "reflexiva"))
    conceptos.append(armar_concepto("Perpendicular", texto_perpendicular(), "perpendicular"))
    conceptos.append(armar_concepto("Ángulos opuestos por el vértice", texto_opuestos(), "opuestos"))
    return conceptos

def buscar_concepto(nombre):
    # Recibe el nombre de un concepto, por ejemplo "Bisectriz".
    # Lo busca en la lista.
    # Devuelve el diccionario. Si no está, devuelve None.
    for concepto in lista_de_conceptos():
        if concepto["nombre"]==nombre:
            return concepto
    return None
