#
# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes
#   posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# - Comprueba si puedes crear funciones dentro de funciones.
# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#
# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#
# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#

'''
Funciones definidas por usuarios
'''

# Simple
def greet():
    print('Hola Python')
greet()

# Con retorno
def return_greet():
    return 'Hola, Phyton!!'

print(return_greet())

# Con parametro
def personal_greet(name):
    print(f'Hola, {name}!!!')

personal_greet('Rick')


# Con parametros
def personal_greet(greet, name):
    print(f'{greet}, {name}!!!!')

personal_greet('Hi','Rick')
personal_greet(name='Rick', greet='Hi')


# con parametros predeterminados
def default_arg_greet(name = 'Sin Nombre'):
    print(f'Hello, {name}!')

default_arg_greet()
default_arg_greet('Rick')


# Con arguentos y retorno
def return_personal_greet(greet, name):
    return f'{greet}, {name}!!!_'

print(return_personal_greet('Hi','Rick'))


# Con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Piton"

saludo, nombre =  multiple_return_greet()
print(saludo)
print(nombre)


# Con nuemro de variodes de parametros

def varible_arg_greet(*names):
    for name in names:
        print(f'Hola, {name}!#')

varible_arg_greet('Phyton', 'JavaScript', 'Ruby', 'C++', 'Cobol', 'Excel')

#C on palaba clave
def varible_key_greet(**names):
    for key, name in names.items():
        print(f'{name} ({key})!???')

varible_key_greet(langue='Phyton',
    name='Ricardo', 
    apodo='Rick', 
    age=31
)

"""
FUNCIONES DENTRO DE FUNCIONES
"""

def outer_function():
    def inner_function():
        print('Funcion interna: Hola.. pitudo')
    inner_function()

outer_function()


"""
FUNCIONES DENTRO DEL LENGUANJE
"""

print(len('fadsfsdasdfasdfsdfgfdhgdh'))
print(type('Rick'))
print(type(1))
print('rick'.upper())


"""
VARIABLE LOCAL Y GLOBAL
"""

global_var = "Python"
print(global_var)

def hello_python():
    local_var = 'Holo'
    print(f'{local_var} {global_var}')

hello_python()
#print(local_var)


"""
DIFICULTAD EXTRA
"""
def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f'{text_1}-{text_2}')
        elif number % 3 == 0: 
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count +=1
    return count

print(print_numbers('fizz','buzz'))