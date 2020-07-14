myStr = "Monzillaa"
print('My name is' + myStr)
#se coloca f para que tome como variable declarada con anterioridad lo que esta en llaves
print(f"My name is {myStr}")#esta opcion solo esta disponible de python 3.3
#se utiliza format, en las llaves e coloca el valor donde se colocara el valor de la variable
print("My name is {0}".format(myStr))

#palabra clave que nos enseña que podemos hacer con cierto tipo de dato
#print (dir(myStr))

""" print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize()) """
#metodos encadenados
""" print(myStr.replace('Hello', 'bye').upper ())
print(myStr.count('l')) """

#python responde con boleanos, el metodo startwith evalua caracter por caracter
""" print(myStr.startswith('Hello'))
print(myStr.endswith('World'))
 """
#este metodo divide el string a travez de los espacios o el dato que se le indique en parentesis
""" print(myStr.split('o')) """
#este ,etodo indica el indice del caracter es decir la posision donde esta guardada
""" print(myStr.find('z')) """
#funcion para saber el tamaño del metodo
""" print(len(myStr)) 
print(myStr.index('e'))"""
#saber si el string es numerico
""" print(myStr.isnumeric())
print(myStr.isalpha()) """
#traer la posision
""" print(myStr[4])
print(myStr[-5]) """