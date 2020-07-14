demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red', 'red', 'red', 'green', 'blue']

##Definimos las listas a travez de un constroctor o funcion llamado list
numbers_list = list((1,2,3,4))
print(numbers_list)
#print(type(numbers_list))

#r = list(range(1, 10))
#print(r)
#print(dir(colors))
#print(len(demo_list))
#print(colors[2])
#print("green" in colors)

# print(colors)
# colors[1] = 'yellow'
# print(colors)

#print(dir(colors))
##agregar elementos a una lista
#colors.append('violet')
##extiende los elementos en la lista
#colors.extend(['violet', 'yellow'])
#colors.extend(['pink', 'black'])
#colors.insert(-1, 'violet')
##cuenta la longitud y coloca al final de la lista el elementp
# colors.insert(len(colors),'violet')
# print(colors)
##elimina el ultimo elemento de la lista si no especifico el indice
# colors.pop()
#colors.pop(1)
#print(colors)

##remueve un elemento en especifico
#colors.remove('green')
#print(colors)

##limpiar toda la lista 
#colors.clear()
##ordena la lista alfabeticamente si se deja vacio
#si colocas reverse en los parentesis lo hace de forma inversa
#colors.sort(reverse=True)
##imprimir el indice del valor
#print(colors.index('blue'))
##imprime cuantas veces esta almacenado un elemento
print(colors)
print(colors.count('red'))