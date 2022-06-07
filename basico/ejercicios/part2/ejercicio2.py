"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista

Plus: Usar while y for

"""

num = []
num2 = []

#print(num)
x = 0

while len(num) <= 120:
    #print(x)
    num.append(x)
    x += 1
    #print(x)

print(num)

y = 0
for i in range(0, 121):
    num2.append(y)
    y += 1

print(num2)

