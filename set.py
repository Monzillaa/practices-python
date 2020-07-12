##no tienen un indice tengo que acceder atravez de su datos

colors = {'Red', 'Green', "Blue"}

#print(type(colors))
print(colors)
##me indica si el elemento esta en la colecion de colors
print('Red' in colors)
#agrega el dato al inicio porque no hay un indice
colors.add('Violet')
print(colors)
#remueve el dato indicado
colors.remove('Red')
print(colors)

#limpia 
colors.clear()
print(colors)

#eliminar el set
del colors
print(colors)

#cuando tienes un conjunto de datos que no deseas iordenar que solo quieres acceder a el!!