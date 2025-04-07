# CRUD Create, Read, Update & Delete
numbers = [1, 2, 3, 4, 5] #create
print(numbers[1]) #read

numbers[-1] = 10 #update
print(numbers)

numbers.append(700)#agregar al final
print(numbers)

numbers.insert(0, 'hola')#agregar en la posicion 0
print(numbers)

numbers.insert(3, 'change')#crear y correr
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks #fusionarlas
print(new_list)

index = new_list.index('todo 2')#posicion del elemento
new_list[index] = 'todo changed'
print(new_list)

#delete
new_list.remove("todo 1")
print(new_list)

new_list.pop()#eliminar el ultimo elemento
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)