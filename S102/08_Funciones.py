'''print('Esta es una funcion')

def my_print(text):
    print('This was the text sent')
    print(text)

my_print('Hola Mundo')
'''
#Return
def sum_with_range(min, max):
  print(min,max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_with_range(2,10)
print(result)
result = sum_with_range(1,100)
print(result)
