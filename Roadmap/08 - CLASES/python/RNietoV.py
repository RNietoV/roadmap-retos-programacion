# EJERCICIO:
# Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
# atributos y una función que los imprima (teniendo en cuenta las posibilidades
# de tu lenguaje).
# Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
# utilizando su función.
#
# DIFICULTAD EXTRA (opcional):
# Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
# en el ejercicio número 7 de la ruta de estudio)
# - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#   retornar el número de elementos e imprimir todo su contenido.


'''
Ejercicio
'''

class Programmer:
    lastname: str = None
    
    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages
    
    def print(self):
        print(f'Nombre: {self.name} \nApellido: {self.lastname} \nEdad: {self.age} \nLenguajes: {self.languages} \n ')
        


my_programer = Programmer('Rick', 31, ['SQL','Python','Visual Basic', 'Javascript'])

my_programer.print()
my_programer.lastname = 'velnie' 
my_programer.print()

my_programer.age = 27
my_programer.print()


'''
DIFICULTAD EXTRA
'''
# LIFO
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push(1)
my_stack.push('b')
my_stack.push(3)
my_stack.push(False)
print('------------------------')
print(my_stack.count())
print('------------------------')

my_stack.print()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()

print('------------------------')
print(my_stack.count())
print('------------------------')

print()



# FIFO

class Queue:
    def __init__(self):
        self.queue = []
    
    def equeue(self, item):
        self.queue.append(item)
    
    def deequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)
    
    def count(self):
        return len(self.queue)

    def print(self):
        for item in reversed(self.queue):
            print(item)

print('------------------------')
print('---------Colas----------')
print('------------------------')
my_queue = Queue()
my_queue.equeue(1)
my_queue.equeue('b')
my_queue.equeue(3)
my_queue.equeue(False)
print('------------------------')
print(my_queue.count())
print('------------------------')

my_queue.print()
my_queue.deequeue()
my_queue.deequeue()
my_queue.deequeue()
my_queue.deequeue()
my_queue.deequeue()

print('------------------------')
print(my_queue.count())
print('------------------------')