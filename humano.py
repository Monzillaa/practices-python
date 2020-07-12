##Link donde se saco el ejemplo d humanos https://pythones.net/clases-y-metodos-python-oop/ 
## ejemplo de metodos con galletas https://docs.hektorprofe.net/python/programacion-orientada-a-objetos/atributos-y-metodos/
## ejemplo de personas https://programacion.net/articulo/como_funcionan_las_clases_y_objetos_en_python_1505
##orientada a objetos https://runestone.academy/runestone/static/pythoned/Introduction/ProgramacionOrientadaAObjetosEnPythonDefinicionDeClases.html
##ejemplos mas complejos https://docs.python.org/es/3.8/tutorial/classes.html
##modulos y clase ejemplo visual https://medium.com/datos-y-ciencia/c%C3%B3mo-crear-m%C3%B3dulos-y-clases-con-python-f8b487bf2908

##este ejemplo aun no esta completo
""" class Humano():
    pass

class Humano():
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
Persona1 = Humano(31,"Pedro") """
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Humano(): #Creamos la clase Humano
    def __init__(self, edad, nombre, ocupacion): #Definimos el parametro edad , nombre y ocupacion
        self.edad = edad # Definimos que el atributo edad, sera la edad asignada
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asig
        self.ocupacion = ocupacion #DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACION
        
        #Creación de un nuevo método
    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}") #Mensaje
        print(presentacion.format(self.nombre, self.edad, self.ocupacion)) #Usamos FORMAT

Persona1 = Humano(31, "Pedro", "Desocupado") #Instancia

#Llamamos al método

Persona1.presentar() 
