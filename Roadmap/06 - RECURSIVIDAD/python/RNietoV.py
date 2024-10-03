# EJERCICIO:
# Entiende el concepto de recursividad creando una función recursiva que imprima
# números del 100 al 0.
#
# DIFICULTAD EXTRA (opcional):
# Utiliza el concepto de recursividad para:
# - Calcular el factorial de un número concreto (la función recibe ese número).
# - Calcular el valor de un elemento concreto (según su posición) en la 
#   sucesión de Fibonacci (la función recibe la posición).

'''
Ejercicio - Recursividad
'''

def countdown(num: int):
    if num >= 0:
        print(num)
        countdown(num - 1 )

countdown(100)

'''
Dificultad Extra
'''

def factorial(num: int) -> int:
    if num < 0:
        print('Colocar un numero entero y positivo')
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))

def fibonacci(num: int)-> int:
    if num <= 0:
        print('La posicion tiene que sermayor que cero')
        return 0
    elif num <= 2:
        return num - 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(5))