import mod
import readcsv
import charts

def run():
  data = readcsv.read_csv('./data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''cnt = input('Escriba un pais=> ')
  res = mod.populationByCountry(data, cnt)

  if len(res) > 0:
    country = res[0]
    keys, values = mod.getPopulation(country)
    print(keys, values)
    charts.generate_bar_chart(keys, values)
    charts.generate_pie_chart(keys, values)
    print(country)
    print(res)
    print(keys)
    print(values)
    
  
  
  key, values = mod.getPopulation()
  print(key, values)
  print(key)
  print(values)

  print(res)

  '''
if __name__ == '__main__':
  run()
  