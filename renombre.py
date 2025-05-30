import os

# Definimos la ruta de la carpeta con los archivos
carpeta = "C:/Users/manue/OneDrive/Escritorio/5 Archivos"

# Función que renombra los archivos
def renombrar_archivos(ruta):
    for nombre_archivo in os.listdir(ruta):
        origen = os.path.join(ruta, nombre_archivo)
        # Evita renombrar el script o archivos ya renombrados
        if nombre_archivo.startswith("nuevo_") or nombre_archivo.endswith(".py"):
            continue
        nuevo_nombre = os.path.join(ruta, "nuevo_" + nombre_archivo)
        os.rename(origen, nuevo_nombre)
        print(f"Renombrado: {origen} -> {nuevo_nombre}")

# Llamamos la función
renombrar_archivos(carpeta)

