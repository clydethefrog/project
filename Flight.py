import pandas as pd

class Flight:

    @staticmethod
    def format_airline_name(name):
        return name.replace(' ', '_')

    @staticmethod
    def destinations_for_airline(airline):
        formatted_airline_name = Flight.format_airline_name(airline.airline)
        link = 'https://en.wikipedia.org/wiki/List_of_{}_destinations'.format(formatted_airline_name)

        wiki_data = pd.read_html(link)

        destinations = wiki_data[1]

        country = destinations[0][2:]
        city = destinations[1][2:]
        airport = destinations[2][2:]

        dictionary = dict()
        for i, j in enumerate(list(country)):
            temp_dict = dict()
            relevant_city = list(city)[i]
            relevant_airport = tuple([list(airport)[i]])
            temp_dict[relevant_city] = relevant_airport

            if j not in dictionary:
                dictionary[j] = tuple([temp_dict])
            else:
                dictionary[j] += tuple([temp_dict])

        return dictionary

    @staticmethod
    def routes(airline):
        print("")

    