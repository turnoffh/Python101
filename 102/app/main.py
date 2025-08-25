import mod

key, values = mod.getPopulation()
print(key, values)
print(key)
print(values)



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

cnt = input('Type a country => ')
res = mod.populationByCountry(data, cnt)
print(res)