set_countries = {'col', 'mex', 'bol'}

size = len(set_countries) #tamaño del conjunto
print(size)

print('col' in set_countries)#buscar booleano
print('pe' in set_countries)

set_countries.add('pe') #agregar
print(set_countries)

set_countries.update({'ar', 'ecua', 'pe'}) #actualizar conjunto agregando varios elementos
print(set_countries)

set_countries.remove('col')
print(set_countries)
set_countries.remove('ar')
print(set_countries)
#set_countries.remove('arg')#error

set_countries.discard('arg')#no falla si no existe
set_countries.add('arg')
print(set_countries)
set_countries.clear()#limpiar el conjunto
print(set_countries)