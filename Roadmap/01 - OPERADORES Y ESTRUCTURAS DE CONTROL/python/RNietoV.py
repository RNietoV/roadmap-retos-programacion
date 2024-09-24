#
# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.
#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#

'''
     OPERADORES EN PYTHON
'''

# Artimeticos
print(f'Operador suma 10 + 3 = {10+3}')
print(f'Operador resta 10 - 3 = {10-3}')
print(f'Operador multiplicacion 10 * 3 = {10*3}')
print(f'Operador division 10 / 3 = {10/3}')
print(f'Operador modulo 10 % 3 = {10%3}')
print(f'Operador exponente 10 ** 3 = {10**3}')
print(f'Operador division entera 10 // 3 = {10//3}')


# Comparacion
print(f'Igualdad 10 == 3 es {10 == 3}')
print(f'Desigualdad 10 != 3 es {10 != 3}')
print(f'Mayor que 10 > 3 es {10 > 3}')
print(f'Menor que 10 < 3 es {10 < 3}')
print(f'Mayor o igual que 10 >= 3 es {10 >= 3}')
print(f'Menor o igual que 10 <= 3 es {10 <= 3}')

# Logicos
print(f'AND &&: 10 + 3 == 13 and 5 - 1 == 4 todo esto es {10 + 3 == 13 and 5 - 1 == 4}')
print(f'or ||: 10 + 3 == 13 or 5 - 1 == 200 todo esto es {10 + 3 == 10 or 5 - 1 == 4}')
print(f'NOT !: not 10 + 3 == 14 not  esto es {not 10 + 3 == 14}')

# Asignacion

my_number = 11
print(my_number)
my_number += 1
print(my_number)
my_number -= 1
print(my_number)
my_number *= 2
print(my_number)
my_number /= 2
print(my_number)
my_number %= 2
print(my_number)
my_number **= 1
print(my_number)
my_number //= 1
print(my_number)




# Identidad
# comparar el valor en la posicion de la memoria

my_new_number = 1.0
print(f'my_number is my_new_number {my_number is my_new_number}')
my_new_number = my_number
print(f'my_number is my_new_number {my_number is my_new_number}')
print(f'my_number is NOT my_new_number {my_number is not my_new_number}')




# Pertenencia
print(f" 'c' in 'Rick' = {'c' in 'Rick'}")
print(f" 't in 'Rick' = {'t' not in 'Rick'}")



# de bit
a = 10 # 1010
b = 3  # 0011

print(f" AND: 10 & 3 = {10&3}") #0010 = 2
print(f" OR: 10 | 3 = {10|3}")  #1011 = 11
print(f" XOR: 10  3 = {10^3}")  #1001 = 9
print(f" NOT: 10  = {~10}")     #0101 = -11
print(f'Desplazamiento a la derecha: 10 >> 2 = {10>>2}')   #0001
print(f'Desplazamiento a la izquierda: 10 << 2 = {10<<2}')   #101000



"""
          ESTRUCTURAS DE CONTROL

"""

# Condicionales
my_string = 'Rick'

if my_string == 'RNietoV4':
     print('=')
elif my_string == 'Rick':
     print('Aqui dice Rick')
else:
     print('!=')


# Iterativas

for i in range(11):
     print(i)

i = 0

while i <= 10:
     print(i)
     i += 1

# excepciones

try:
     print(10/0)
except:
     print('se ha producido un error')
finally:
     print('Ha finalizado el manejo de excepciones')



# EJERCICIO

for number in range(10, 56):
     if number % 2 == 0 and number != 16 and number % 3 != 0 :
          print(number)