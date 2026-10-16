# Este archivo abre el proyecto.
# La pantalla está en interfaz.py.
# El álgebra está en la carpeta algebra. La geometría está en la carpeta geometria.
# Las ecuaciones están en la carpeta ecuaciones.
# La introducción está en la carpeta introduccion.

from interfaz import crear_ventana


def iniciar():
    # No recibe datos.
    # Abre la ventana para escribir una expresión y espera a que la cierres.
    # No devuelve nada.
    ventana=crear_ventana()
    ventana.mainloop()


if __name__=="__main__":
    iniciar()
