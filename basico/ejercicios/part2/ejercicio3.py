"""
Ejercicio 3. Programa que compruebe si una variable está vacia
y si está vacia, rellenerla con texto en minusculas y mostrarlo
en mayusculas.
"""
x = ''

print(x)
if(x == ''):
    print(f'{x} x esta vacio')
    x = input("\ningresa el nuevo texto: \n")
    print(x.upper())
else:
    print(f'\"{x}\", es el contenido de x')