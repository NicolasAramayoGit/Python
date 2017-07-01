# Encuentra el bug
import random

numero1 = random.randint(1, 10)
numero2 = random.randint(1, 10)

print("¿Cuánto es " + str(numero1) + " + " + str(numero2) + "?")
respuesta = input() 

if int(respuesta) == numero1 + numero2: #variable respuesta casteo a int
    print("¡Correcto!")
else:
    print("¡Nops! La respuesta es " + str(numero1 + numero2))
    
