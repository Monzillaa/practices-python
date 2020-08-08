juegos = [
    { 
        "nombre": "Resident Evil 2",
        "calificacion": 99,
    },
    {
        "nombre": "Crash Bandicoot N. Sane Trilogy",
        "calificacion": 76,
    },

    {
        "nombre": "Cuphead",
        "calificacion": 100,
    },
    {
        "nombre": "Minecraft",
        "calificacion": 80,
    },
    {
        "nombre": "Bioshock",
        "calificacion": 95,
    },
]
mascotasArray =[
    {
        "nombre": "Uno",
        "peso": 5.200,
    },
    {
        "nombre": "Orión",
        "peso": 13,
    },
    {
        "nombre": "Zero",
        "peso": 3.800,
    },
    {
        "nombre": "Dosh",
        "peso": 4.100,
    },
    {
        "nombre":"Nini",
        "peso": 5.300,
    },
    {
        "nombre":"Mushu",
        "peso": 5,
    },
]
#Declaramos la variable que dictara la clave por la que se ordenara el arreglo
def funcion_que_devuelve_clave(juego):
    # Vamos a ordenar basándonos en su calificación, y como se nos
    # va a pasar un diccionario, devolvemos el elemento "calificacion"
    return juego["calificacion"]

def function_that_returns_key(mascota):
    return mascota["peso"]

print('\n')
print("Originalmente es: ")
#imprime la lista de juegos
for juego in juegos:
    print(juego)
print('\n')

print("Listado Original: ")
for mascota in mascotasArray:
    print(mascota)
print('\n')

# La ordenamos
juegos_ordenados = sorted(juegos, key=funcion_que_devuelve_clave)
print("Ordenada por calificación ascendente: ")
for juego in juegos_ordenados:
    print(juego)
print('\n')

mascotasOrdenadas = sorted(mascotasArray, key=function_that_returns_key)
print("Ordena por peso ascendente: ")
for mascota in mascotasOrdenadas:
    print(mascota)
print('\n')

# También se puede en orden inverso
juegos_ordenados = sorted(juegos, key=funcion_que_devuelve_clave, reverse=True)
print("Ordenada por calificación descendente: ")
for juego in juegos_ordenados:
    print(juego)
print('\n')

mascotasOrdenadas = sorted(mascotasArray, key=function_that_returns_key, reverse=True)
print("Ordenada por peso descendente: ")
for mascota in mascotasOrdenadas: 
    print(mascota)
=======
juegos = [
    { 
        "nombre": "Resident Evil 2",
        "calificacion": 99,
    },
    {
        "nombre": "Crash Bandicoot N. Sane Trilogy",
        "calificacion": 76,
    },

    {
        "nombre": "Cuphead",
        "calificacion": 100,
    },
    {
        "nombre": "Minecraft",
        "calificacion": 80,
    },
    {
        "nombre": "Bioshock",
        "calificacion": 95,
    },
]
mascotasArray =[
    {
        "nombre": "Uno",
        "peso": 5.200,
    },
    {
        "nombre": "Orión",
        "peso": 13,
    },
    {
        "nombre": "Zero",
        "peso": 3.800,
    },
    {
        "nombre": "Dosh",
        "peso": 4.100,
    },
    {
        "nombre":"Nini",
        "peso": 5.300,
    },
    {
        "nombre":"Mushu",
        "peso": 5,
    },
]
#Declaramos la variable que dictara la clave por la que se ordenara el arreglo
def funcion_que_devuelve_clave(juego):
    # Vamos a ordenar basándonos en su calificación, y como se nos
    # va a pasar un diccionario, devolvemos el elemento "calificacion"
    return juego["calificacion"]

def function_that_returns_key(mascota):
    return mascota["peso"]

print('\n')
print("Originalmente es: ")
#imprime la lista de juegos
for juego in juegos:
    print(juego)
print('\n')

print("Listado Original: ")
for mascota in mascotasArray:
    print(mascota)
print('\n')

# La ordenamos
juegos_ordenados = sorted(juegos, key=funcion_que_devuelve_clave)
print("Ordenada por calificación ascendente: ")
for juego in juegos_ordenados:
    print(juego)
print('\n')

mascotasOrdenadas = sorted(mascotasArray, key=function_that_returns_key)
print("Ordena por peso ascendente: ")
for mascota in mascotasOrdenadas:
    print(mascota)
print('\n')

# También se puede en orden inverso
juegos_ordenados = sorted(juegos, key=funcion_que_devuelve_clave, reverse=True)
print("Ordenada por calificación descendente: ")
for juego in juegos_ordenados:
    print(juego)
print('\n')

mascotasOrdenadas = sorted(mascotasArray, key=function_that_returns_key, reverse=True)
print("Ordenada por peso descendente: ")
for mascota in mascotasOrdenadas: 
    print(mascota)
>>>>>>> aa07b41050d5f99dddc96ad2a6fd0167d5f2bcbe
