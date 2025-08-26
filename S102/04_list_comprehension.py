numbers = []
for element in range(1, 11):
    numbers.append(element * 2)
print(numbers)

#list comprehension: forma mas corta de escribir guardar una lista con un ciclo for en la misma linea
numbers_v2 = [element for element in range(1, 11)] #el range puede ser una lista tupla etc, cualquier iterable, sintaxis mas corta y facil de leer
print(numbers_v2)

number_v3 = [element * 2 for element in range(1, 11)]
print(number_v3)

#con condicionales
numbers_v4 = [i*2 for i in range(1, 101) if i % 2 == 0]
#pasos: elemento a iterar como lo quiero agregar, iteracion, condicional
print(numbers_v4)