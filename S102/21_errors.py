#print(0 / 0)) # SyntaxError
#print(0 / 0) # ZeroDivisionError
#print(result) # NameError

suma = lambda x,y : x + y
assert suma(2, 2) == 4 # No pasa nada pq funciona bien
# assert suma(2, 2) == 5 # AssertionError

age = 10 
if age < 18:
  raise Exception('No se permite menores de edad')
  