# EJERCICIO:
# - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#   su tipo de dato.
# - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
# (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#
# DIFICULTAD EXTRA (opcional):
# Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#   Comprueba también que se ha conservado el valor original en las primeras.

'''
VALOR Y REFERENCIA
'''

# Tipos de datos por valor

my_int_a = 10
my_int_b = my_int_a
#my_int_b = 20
#my_int_a = 30

print(my_int_a)
print(my_int_b)

# Tipos de datos por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)

print(my_list_a)
print(my_list_b)


# Funciones de datos por valor
my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)



# Funciones con datos de refeencia
def my_list_func(my_list: list):
    my_list_e = my_list
    my_list_e.append(30)
    
    my_list_d = my_list_e
    my_list_d.append(40)
    
    print(my_list_e)
    print(my_list_d)

my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

'''
Dificultad extra
'''
# Por valor
my_int_d = 10
my_int_e = 20

def value(value_a : int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    
    return value_a, value_b


my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f'{my_int_d}, { my_int_e}')
print(f'{my_int_f}, {my_int_g}')

print()
print()

#por referencia

def ref(list_a : list, list_b: list) -> tuple:
    temp = list_a
    list_a = list_b
    list_b = temp
    list_a.append(60)
    list_b.append(50)
    
    return list_a, list_b

my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = ref(my_list_e, my_list_f)

print(f'{my_list_e}, {my_list_f}')
print(f'{my_list_g}, {my_list_h}')
