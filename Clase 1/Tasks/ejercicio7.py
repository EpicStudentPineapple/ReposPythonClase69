# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

min = int(input("Ingresa minutos a convertir:"))
hor = int(0)

hor = min // 60
minRes = min % 60
    
print(f"{hor} hora(s) y {minRes} minuto(s)")