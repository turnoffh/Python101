import sys #modulo de sistema
#print(sys.path)

import re #Expresiones regulares
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es el 13'

result = re.findall('[0-9]+', text) #Strings de solo numeros
print(result)

import time
timestamp = time.time() #tiempo en segundos desde 1970  
local = time.localtime() #tiempo local
res = time.asctime(local)
print(timestamp)
print(local)
print(res)

import collections #usada para manejar listas
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)