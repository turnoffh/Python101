try:
  print(0/0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')

except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)
#else: # se ejecuta si no hay error despues de ejecutar lo del try
#finally: # se ejecuta siempre al final haya o no errores

  
try:
  print(0/0)
except Exception as error:
  print(error)
  
print('Hola')