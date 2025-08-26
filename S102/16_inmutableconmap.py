items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300,
  },
  {
    'product': 'pantalones 2',
    'price': 200,
  }
]
'''
#Vamos a transformar el precio de cada uno de los productos
prices = list(map(lambda item: item['price'], items)) #obtenemos el precio de cada uno de los items. item['price'] es la clave del diccionario que queremos obtener, items es el diccionario que queremos transformar
print(prices)
#Ahora vamos a agregar un nuevo atributo a cada uno de los productos, impuestos
'''

def add_taxes(item):
  new_item = item.copy() #copiamos el diccionario para no modificar el original
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))
print('new list')
print(new_items)
print('old list')
print(items)
#print(new_items)
