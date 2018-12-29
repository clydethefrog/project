
import pandas as pd

#airlines = ['Air_Canada', 'Delta_Air_Lines', 'JetBlue']


class MacroDataSource:

    def get_destinations_with_ticker(self, airline):

        link = 'https://en.wikipedia.org/wiki/List_of_{}_destinations'.format(airline)

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




#if __name__ == '__main__':
#    obj = MacroDataSource()
#    airlines = ['Air_Canada', 'Delta_Air_Lines', 'JetBlue']
#    airline = airlines[0]
#    obj.get_destinations_with_ticker(airline)

