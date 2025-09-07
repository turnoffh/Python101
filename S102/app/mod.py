def getPopulation(countryData):
    popDict = {
        '2022': int(countryData['2022 Population']),
        '2020': int(countryData['2020 Population']),
        '2015': int(countryData['2015 Population']),
        '2010': int(countryData['2010 Population']),
        '2000': int(countryData['2000 Population']),
        '1990': int(countryData['1990 Population']),
        '1980': int(countryData['1980 Population']),
        '1970': int(countryData['1970 Population'])
    }
    labels = popDict.keys()
    values = popDict.values()
    return labels, values
    
def populationByCountry(data, country):
    res = list(filter(lambda item: item['Country/Territory'] == country, data))
    
    return res
    
def getWorldPopulationPercentage(data):
    worldPopulationPercentage = list(map(lambda item: item['World Population Percentage'], data))
    labels = list(map(lambda item: item['Country/Territory'], data))
    return labels, worldPopulationPercentage