#Local scope
#Enclosing scope
#Global scope
#Built-in scope

#Local scope
price = 100 #Global
#print(price) #solo funciona cuando la ponemos aqui

def increment():
  price = 200 #Local
  result = price +10 #local
  print(result)
  return result

print(price)
price_2= increment()
print(price_2)
