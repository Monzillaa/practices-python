archivo = "input.txt"
salida = "result.txt"
busqueda = input("Ingresa búsqueda: ")
lineas_escribir = []
contador = 0
#Metodo para leer el archivo
with open(archivo, "r") as archivo_lectura:
    numero_linea = 0
#Recorre linea or linea el archivo
    for linea in archivo_lectura:
        numero_linea += 1
#Metodo split elimina los espacios al final de cada oración
        linea = linea.rstrip()
#Divide en arreglos cada palabra para poder recorrerlo
        separado = linea.split(" ")
#Busca dentro de los arreglos la palabra alojada en la variable busqueda
        if busqueda in separado:
            contador += 1
            lineas_escribir.append(str(numero_linea) + " - " + linea)
#Metddo pra crear el archivo
with open(salida, "w") as archivo_salida:
    for linea in lineas_escribir:
        archivo_salida.write(linea + "\n")
#Imprime el resultado del contador se puede colocar arriba del metodo open fuera del for
print('se detecto '+ str(contador)+' veces')
