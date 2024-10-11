# EJERCICIO:
# Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
# implemente una superclase Animal y un par de subclases Perro y Gato,
# junto con una función que sirva para imprimir el sonido que emite cada Animal.
#
# DIFICULTAD EXTRA (opcional):
# Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
# pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# Cada empleado tiene un identificador y un nombre.
# Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
# actividad, y almacenan los empleados a su cargo.

'''
Ejercicio
'''

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print(f'{self.name} dice: guau!')


class Cat(Animal):
    def sound(self):
        print(f'{self.name} dice: miau!')


#SuperClase
def print_sound(animal: Animal):
    animal.sound()


my_animal = Animal('Animal')
my_animal.sound()

my_dog = Dog('Chela')
#my_dog.sound(my_dog.name)
print_sound(my_dog)

my_cat = Cat('Bruce')
#my_cat.sound(my_cat.name)
print_sound(my_cat)

'''
DIFICULTAD EXTRA
'''

class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []
    
    def add(self, employee):
        self.employees.append(employee)
    
    def print_employees(self):
        for employee in self.employees:
            print(employee.name)



class Manager(Employee):
    def coordinate_proyects(self):
        print(f'{self.name} esta coordinado los proyectos de la empresa')



class ProyectManager(Employee):
    def __init__(self, id: int, name: str, proyect: str):
        super().__init__(id, name)
        self.proyect = proyect
        
    def coordinate_proyects(self):
        print(f'{self.name} esta coordinando su protecto')
    



class Programmer(Employee):
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language
    
    def coding(self):
        print(f'{self.name} esta progrmando en {self.language}')
    
    def add(self, employee: Employee):
        print(f'Un programador no puede tener empleados a su cargo, {employee.name} no se añadira')
        

my_manager = Manager(1, 'Calros')
my_proyect_manager1 = ProyectManager(2, 'Roberto', 'Proyecto 1')
my_proyect_manager2 = ProyectManager(3, 'Jose1','Proyecto 2')
my_proyect_manager3 = ProyectManager(4, 'Jose2','Proyecto 3')
my_programmer1 = Programmer(10, 'Rick', 'Python')
my_programmer2 = Programmer(11, 'Rickardo', 'Java')
my_programmer4 = Programmer(13, 'Richard', 'Cobol')

my_manager.add(my_proyect_manager1)
my_manager.add(my_proyect_manager2)
my_manager.add(my_proyect_manager3)

my_proyect_manager1.add(my_programmer4)
my_proyect_manager2.add(my_programmer1)
my_proyect_manager3.add(my_programmer2)

my_programmer4.add(my_programmer1)

my_manager.coordinate_proyects()
my_proyect_manager1.coordinate_proyects()
my_programmer1.coding()


my_manager.print_employees()
my_proyect_manager1.print_employees()
my_programmer4.print_employees()
