numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)  
#podemos guardar diferentes tipos de datos en una lista
types = [1, True, 'hola']
print(types)  

print(numbers[0])
print(tasks[0])
text = 'Hola'
#text[0] = 'W' #Error

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[1] = 'do the dishes'
print(tasks)

#hacer slicings
print(numbers[:3])
print(True in types) #buscar en listas
print("hola" in types) #buscar en listas
