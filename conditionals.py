""" print("ingresa color")
color = input()

if color == "red" :
    print("the color is red")
elif color == "blue":
    print("the color is blue")
elif color == "yellow":
    print("the color is yellow")
else:
    print("any color bitch!!") """

""" print("ingresa tu nombre")
name = input()
print("ingresa tu apellido")
lastname = input()

if name == "Nini":
    if lastname == "Morales":
        print(f"You are {name} {lastname}")
    elif name == "Mushu" and lastname == "Morales":    
            print(f"You are {name} {lastname}")
    else:
        print(f"You are {name} {lastname}")
else:
    print(f"You are {name} {lastname}") """
##se utiliza para comparaciones and, or  y not son comparadores logicos
x = 30
y = 5
if x > 2 and x <= 10:
    print("x is greater than two and less than or equal to ten")
if x > 2 or x <= 20 :
    print("x is geater than two or less or equal to twenty")
if(not(x == y)):
    print("x is not equal y")