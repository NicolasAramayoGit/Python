# Este es el juego de adivinar el número.
import random

intentosRealizados = 0

print(" ¡Hola! ¿Cómo te llamas?")
miNombre = input()

numero = random.randint(1, 20)

print("Bueno, " + miNombre + ". estoy pensando en un número entre 1 y 20.")

while intentosRealizados < 6:
    print("Intenta adivinar.") #Hay cuatro espacios delante de print.
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print("Tu estimación es muy baja.") #Hay ocho espacios delante de print

    if estimacion > numero:
        print("Tu estimación es muy alta.")

    if estimacion == numero:
        break

if estimacion == numero:    
    intentosRealizados = str(intentosRealizados)
    print("¡Buen trabajo, " + miNombre + ". ¡Has adivinado mi número en " + intentosRealizados + " intentos!")

if estimacion != numero:
    numero = str(numero)
    print("¡Pues no. El numero que esta pensando era " + numero)
