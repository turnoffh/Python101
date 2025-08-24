#se importa la funcion reduce
import functools #herramientas de python

numbers = [1,2,3,4]

result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)