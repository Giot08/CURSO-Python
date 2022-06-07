"""

# ejercicio nro 1
print("ejercicio 1")
pais = "chile"
continente = "America"
year = 2022

print(f"{pais} - {continente} - {str(year)}")

# ejercicio nro 2
print("ejercicio 2")

num = 1
for num in range (1, 121):
    if num%2 == 0:
        print(num)
    # else: print(f"{num} es impar")

# ejercicio nro 3
print("ejercicio 3")

Ejercicio 3:
escribir un programa que muestre 
los cuadrados de los primero 60 
numeros

    #while
contador = 0
while contador <=60:
    cuadrado = contador*contador
    contador += 1
    print(f"{cuadrado}")

    #for
for numero in range(61):
    cuadrado = numero * numero 
    print(f"{cuadrado}")

# ejercicio nro 4
print("ejercicio 4")

# Pedir dos numeros enteros y realizar operaciones aritmeticas.

num1 = int(input("primer numero \n"))
num2 = int(input("primer numero \n"))

print(f"suma: {str(num1 + num2)}")
print(f"resta: {str(num1 - num2)}")
print(f"division: {str(num1 / num2)}")
print(f"multiplicacion: {str(num1 * num2)}")
# que diga usuario

# ejercicio nro 5
print("ejercicio 5")

#Hacer in programa que muestre 
# los numeros entre dos numeros 
# que diga usuario

num1 = int(input("num1"))
num2 = int(input("num2"))

if num1 < num2:
    for contador in range(num1, num2):
        print(contador)
else:
    print("num1 debe ser menor a num2")

# ejercicio nro 6
print("ejercicio 6")

# Mostrar las tablas de multiplicar entre un numero

for cabecera in range(1, 11):
    print("###########")
    print(f"##### Tabla del {cabecera} ######")
    print("###########")
    for numero in range(1, 11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")

    print("\n")


# ejercicio nro 7
print("ejercicio 7")

# mostrar todos los numeros impares entre dos numeros

num1 = int(input("primer numero"))
num2 = int(input("segundo numero"))
if num1 < num2:
    for i in range(num1, (num2 + 1)):
        if i%2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")
else:
    print("num1 debe ser mayor que num2")

# ejercicio nro 8
print("ejercicio 8")

# sacar un porcentaje de un numero

num1 = int(input("primer num \n"))
porcentaje = int(input(f"que porcentaje quieres sacar de {num1} \n"))

resultado = (num1 * (porcentaje/100))
print(f"\nes {resultado} ")


# ejercicio nro 9
print("ejercicio 9")

#hacer un programa que pida 
# numero al usuario hasta que 
# el usuario inserte el num 
# correcto.

contador = 1
while contador < 100:
    numero = int(input("introduce un numero \n"))
    if numero == 111:
        print(f"has introducido el num correcto {numero}")
        break
    else:
        print(f"has introduciodo el {numero}")


"""

# ejercicio nro 10
print("ejercicio 10")

#programa que muestra alumnos reprobados

contador = 0
aprobados = 0
suspendidos = 0

num_alumnos = int(input("cuantos alumnos tienes: ? \n"))

while contador <= num_alumnos:
    nota = int(input(f"que nota quieres ponerle al \"alumno{contador}\" "))

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

    contador += 1

print(f"alumnos aprobados {aprobados}")
print(f"alumnos suspendidos {suspendidos}")