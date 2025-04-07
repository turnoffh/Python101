my_dict = {} #()-> tuplas []-> listas {}-> diccionarios
print(type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age': 29
}
print(my_dict)
print(len(my_dict))
print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('aged'))#retorna none si no encuentra la llave, es mejor usar get para evitar errores

print('avion' in my_dict)
print('otroqueno' in my_dict)