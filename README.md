# Matemáticas 8C

Programa para practicar factorización y congruencia de triángulos.

## Propietario

El proyecto es de **Juan Pablo Urzola Marin**, estudiante de octavo, curso 8C.

Lo hizo para aprender los casos de factorización y la congruencia de triángulos, y para mostrarlo en clase.

## Qué hace

Al abrir el programa aparecen dos temas:

- **Álgebra.** Escribes una expresión y el programa dice el tipo, el caso de factorización y el resultado. También puedes leer el plan de cada caso, con los pasos que se usan en clase.
- **Geometría.** Explica la congruencia de triángulos y deja comparar dos triángulos. El dibujo es un esquema. La congruencia se decide con las marcas y con el criterio LLL, LAL o ALA. La comparación arma una tabla de afirmación y razón.

Los casos de álgebra son estos:

- Factor común
- Factorización por agrupación
- Diferencia de cuadrados
- Trinomio cuadrado perfecto
- Trinomio de la forma x² + bx + c
- Trinomio de la forma ax² + bx + c
- Trinomio cuadrado perfecto por adición y sustracción
- Suma o diferencia de cubos perfectos
- Cubo perfecto de un binomio
- Suma o diferencia de dos potencias iguales
- Cuadrado de un binomio
- Cubo de un binomio

## Cómo abrirlo

1. Abre la carpeta del proyecto.
2. En la terminal, escribe:

```
python main.py
```

Hace falta Python. La ventana usa Tkinter, que ya viene con Python en Windows.

## Cómo se usa el álgebra

1. En la pantalla de inicio, elige **Álgebra**.
2. Pulsa **Factorizar una expresión**.
3. Usa el teclado de la pantalla o escribe la expresión. Las potencias se pueden escribir con `^`, por ejemplo `6x^2 + 9xy`. En la pantalla se ven como 6x² + 9xy.
4. Pulsa **Factorizar**. Abajo aparece el tipo, el caso y el resultado.
5. Si quieres ver cómo se resuelve un caso, vuelve a álgebra y abre el nombre de ese caso. Ahí está el plan.

Para regresar, usa **Volver a álgebra** o **Volver al inicio**.

## Cómo se usa la geometría

1. En la pantalla de inicio, elige **Geometría**.
2. Pulsa **Conceptos** para leer uno por uno. Cada concepto tiene un texto y un dibujo. Están la congruencia, la correspondencia, LLL, LAL, ALA, y las razones que se usan en la tabla: dado, bisectriz, punto medio, lado común, propiedad reflexiva, perpendicular y ángulos opuestos por el vértice.
3. Pulsa **Comparar dos triángulos** para armar la tabla.

Hay dos figuras:

- **Separados.** Compara △ABC con △DEF. A va con D, B con E y C con F. El tamaño del dibujo no importa.
- **Misma figura.** Compara △ABD con △ACD. D está en la mitad de BC. AD parte el ángulo A y es lado de los dos triángulos.

En los triángulos separados:

1. Toca un lado o la letra de un ángulo.
2. Toca la parte que le corresponde en el otro triángulo.
3. Elige por qué son iguales.

En la misma figura:

1. Toca dos partes iguales, o toca AD si es el lado de en medio.
2. Elige el porqué: punto medio, bisectriz, lado común o propiedad reflexiva.

Cuando las marcas alcanzan un criterio, la tabla concluye la congruencia y dice si fue LLL, LAL o ALA.

## Dónde está cada parte

- `main.py` abre la ventana.
- `interfaz.py` muestra el inicio, el álgebra y el paso a la geometría.
- La carpeta `algebra` lee la expresión. Cada caso está en su propio archivo, dentro de `algebra/casos`.
- La carpeta `geometria` tiene los conceptos, los criterios, los dibujos y la pantalla de congruencia.
