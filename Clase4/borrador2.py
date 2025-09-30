# Generar la tabla de valores aleatorios entre 1 y 99 (16x16)
import random

# Tabla de valores aleatorios (números enteros)
tabla = [
    ["Ana",   "Bea",   "Carmen"],
    ["Diego", "Luis",  "Mario"],
    ["Nora",  "Pablo", "Sofía"]
]

# Ancho de la celda (2 caracteres por valor)
ANCHO = 2

# Línea horizontal
hline = "+" + ("-" * ANCHO * 2 + "+") * 10

# Imprimir la tabla
for i in range(10):  # Filas
    print(hline)  # Imprime la línea horizontal
    for j in range(10):  # Columnas
        # Cada celda alineada al centro en 4 caracteres
        print(f"| {tabla[i][j]:0>{ANCHO}} ", end="")
    print("|")  # Cierra la fila
print(hline)  # Cierra la última línea horizontal