# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math

cAdyacente = int (input("Ingresa cateto Adyacente:"))
cContiguo = int (input("Ingresa cateto Contiguo:"))

hyp = math.sqrt((cAdyacente**2) + (cContiguo**2))

print("la hipotenusa es:", hyp)