#
# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#
# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.
#


'''
ESTRUTURAS DE DATOS
'''
# Listas

my_list = ['Rick', 'Koi', 'Vicios','Ale']
print(my_list)

#Insercion
my_list.append('velric')
print(my_list)

# Eliminar
my_list.remove('Vicios')
print(my_list)

# Acceso
print(my_list[1])
my_list[1] = 'Rick_Koi' #Modificacion
print(my_list)

my_list.sort() #Ordenacion
print(my_list)
print(type(my_list))
print('---')


my_tuple =('Ricardo', 'Nieto', 'Rick_koi', '31')
print(type(my_tuple))
print(my_tuple)
print(my_tuple[2]) #acceso

my_tuple = sorted(my_tuple)
print(type(my_tuple))
my_tuple = tuple(sorted(my_tuple))
print(type(my_tuple))
print(my_tuple)

my_set = {'Ricardo', 'Nieto', 'Rick_koi', '31'}
print(type(my_set))
print(my_set)
my_set.add('VELRIC')
my_set.add('VELRIC')

my_set.remove('31')
print(my_set)

my_set = sorted(my_set)
print(type(my_set))
print(my_set)

# Dicionario
my_dict = {'name':'Ricardo', 
        'last_name':'Nieto', 
        'ig':'Rick_koi', 
        'age':'31'}

print(type(my_dict))

print(my_dict['name'])
my_dict['email'] = 'rick_koi@outlook.com'
print(my_dict)

my_dict['age'] = '30'
print(my_dict)

del my_dict['last_name']
print(my_dict)

my_dict = sorted(my_dict.items())
my_dict = dict(my_dict)
print(type(my_dict))
print(my_dict)


'''
Dificultar extra
'''
def my_agenda():
    agenda = {}
    
    def inser_contact(name):
        phone = input('Introduce el telefono del contacto: ')
        if phone.isdigit() and len(phone) == 10:
            if name in agenda:
                print(f'Se a modificado el contacto de {name}')
                agenda[name] =  phone
            else:
                print(f'Se a creado el contacto de {name}')
                agenda[name] =  phone
            
        else:
            print('El telefo ingresado no es valido.\n')
    
    while True:
        print('------------------------')
        print('Bienvenidio a mai ayenda')
        print('------------------------')
        print('1. Buscar contacto. ')
        print('2. Insertar contacto. ')
        print('3. Actualizar contacto. ')
        print('4. Eliminar contacto. ')
        print('5. Salir')
        
        option = input('\n Seleciona una opcion: ')
        match option:
            case '1':
                name = input('Ingresa el nombre del contacto a buscar: ')
                if name in agenda:
                    print(f'El telefono de {name} es {agenda[name]}.\n')
                else:
                    print(f'El contacto {name} no existe.\n')
                pass
        
            case '2':
                name = input('Introduce el Nombre del contacto: ')
                inser_contact(name)
                pass
        
            case '3':
                name = input('Ingresa el nombre del contacto a actualizar: ')
                if name in agenda:
                    inser_contact(name)
                else:
                    print(f'El contacto {name} no existe.\n')
                
                pass
        
            case '4':
                name = input('Ingresa el nombre del contacto a eliminar: ')
                if name in agenda:
                    print(f'El contacto {name} se ha elimando.\n')
                    del agenda[name]
                else:
                    print(f'El contacto {name} no existe.\n')
                pass
        
            case '5':
                print('Saliendo de la mai ayenda...\n')
                break
        
            case _:
                print('Opcion no valida del 1 al 5\n')

my_agenda()