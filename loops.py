""" foods = ['apples','breads', 'cheese', 'milk', 'bananas', 'grapes']

for food in foods:
    if food == "cheese":
        #print("you have to buy this")
        #break #para el proceso al encontrar cheese
        continue #realiza la validacion y como si cumple al llegar a cheese continua leyendo el arreglo saltando este
    print(food) """

""" ##rango imprime del 1 al siete
for number in range (1,8):
    print(number) """

""" ##podemos recorrer un arreglo e imprimir por caracter
for letter in "Hello":
    print(letter) """

""" ##se incrementa la variable para que pueda salir del bucle(loops), si no se incrementa se volveria un bucle infinito
count =  4
while count <= 10:
    print(count)
    count = count + 1 """

""" ##ejemplo del libro python 3 pagina 53 se cambio la posicion de los signos por error en el libro
lista = ["uno", "dos", "tres"]
cad = ""
for ele in lista :
     cad += ele
   ## cad = cad + ele puede funcionar tambien con esta linea de codigo en lugar de la de arriba
print(lista) """

""" ##ejemplo de pagina del libro 53
for item in (1, 2, 3):
    print(item)
else:
    print("fin") """

""" # ##ejemplo del libro de pytho 54 pag
x = 0
y = 6
while x < y:
    print(x)
    x += 1  """

""" ##ejemplo del libro pag 54
x = 0
y = 3
while x < y:
    print(x)
    x+=1
    if x == 2 :
        break
else:
    print("x es igual a 2") """

""" for i in range(1, 10) :
    if i % 2 != 0 :
        continue
    print(i) """
