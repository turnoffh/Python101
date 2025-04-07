#comparador de flotantes
x = 3.3
print(x)
y = 1.1 + 2.2
print(y) #precision diferente
print(x == y) #false por la precision
#comparador de flotantes con strings
y_str = format(y, ".2g")#se convierte a string y se le da formato de 2 digitos
print('str =>', y_str)
print(y_str == str(x))

#forma matematica
print('*' * 10)
print(y, x)
tolerance = 0.00001
print(abs(x - y) < tolerance)#abs valor absoluto para comparar matematicamente
