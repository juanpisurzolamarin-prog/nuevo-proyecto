# Reglas de desarrollo

Este proyecto lo hace un estudiante de 13 años, grado octavo, para aprender los casos de factorización y mostrarlo a su profesora.

## Cómo se escribe

- Comentarios, nombres y textos de la pantalla van en español claro.
- Cada cambio debe poder explicarse en voz alta en clase.
- Si algo es difícil, se divide en pasos pequeños con nombres que digan qué hacen.

## Cómo son las funciones

- Una función hace una sola cosa.
- Se usan `if`, `for` y variables con nombre claro.
- Toda función lleva un comentario encima que dice qué recibe, qué hace y qué devuelve.
- El comentario va en español, con un ejemplo corto cuando ayude.

```python
# Recibe un término como "-12ab".
# Separa el signo y el número.
# Devuelve el coeficiente, por ejemplo -12. Si no hay número, devuelve 1 o -1.
def obtener_coeficiente(termino):
    ...
```

- Cada caso de factorización (factor común, diferencia de cuadrados, trinomio y los demás) va en su propia función, con su propio comentario.
- La pantalla solo pide la expresión y muestra el caso y el resultado. La matemática queda en funciones aparte.

## Dónde va cada tema

- El álgebra está en la carpeta `algebra`: la lectura de expresiones y cada caso de factorización.
- La geometría está en la carpeta `geometria`, sin mezclarla con el álgebra.

## Congruencia de triángulos

- Cada criterio (LLL, LAL y ALA) va en su propia función.
- La pantalla explica los conceptos, dibuja dos triángulos y muestra la tabla de afirmación y razón.
- El dibujo es un esquema. La congruencia se decide por las marcas y el criterio.
- En la comparación se hace clic en un lado o en la letra de un ángulo, luego en la parte del otro triángulo, y se elige la razón.
