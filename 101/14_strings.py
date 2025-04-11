text = "Ella sabe programar en Python"

'''
print("JavaScript" in text) #Evalua si la cadena esta en la variable ("contains en c#")
print("Python" in text) # true

if 'Python' in text:
  print('Elegiste bien!!') 
else:
  print('Tambien elegiste bien!!')

'''

size = len(text)#longitud de la cadena
print (size)

print(text, text.upper(), text.lower(), text.count('a'))
 #Mayusculas, minusculas, cuenta la cantidad de veces que se repite el caracter
print(text.swapcase())
 #Cambia las mayusculas por minusculas y viceversa
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python', 'Go'))
text_2 = 'este es un titulo'
print(text_2.capitalize()) #solo la primera letra en mayuscula
print(text_2.title())  #todas las palabras con la primera letra en mayuscula
print("398".isdigit()) #potencial numero
