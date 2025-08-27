with open('./text.txt', 'w+') as file: #r+ lect y esct(agregando nuevas lineas), si se agrega w+ se sobreescribe
  for line in file:
    print(line)
  file.write('Nuevas cosas en el archivo\n')
  file.write('Me llamo\n')
  file.write('David\n')
  file.write('Morales\n')
