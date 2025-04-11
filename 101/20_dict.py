person = {
  'name': 'Nicolas',
  'last_name': 'Molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

person['name'] = 'David'
person['age'] -= 67

print(person)

person['langs'].append('C#')
print(person)

del person['last_name'] #eliminar una llave
person.pop('age') #eliminar una llave, en diccionarios toca pasar la llave, no como en listas
print(person)
print('items')
print(person.items())
print('keys')
print(person.keys())
print('values')
print(person.values())
