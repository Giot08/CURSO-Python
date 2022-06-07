nombre="Víctor Robles"
#funciones generales
print(type(nombre))
#Detectar el tipado
comprobar=isinstance(nombre, str)
if comprobar:
   print ("Esa variables es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print ("La variable no es un numero con defimales")

#Limpiar espacios
frase="  mi contenido    "

print(frase)
print(frase.strip())

#ELiminar variables
year=2022
print(year)
del year
#print(year)

#Comprobar variable vacia
texto="ff"

if len(texto) <= 0:
   print("La variable está vacia")
else:
    print("La variable tiene contenido: ",len(texto))

#Encontrar caracteres
#Encontrar caracteres
frase="La vida es bella"
print(frase.find("vida"))
#Reemplazar palabras en un string
nueva_frase=frase.replace("vida", "moto")
print(nueva_frase)
#Mayusculasyminusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())