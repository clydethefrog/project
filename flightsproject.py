



#https://en.wikipedia.org/wiki/List_of_Air_Canada_destinations

#airlines:
#Air_Canada
#Delta_Airlines
#JetBlue
#Southwest_Airlines
#Spirit_Airlines (not in a table)
#WestJet


import pandas as pd

def function():

    link = 'https://tradingeconomics.com/country-list/tourist-arrivals'

    tourism_data = pd.read_html(link)[0]


    country_name = list(tourism_data['Country'])
    last_tourism_rate = list(tourism_data['Last '])
    previous_tourism_rate = list(tourism_data['Previous '])

    dictionary = {}
    for i,j in enumerate(country_name):
        l_tourism_rate = tuple(['last',last_tourism_rate[i]])
        p_tourism_rate = tuple(['previous',previous_tourism_rate[i]])
        delta = tuple(['change',float('{:.3f}'.format((l_tourism_rate[1] - p_tourism_rate[1]) / p_tourism_rate[1]))])
        dictionary[j] = l_tourism_rate+p_tourism_rate+delta

    return dictionary

