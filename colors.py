from colorama import init, Fore

# Para iniciar colorama
init()

print("Texto color original")

print(Fore.YELLOW + "Texto color amarillo")
print(Fore.GREEN + "Texto color verde")
print(Fore.RED + "Texto color rojo\n")

##Si después de imprimir texto con color quieres imprimir texto sin color, habrá un comportamiento no esperado, pues se imprimirá con el último color utilizado.
##Para reiniciar los colores puedes imprimir Style.RESET_ALL. No olvides importar a Style:
from colorama import init, Fore, Style

# Para iniciar colorama
init()

print("Texto color original")

print(Fore.YELLOW + "Texto color amarillo")
print(Fore.GREEN + "Texto color verde")
print(Fore.RED + "Texto color rojo")
print(Style.RESET_ALL, end="")
print("Texto color original de nuevo\n")

##Igualmente si quieres puedes indicarle a colorama que se reinicie automáticamente. De este modo te evitas resetear manualmente. Solo pasa el argumento de autoreset en True al invocar a init.
#from colorama import init, Fore

# Para iniciar colorama
init(autoreset=True)

print("Texto color original")

print(Fore.YELLOW + "Texto color amarillo")
print(Fore.GREEN + "Texto color verde")
print(Fore.RED + "Texto color rojo")
print("Texto color original de nuevo\n")

# Vamos a ver cómo imprimir una palabra pero con un color distinto para cada letra.

from colorama import init, Fore

# Para iniciar colorama
init(autoreset=True)

print(Fore.YELLOW + "P" + Fore.GREEN + "a" + Fore.BLUE + "r" + Fore.RED + "z" + Fore.CYAN + "i" + Fore.MAGENTA + "b" + Fore.WHITE + "y" + Fore.YELLOW + "t" + Fore.RED + "e")

# Otra forma:
print(Fore.YELLOW + "P", end="")
print(Fore.GREEN + "a", end="")
print(Fore.BLUE + "r", end="")
print(Fore.RED + "z", end="")
print(Fore.CYAN + "i", end="")
print(Fore.MAGENTA + "b", end="")
print(Fore.WHITE + "y", end="")
print(Fore.YELLOW + "t", end="")
print(Fore.RED + "e")