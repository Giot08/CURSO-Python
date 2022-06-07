"""

Diccionario es parecido a un json o array asociativo.

"""

personas = {
    "id": "001",
    "nombre": "miguel",
    "web": "google.com",
}

print(type(personas))

print(personas["id"])

#lsita con diccionarios

contactos = [
    {
        'nombre' : 'jose',
        'mail' : 'jose@mail.com',
        'tlf' : '9876543210',
    },
    {
        'nombre' : 'pedro',
        'mail' : 'pedro@mail.com',
        'tlf' : '12353466',
    },
    {
        'nombre' : 'lana',
        'mail' : 'lana@mail.com',
        'tlf' : '567567657567',
    },
]

contactos[0][ 'nombre']="Antoñito"
print(contactos[0]['nombre'])

print("\nListado de contactos: ")

for contacto in contactos:
   print (f"Nombre del contacto: {contacto['nombre']}")
   print (f"Email del contacto: {contacto['mail']}")
   print (f"-------------------------------------")