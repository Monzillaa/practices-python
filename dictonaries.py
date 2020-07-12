##cuando se necesita meter elementos con muchos datos como un carrito de compras
##definir objetos de la vida real
product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "firts_name": "ryan",
    "last_name": "ray"
}
##imprime el tipo de dato
#print(type(person))
##imprime los metodos
#print(dir(person))

##de mi variable person quiero obtener las claves
#print(person.keys())
##obtener los items
print(person.items())

##eliminar person
#del person
person.clear()
print(person)

#ejemplo de una lista con diccionarios adentro
products =[
    {"name": "book", "price": 10.99},
    {"name": "laptop", "price": 100000}
] 
print(products)