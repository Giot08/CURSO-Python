"""
Ejercicio 1.
Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Ordenarla y mostrarla
- Mostrar su longitud
- buscar algun elemento( que el usuario pida por teclado)
"""

lista = [1,5,3,4,2,6,7,8]
print(f'lista: {lista}')

for i in lista:
    print(f'El numero en la lista es: {i}')

lista.sort()
print(f'lista ordenada: {lista}')

print(f'La longitud de la lista es: {len(lista)}')

var = int(input('introduce el nro a buscar: \n'))

print(f'la posicion de el numero {var} es de: {lista.index(var)}')