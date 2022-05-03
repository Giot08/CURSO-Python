#Ejemplo1
print("####### EJEMPLO1#######")

#Definir función
def muestraNombre():
     print("Víctor")
     print("Paco")
     print("Juan")
     print("Francisco")
     print("Aitor")
     print("Nestor")
     print("\n")
#Invocar función
muestraNombre()


#Ejemplo 2: parametros
print("####### EJEMPLO2#### ")

def mostrarTuNombre(nombre, edad):

    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad=int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)


#Ejemplo 3
def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")
    for contador in range(11):
        operacion=numero*contador
        print(f"{numero}x{contador}={operacion}")
    print("\n")
tabla(3)
tabla(7)
tabla(12)

#Ejemplo 3.1
print("----------------------------")
for numero_tabla in range(1, 11):
    tabla(numero_tabla)

#Ejemplo 4
#Parametros opcionales
def getEmpleado(nombre, dni=None):
    print ("EMPLEADO")
    print (f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")
getEmpleado("Víctor Robles WEB", 42334242)

#Ejemplo 5: returnodevolver datos
print("####### EJEMPLO5#######")
def saludame (nombre):
    saludo=f"Hola, saludos {nombre}"
    return saludo
print(saludame ("Víctor Robles"))



#Ejemplo6
print("\n####### EJEMPLO6#######")
def calculadora(numero1, numero2, basicas = False):
    suma=numero1+numero2
    resta=numero1
    multi=numero1
    division=numero1 /numero2
    cadena= ''
    if basicas != False:
        cadena += "Suma:"+str(suma)
        cadena += "\n"
        cadena += "Resta:"+str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación:"+str(multi)
        cadena += "\n"
        cadena += "División:"+str(division)
    return cadena
print(calculadora(56, 5))
                                                  

#Ejemplo7
print("\n##### EJEMPLO7 #### ")
def getNombre(nombre):
    texto=f"El nombre es: {nombre}"
    return texto
def getApellidos (apellidos):
    texto=f"Los apellidos son: {apellidos}"
    return texto
def devuelveTodo(nombre, apellidos):
    texto=getNombre(nombre)+"\n"+getApellidos (apellidos)
    return texto
print (devuelveTodo("Víctor", "Robles"))


#Ejemplo 8: Funciones Lambda
print("\n####### EJEMPLO8###")
dime_el_year= lambda year: f"El año es {year*50}"
print(dime_el_year(2034))