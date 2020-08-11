import random

def generar_lista_enteros(minimo, maximo, longitud):
	return [random.randint(minimo, maximo) for _ in range(longitud)]

def generar_lista_flotantes(minimo, maximo, longitud):
	return [random.uniform(minimo, maximo) for _ in range(longitud)]


enteros_aleatorios = generar_lista_enteros(1, 10, 5)
print("Enteros: " + str(enteros_aleatorios))
flotantes_aleatorios = generar_lista_flotantes(20, 100, 5)
print("Flotantes: " + str(flotantes_aleatorios))