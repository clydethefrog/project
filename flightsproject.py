



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

    airlines = ['Air_Canada','Delta_Air_Lines','JetBlue']

    link = 'https://en.wikipedia.org/wiki/List_of_{}_destinations'.format(airlines[0])

    wiki_data = pd.read_html(link)

    destinations = wiki_data[1]

    country = destinations[0][2:]
    city = destinations[1][2:]
    airport = destinations[2][2:]


    dictionary = dict()
    for i,j in enumerate(list(country)):
        temp_dict = dict()
        relevant_city = list(city)[i]
        relevant_airport = tuple([list(airport)[i]])
        temp_dict[relevant_city] = relevant_airport

        if j not in dictionary.keys():
            dictionary[j] = tuple([temp_dict])
        else:
            dictionary[j] += tuple([temp_dict])


    return dictionary
