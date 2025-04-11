#conjuntos no tienen orden y no permiten duplicados, se pueden modificar
set_countries = {'col', 'mex', 'bol'} #se parece a los diccionarios pero no tienen llave, muestra solo los valores no repetidos
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0} #lo ordena automaticamente cuando es numeros,
#permite agregar cualquier tipo de dato
print(set_numbers)

set_from_string = set('hola') #separa cada letra y la muestra sin repetir
print(set_from_string)

set_from_tuples = set(('abc', 'def', 'ghi', 'abc')) #muestra solo los valores sin repetir
print(set_from_tuples)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7]
set_numbers = set(numbers)
print(set_numbers)
unique_numebers = list(set_numbers)
print(unique_numebers)