def find_volume(length =1, width = 1, depth =1):
    return length * width * depth, width, 'Hola' #retorna una tupla con los valores

result = find_volume()
print(result)
print(result[2])
result, width, text = find_volume(10, 20,30) #enviando los valores que esperamos en el orden que los esperamos
print(result)
print(width)
print(text)

result = find_volume(10, 20,30)
print(result)

result = find_volume(width = 10)
print(result)