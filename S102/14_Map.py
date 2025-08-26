#Funcion mas usada que vamos a conocer
numbers = [1, 2, 3, 4] #lista de numeros
numbers_v2 = []
for i in numbers: #iteramos numbers
  numbers_v2.append(i * 2) #multiplicamos cada elemento de la lista por 2
print(numbers) #Sin transformar
print(numbers_v2) #Transformada

numbers_v3 = list(map(lambda i: i * 2, numbers)) #map nos permite transformar cada uno de los elementos de la lista, es una higher order function, recibe una funcion como parametro(lambda) y una lista(numbers)

print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

#vamos a transformar estas con diferentes dimensiones
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))

print(result) #ignora los elementos que sobran

