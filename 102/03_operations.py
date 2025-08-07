set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b) #unir conjuntos
print(set_c)
print(set_a | set_b) #otra forma de unir conjuntos, solo hay diferencia en la sintaxis

set_c = set_a.intersection(set_b) #interseccion de conjuntos solo los elementos que se repiten en ambos conjuntos
print(set_c)
print(set_a & set_b) #otra forma de interseccion de conjuntos, solo hay diferencia en la sintaxis

set_c = set_a.difference(set_b) #diferencia de conjuntos, quitar elementos de un conjunto que esten en otro
print(set_c)
print(set_a - set_b) #otra forma de diferencia de conjuntos, solo hay diferencia en la sintaxis remover del primero los del segundo

#diferencia simetrica
set_c = set_a.symmetric_difference(set_b) #diferencia simetrica, quitar elementos de un conjunto que esten en otro y viceversa
print(set_c)
print(set_a ^ set_b) #otra forma de diferencia simetrica, solo hay diferencia en la sintaxis, elementos que son unicos al unir los dos conjuntos

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set = countries.union(northAm).union(centralAm).union(southAm)
print(new_set)