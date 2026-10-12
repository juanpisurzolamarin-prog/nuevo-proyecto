# Captura temporal para revisar los dibujos. Se borra después.

import subprocess
import interfaz
from geometria import pantalla
from geometria.dibujos import vertices_abc, vertices_def, letras_de_los_vertices, punto_medio

ventana=interfaz.crear_ventana()
ventana.attributes("-topmost", True)
ventana.lift()
ventana.focus_force()
ventana.update()
interfaz.mostrar_geometria()
pantalla.ir_a_comparar()
ventana.update()


def clic_lado(triangulo, vertice_1, vertice_2):
    # Clic en el medio de un lado, con el tamaño actual del lienzo.
    ancho, alto=pantalla.tamano_usado()
    if triangulo=="ABC":
        puntos=vertices_abc(ancho, alto)
    else:
        puntos=vertices_def(ancho, alto)
    punto=punto_medio(puntos[vertice_1], puntos[vertice_2])
    pantalla.procesar_clic(punto[0], punto[1])
    ventana.update()


def clic_angulo(triangulo, vertice):
    # Clic en la letra de un ángulo, con el tamaño actual del lienzo.
    ancho, alto=pantalla.tamano_usado()
    if triangulo=="ABC":
        puntos=vertices_abc(ancho, alto)
    else:
        puntos=vertices_def(ancho, alto)
    letras=letras_de_los_vertices(puntos)
    punto=letras[vertice]
    pantalla.procesar_clic(punto[0], punto[1])
    ventana.update()


clic_lado("ABC", "A", "B")
clic_lado("DEF", "D", "E")
pantalla.confirmar_razon("Dado")
clic_angulo("ABC", "B")
clic_angulo("DEF", "E")
pantalla.confirmar_razon("Bisectriz")
clic_lado("ABC", "B", "C")
clic_lado("DEF", "E", "F")
pantalla.confirmar_razon("Punto medio")
ventana.lift()
ventana.attributes("-topmost", True)
ventana.update()
fondo=ventana.winfo_rooty()+ventana.winfo_height()
print("resultado", pantalla.etiqueta_resultado.winfo_rooty(), pantalla.etiqueta_resultado.cget("text")[:40])
print("tabla abajo", pantalla.marco_filas.winfo_rooty()+pantalla.marco_filas.winfo_height())
print("fondo ventana", fondo)

ruta=r"c:\Users\juanp\OneDrive\Documentos\Nuevo proyecto\captura_comparar.png"
x=ventana.winfo_rootx()
y=ventana.winfo_rooty()
w=ventana.winfo_width()
h=ventana.winfo_height()
orden=(
    "Add-Type -AssemblyName System.Drawing; "
    "$b=New-Object System.Drawing.Bitmap "+str(w)+","+str(h)+"; "
    "$g=[System.Drawing.Graphics]::FromImage($b); "
    "$g.CopyFromScreen("+str(x)+","+str(y)+",0,0,(New-Object System.Drawing.Size("+str(w)+","+str(h)+"))); "
    "$b.Save('"+ruta+"'); $g.Dispose(); $b.Dispose()"
)
subprocess.run(["powershell", "-NoProfile", "-Command", orden], check=True)

pantalla.mostrar_un_concepto("Bisectriz")
ventana.lift()
ventana.update()
ruta2=r"c:\Users\juanp\OneDrive\Documentos\Nuevo proyecto\captura_bisectriz.png"
orden2=orden.replace(ruta, ruta2)
subprocess.run(["powershell", "-NoProfile", "-Command", orden2], check=True)

pantalla.mostrar_un_concepto("Ángulos opuestos por el vértice")
ventana.lift()
ventana.update()
ruta3=r"c:\Users\juanp\OneDrive\Documentos\Nuevo proyecto\captura_opuestos.png"
subprocess.run(["powershell", "-NoProfile", "-Command", orden.replace(ruta, ruta3)], check=True)

ventana.destroy()
print("capturas listas", w, h)
