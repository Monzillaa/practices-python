""" ##primera forma de importar librerias
import datetime
##imprime la fecha actual
print(datetime.date.today())
##imprime los minutos a horas
print(datetime.timedelta(minutes=70)) """

""" ##segunda forma importo especificando desde que biblioteca
from datetime import timedelta

print(timedelta(minutes=100)) """
""" 
##importa la fecha
from datetime import timedelta, date
print(date.today()) """

""" ##importando modulo propia primera forma
import fmath

fmath.add(1,2)
fmath.substract(1,2) """

""" 
##segunda forma de importar modulo
from fmath import add, substract

substract(1,2)
add(1,2) """

""" from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "hello")
print("hello bitch") """

##ejemplo del libro de la pagina 66
""" import modulesbook
modulesbook.say_hello() """
#especificas la funcion que quieres utilizar con from 
""" from modulesbook import say_hello
say_hello()
""" 
""" import imp
imp.reload(module)
#no se como funciona duda de como correrlo """

#si quieres mandar a llamar mas de una funcion pero no todas puedes mandarlas allamar separadas por comas

from modulesbook import say_hello, say_bye
say_hello()
say_bye()

