def incrementar(x):
  return x + 1


incrementar_v2 = lambda x : x + 1 #Funcion lambda, sirve para asignar a una variable que cuando la llame se ejecute

res = incrementar(10)
print (res)

resul = incrementar_v2(20)
print(resul)

full_name = lambda name, last_name: f'Su nombre completo es {name.title()} {last_name.title()}' #Title para que cada letra inciial sea mayuscula

res = full_name('David', 'Morales')
print(res)

res = full_name(input("Digite tu primer nombre: "), input("Digite tu apellido:"))
print(res)
