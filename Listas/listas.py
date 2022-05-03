
pelicula="Batman"

#Definir Lista
peliculas=["Batman", "Spiderman", "El señor de los anillos"]
cantantes=list(('2pac', 'Drake', 'Jennifer Lopez'))
years=list(range(2020, 2050))
variada=["Victor", 30, 4.4, True, "Texto"]

"""

print(peliculas)
print(cantantes)
print(years)
print(variada)


"""
"""

#Indices
pelicula="otra cosa"
peliculas[1]="Gran Torino"
peliculas [2]="El hobbit"
print(peliculas)

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:])

#Añadir elementoaLista
cantantes.append ("Kase 0")
cantantes.append("Natosywaor")
print(cantantes)


#Recorrer Lista
nueva_pelicula= ''
while nueva_pelicula != "parar":
    nueva_pelicula=input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
       peliculas.append (nueva_pelicula)
print("\n*******LISTADO PELICULAS*********")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

"""




#Listas Multidimensionales
print( '\n############ Lista de contactos ###########')

contactos = [
    [
        'antonio',
        'antoni@mail.com'
    ],
    [
        'luis',
        'luis@mail.com'
    ],
    [
        'salvador',
        'salvador@mail.com'
    ],
]

# print(contactos[0][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print('nombre: ' + elemento + '\n')
        else:
            print('email: ' + elemento + '\n')
    #print(contacto[0])