for i in range(1, 11):
    print(i)

my_iter = iter(range(1, 2)) #Iterador
print(my_iter)
print(next(my_iter))#podemos generar manualmente las iteraciones
print(next(my_iter))#es importante para leer las lineas de un archivo
print(next(my_iter))#saca error por que ya no hay mas elementos