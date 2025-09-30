# 1) Algoritmo que pida dos números e indique si el primero es mayor que el segundo.

num1 = int(input("Dame número:"))
num2 = int(input("Dame otro número:"))

if (num1 > num2):
    print(f"{num1} es mayor que {num2}.")
elif (num1 < num2):
    print(f"{num1} es menor que {num2}.")
else:
    print("Los números son iguales.")
print("Programa finalizado.")