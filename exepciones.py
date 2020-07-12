##Se debe colocar el codigo dentro del try para que cuando suceda un error mande la exepción
##ejemplo uno
try:
    li = [0, 1]
    print(li[2])
except IndexError:
    print("Error: Índice no válido maldita esperanzitaXD")
##ejemplo dos
a = 3
b = 2
c = a + b
try:
    """ li = [0, 3]
    li[1] """
    b/0
except:
    print("error: indice no valido x2")
else:
    print("sin error")
finally:
    print("bloque Dos ejecutado")

##ejemplo tres
try:
    raise TypeError
except:
    print("error de tipo")

class ValorIncorrecto(Exception):
    def __init__(self, val):
        print(("{0} no permitido").format(val))

val = 8
if val > 5 and val < 9:
    print("valor es ",val)
    raise ValorIncorrecto(val)

##ejemplo 4 
try:
    print(li[2])
except IndexError('list assignment index out of range'):
    import sys
    sys.exc.info()[2]

try:
    print(li[2])
except IndexError:
    import sys
    sys.exc.info()[2]