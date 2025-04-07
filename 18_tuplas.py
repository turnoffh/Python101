#no se pueden hacer cambios en las tuplas
numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
#se declara con parentesis, no se puede modificar
print(numbers)
print('0 =>', numbers[0])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD
#numbers.append(10) #no se puede
print(numbers)
#numbers[1] = 'change' #no se puede

print(strings.index('zule'))
print(strings.count('nico'))

#podemos convertir una tupla a una lista
my_list = list(strings)
print(type(my_list))
print(type(strings))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(type(my_tuple))
