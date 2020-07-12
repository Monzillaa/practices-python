##ejemplo de clases y objetos de página 78
##ejemplo de instancia pagina 79
""" class Moto:
    pass
 """
class Moto:
    ##se crea una variable justo despues de la deficinicion del la clase y fuera de cualquier metodo, declara la variable n_ruedas
    ##Variables de clase
    ##Las variables de clases o estáticas como dijimos mas arriba son definidas dentro de una clase, mas específicamente luego del encabezado. Pero nunca dentro de un método, porque eso la convertiría en una variable de instancia.
    n_ruedas = 2
    tiene_espejos = True
    def __init__(self, marca, modelo, color):
    #def _init_(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    #si llamamos el nuevo metodo como el atributo de arriba no corre debemos usar otro y sin get o con get funciona
    def get_monse(self):
        """         marca = "Nueva marca"
        print(self.marca) """
        monserrat = ("La marca de la moto es {}, mi modelo es {} y mi color {}") #Mensaje
        print(monserrat.format(self.marca, self.modelo, self.color)) #Usamos FORMAT
    def get_marcaa(self, ):
        marca = 'Nueva marca'
        print(self.marca)
        #instancia recibe un número de parametros
    def acelerar(self, marca, km):
        print(f"La moto {marca}" " acelera a {0}".format(km))


bmw_r1000 = Moto("BMW", "GXS", "blanca")
susuki = Moto("susuki", "wse", "negra")
susuki.get_monse()
bmw_r1000.get_monse()
    
honda_cbr = Moto("Honda", "CBR", "rosa")
honda_cbr.get_marcaa()
honda_cbr.get_monse()
##llamada del nuevo metodo
honda_cbr.acelerar('honda', 20)
##para acceder a la variable solo se coloca la clase y el nombre de la variable!
print(f"Las ruedas son {Moto.n_ruedas}")
print(f"La moto tiene espejos! {Moto.tiene_espejos}")

""" m = Moto(marca,modelo)
print(m.marca) """

""" 
Es otra forma de meter datos para los metodos
bmw_r1000 =  Moto ()
marca = 'BMW'
modelo = 'r100'
color = 'blanca'
susuki_gsx = Moto()
marca = 'Susuki'
modelo = 'GSX'
color = 'negra'
 """

##https://es.stackoverflow.com/questions/132561/diferencia-entre-atributos-de-instancia-y-atributos-de-clase