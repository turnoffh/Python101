import mod

data = [
  {
    'Country': 'Colombia',
    'Population': 300
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def run():
  key, values = mod.getPopulation()
  print(key, values)
  print(key)
  print(values)

  cnt = input('Type a country => ')
  res = mod.populationByCountry(data, cnt)
  print(res)

if __name__ == '__main__':
  run()
  