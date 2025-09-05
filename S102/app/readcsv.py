import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader) #Con esto traemos el nombre de cada columna
    data = []
    for row in reader:
      iterable = zip(header, row) #unimos el header con la fila que estamos iterando
      country_dict = {key: value for key, value in iterable} #Dictionary comprehension
      data.append(country_dict)
    return data
      

if __name__ == '__main__':
  data = read_csv('data.csv')
#  print(data[0])
  pais = input('Type Country => ')
  result = list(filter(lambda item: item['Country/Territory'] == pais, data))
  print(result)
  print(result[0]['World Population Percentage'])
  