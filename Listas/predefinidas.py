cantantes = ['muse', 'imagine dragons', 'maroon 5']
numeros = [1, 2, 3, 7, 5, 9]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos

cantantes.append('Metallica')
print(cantantes)
cantantes.insert(2, 'RAGE')
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
print(cantantes)
cantantes.remove('RAGE')
print(cantantes)

# Dar la vuelta
numeros.reverse()
print(numeros)

#buscar elementos
print('muse' in cantantes)
