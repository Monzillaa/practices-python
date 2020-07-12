""" def hello(name="Person"):
    print("hello "+ name)

hello("bitch")
hello("Nano")
hello("Nini")
hello() """
""" 
##jemplo de funcion suma
def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10,30))
print(add(600,10)) """

""" 
##Se puede hacer todo sobre una misma linea de codigo
add = lambda numberOne, numberTwo: numberOne + numberTwo
print(add(10, 30)) """

##ejemplos del ibro
""" def test():
    print("test ejecutada")
test()
nueva = test
nueva() """

""" def test2(a,b):
    a = 2
    b = 3

c = 5
d = 6
test2(c,d)
print("c={0}, d={1}".format(c, d)) """

##me da resultado none en lugar de la lista invs como se imprime lista
""" def variable(lista):
     lista [0] = 3

lista = [1,2,3]
print(variable(lista)) """

""" a = 3
b = a
b = 2
print ("a={0}, b={1}".format(a,b)) """

""" a = [0, 1]
b = a
b[0] = 1
print(a)
print("a={0}; b={1}".format(a,b)) """

""" def fun(a,b=1):
    print(b)
fun(4) """
""" 
##se cambio el valor de c por el numero seis para saber en que momento se esta imprimiendo por obviedad el valor de c
def fun (a, b, c = 6):
    print("a={0}, b={1}, c={2}".format(a, b, c))
fun(1, 2, 4)
print("tres datos con variables")
fun(a=1, b=2, c=4)
print("dos datos con variables")
fun(a=1, b=2)
print("dos datos sin variables")
fun(1,2) """

""" def fun(*items):
    for item in items:
        print(item)

fun(1, 2, 3)
fun(5,6)

t = ('a', 'b', 'c')
fun(t) """

""" def fun(**params):
    print(params)

fun(x=5, y=8)
{'x' :5, 'y':8}
fun(x=5, y=8, z=4)
{'x':5, 'y':8, 'z':4} """

""" def print_record(nombre, apellido, **rec):
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    for k in rec:
        print("{0}: {1}".format(k, rec[k]))

print_record("juan","coll", edad=43, localidad="madrid")

print_record("Monse", "Tip", edad="20") """

""" ##En lugar de llamar tres parametros colocamos *
def fun(x, y, z):
    print(x, y, z)
t = (1, 2, 3)
fun(*t) """

""" ##En lugar de mandar a llamar una tupla se coloca **
def fun(x, y, z):
    print(x, y, z)
d = {'y':1, 'z':2, 'x':0}
fun(**d) """

""" ##combina el paso de parametros con el operador **
def fun(a=1, b=2, c=3):
    print(a, b, c)

d = {'a':3,'b':4}
fun(**d) """

""" ##Funcion lambda
li = [lambda x: x + 2, lambda x: x + 3]
param = 4
for accion in li:
    print(accion(param))

lam = lambda x: x*5
print(lam(3))

def lam(x):
    return x*5
print(lam(3))

li = [1,2,3]
new_li = map(lambda x: x+2, li)
for item in new_li: print(item) """

""" ##ejemplo del libro pagina 65tipos mutables con argumentos por defecto
def fun(x=1, li=None):
    if li is None:
        li = []
    li.append(x)
    print(li)

fun()
fun()
fun(2)
li = [3, 4]
fun(6, li) """

