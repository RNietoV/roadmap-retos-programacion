# EJERCICIO:
# Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
# en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
# - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que analice dos palabras diferentes y realice comprobaciones
# para descubrir si son:
# - Palíndromos
# - Anagramas
# - Isogramas


'''
OPERACIONES
'''

s1 = 'Hello'
s2 = 'Pyhton'
# Concatenacion

print(s1 + ', ' + s2 + '!')

# repeticeion
print( (s1 + '_') * 5)

# indexacion
print( s1[0] + s1[1] + s1[2] + s1[3] + s1[4])

# logitud
print(len(s2))

# Porcion
print(s2[2:5])
print(s2[2:])
print(s2[0:2])
print(s2[:2])
print(f'invertirlo: {s2[::-1]}')

# Busqueda
print('P' in s2)
print('Py' in s2)
print('Py' in s1)

# Remplazo
print(s1.replace('o','u'))

# division
s3 = 'pythonthon rick'
print(s3.split('t'))

# Mayusculaas y minisculas
print(s1. upper())
print(s2.lower())
print(s3.title())
print(s3.capitalize())

# Eliminacion de espacios
s4 = ' VelRick '
print(s4.strip() + '@gmail.com')

# busqueda al principio y al final
print(s1.startswith('He'))
print(s1.startswith('Py'))
print(s1.endswith('lo'))
print(s1.endswith('on'))

# Busqueda de posicion
s5 = 'VELRIC Rick @rick_koi'
print(s5.find('rick'))
print(s5.find('Rick'))
print(s5.find('R'))

# Busqueda de ocurrencias
print(s5.lower().count('r'))

# Formateo
print('Saludo: {}, Lenjuaje: {} !'.format(s1,s2))

# Interpolacion
print(f'Saludo: {s1}, Lenjuaje: {s2} !')

# transformacion en lista de caracteres
print(list(s3))

l1 =[s1, ', ', s2, '!']
print('-'.join(l1))

# Tranformaciones numericos
s6 = '45646874864'
print(int(s6))

#  Comprovaciones varias
print(s1.isalnum()) #es alfa numerico - letras y numeros
print(s1.isalpha()) #es alfa - letras
print(s6.isalpha()) #es alfa - letras
print(s6.isnumeric()) #es numeric

'''
Dificultat Extra
'''


def check(word1: str, word2: str):
    
    # Palindromos: es una palabra, frase, número o cualquier otra secuencia de caracteres 
    # que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando los 
    # espacios, signos de puntuación y acentos.
    print('-------------------')
    print('Palindromo')
    print('-------------------')
    print(f'¿{word1} es un palindromo?: {word1 == word1[::-1]}')
    print(f'¿{word2} es un palindromo?: {word2 == word2[::-1]}')
    
    # Anagrama: es una palabra o frase formada al reordenar las letras de otra palabra o frase, 
    # utilizando todas las letras exactamente una vez. Es decir, se trata de una reorganización 
    # de las letras para formar una nueva palabra o expresión.
    
    print('-------------------')
    print('Anagrama')
    print('-------------------')
    print(f'¿{word2} es un anagrada de {word2}?: {sorted(word1) == sorted(word2)}')
    # Isograma: es una palabra o frase en la que no se repite ninguna letra. 
    # En otras palabras, cada letra aparece una sola vez.
    
    print('-------------------')
    print('Isograma')
    print('-------------------')
    #print(f'¿{word1} es un isograma?: {len(word1) == len(set(word1))}')
    #print(f'¿{word2} es un isograma?: {len(word2) == len(set(word2))}')
    
    def isogram( word: str) -> bool:
        word_dict = dict()
        for char in word:
            word_dict[char] = word_dict.get(char, 0) + 1
        
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    
    print(f'¿{word1} es un isograma?: {isogram(word1)}')
    print(f'¿{word2} es un isograma?: {isogram(word2)}')
    

check('radar', 'pythonpythonpythonpython')
#check('amor', 'roma')
