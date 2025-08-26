import random

countries = ['col', 'mex', 'bol', 'pe']

dict_v4 = {country: random.randint(1, 100) for country in countries}
print(dict_v4)

population_v2 = {country: population for (country, population) in dict_v4.items() if population > 50}
print(population_v2)

text = 'Hola, soy Nicolas'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)  
uniquev2 = {c: text.count(c) for c in text if c in 'aeiou'}
print(uniquev2)