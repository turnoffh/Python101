def getPopulation():
    keys = ['col', 'bol']
    values = [300, 400]
    return keys, values


def populationByCountry(data, country):
    res = list(filter(lambda item: item['Country'] == country, data))
    
    return res
    
