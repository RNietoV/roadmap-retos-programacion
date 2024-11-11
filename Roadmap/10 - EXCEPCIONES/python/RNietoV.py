# EJERCICIO:
# Explora el concepto de manejo de excepciones según tu lenguaje.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.
#
# DIFICULTAD EXTRA (opcional):
# Crea una función que sea capaz de procesar parámetros, pero que también
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepción creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# - Captura todas las excepciones desde el lugar donde llamas a la función.
# - Imprime el tipo de error.
# - Imprime si no se ha producido ningún error.
# - Imprime que la ejecución ha finalizado. 

'''
Ejercicio
'''

try:
    print(10/1)
    
    my_list = [1,2,3,4]
    print(my_list[4])
    
except Exception as e:
    print(f'Se producido un error: {e}')


print('Hola mundo?')

'''
Extra
'''
class StrTypeError_rnv(Exception):
    pass


def process_params(parameters: list):
    if len(parameters) < 3:
        raise IndexError() 
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[1]) == str:
        raise StrTypeError_rnv('El segundo elemento no puede ser texto ')

    print(parameters[2])
    print(parameters[0] / parameters[1])
    print(parameters[1] + parameters[2])


try:
    process_params([1,2,3])
except IndexError as e:
    print('El numero de elemento de la lista dedar mayor a 2')
except ZeroDivisionError as e:
    print('El segundo elemetno de la list ano puede ser 0')
except Exception as e:
    print(f'Se ha producido un error inesperado: {e}')
except StrTypeError_rnv as e:
    print(f'{e}')
else:
    print('No se ha producido ningun error')
finally:
    print('El programa ha finalizado')

