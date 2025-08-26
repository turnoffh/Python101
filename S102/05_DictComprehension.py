#Generamos el diccionario con un ciclo for
import random

dict = {}
for i in range(1, 5):
    dict[i] = i * 2

print(dict)

dict_v2 = {i: i * 2 for i in range(1, 5)}
print(dict_v2)

countries = ['col', 'mex', 'bol', 'pe']
dict_v3 = {i: i.upper() for i in countries}
print(dict_v3)

countries = ['col', 'mex', 'bol', 'pe']
dict_v3 = {index + 1: country.upper() for index, country in enumerate(countries)}
print(dict_v3)

dict_v4 = {country: random.randint(1, 100) for country in countries}
print(dict_v4)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
print(list(zip(names, ages)))
dict_v5 = {name: age for (name, age) in zip(names, ages)} #ZIP: Une una lista con otra y las convierte en una tupla
print(dict_v5)