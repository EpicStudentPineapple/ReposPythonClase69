# 2) Algoritmo que pida un número y diga si es positivo, negativo o 0.

num = int(input("Dame un número:"))

if(num > 0):
    print(f"{num} es positivo")
elif(num < 0):
    print(f"{num} es negativo")
else:
    print(f"Esto es un cero")