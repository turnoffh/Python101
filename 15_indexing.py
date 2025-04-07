text = "Ella sabe Python"
print(text[0])
print(text[1])
#print(text[999]) #Error
size = len(text)

print(text[size - 1])
print(text[-1])#funciona igual que el anterior (nos muestra la ultima letra )

# slicing
print(text[0:5]) #muestra desde la posicion 0 hasta la 5
print(text[10:16])
print(text[16:9:-1])#al reves
print(text[:10])#muestra desde el inicio hasta la posicion 10
print(text[5:-1])#muestra desde la posicion 5 hasta la ultima


