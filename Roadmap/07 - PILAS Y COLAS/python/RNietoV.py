#
# EJERCICIO:
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).
#
# DIFICULTAD EXTRA (opcional):
# - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#   el nombre de una nueva web.
# - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#   interpretan como nombres de documentos.
#/

'''
Ejercicio
'''
# Pila / Stack (LIFO)

stack = []

# push
stack.append('1')
stack.append('2')
stack.append('3')


print(stack)

#pop

stack_item = stack[len(stack) - 1]
print(stack_item)
del stack[len(stack) - 1]
print(stack)

print(stack.pop())
print(stack)


# Cola / queue (FIFO)
queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)


# dequeue
print(queue.pop(0))
print(queue)

queue_item = queue[0]
print(queue_item)
del queue[0]
print(queue)


'''
Extra
'''

# web
def web_navigation():
    stack = []
    
    while True:
        
        action = input('Añade una url o navega con las palabras adelente/atras: \n')
        if action == 'salir':
            print('Saliendo del navegador web...')
            break
        elif action == 'adelante':
            pass
        elif action == 'atras':
            if len(stack) > 0 :
                stack.pop()
        else:
            stack.append(action)
        
        if len(stack) > 0 :
            print(f'https://{stack[len(stack) -1]}')
        else:
            print('Inicio: \n')

#web_navigation()

def share_printed():
    
    queue = []
    
    while True:
        print('-----------------------')
        print('Bienvedo a la impresora 3000')
        print('Que desea realiar: ')
        print(' 1: Imprimir documento.')
        print(' 2: Agregar documento.')
        print(' 3: Mostrar documentos pendientes a imprimir.')
        print(' 4: Imprimir todo.')
        print(' 5: Salir.')
        print('-----------------------')
        
        
        action = input('Ingrese la accion a realizar:  \n')
        
        if action == '5':
            print('Saliendo de impresora 3000...')
            break
        elif action == '1':
            if len(queue) > 0:
                print(f'Imprimeindo: {queue.pop(0)}')
            else:
                print('Sin documentos por imprimir...')
        elif action == '2':
            action = input('Agrege el documento a encolar: \n')
            queue.append(action)
        elif action == '3':
            if len(queue) > 0:
                print(f'Cola de impresion: {queue}')
            else:
                print('Sin documentos por imprimir...')
        elif action == '4':
            if len(queue) > 0:
                for i in queue[:]:
                    print(f'Imprimiendo: {queue.pop(0)}')
            else:
                print('Sin documentos por imprimir...')
        else:
            print('INGRESA UNA OPCION VALIDA....')

share_printed()