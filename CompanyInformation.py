import urllib.request
import pandas

class CompanyDetails:

    # makes all letters lowercase, then makes first letter of each word uppercase then makes list using split
    def scraper(self, airline):
        name = airline.lower().title().split(' ')
        
        symbol = '%20'
        linkTail = ''.join([j+symbol for i,j in enumerate(name)])[:-3]# air canada >>becomes>> Air%20Canada
        url = 'https://www.airfleets.net/ageflotte/' + linkTail + '.htm'

        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,}
        response = urllib.request.urlopen(urllib.request.Request(url,None,headers))
        return pandas.read_html(response.read())

        #Function to search the amount of aircraft in a fleet
        #Input: Airline name: Example: Air Canada
        #return: {Total => number}
    def search_total_no_aircraft(self, airline):
        fleet = self.scraper(airline)[15]
        return {'Total':list(fleet[list(fleet.columns)[1]])[-1]}

        #function to search for the average age of the entire fleet in question
        #Input: Airline name: Example: Air Canada
        #Return: {Average age => number}
    def search_avg_age_aircraft(self, airline):
        fleet = self.scraper(airline)[15]
        return {'Average age':list(fleet[list(fleet.columns)[2]])[-1]}

        #function that returns the count of each TYPE of aircraft
        #Input: Airline name: Example: Air Canada
        #Return: {plane type 1 => 5, plane type 2 => 10}
    def search_type_aircraft(self, airline):
        fleet = self.scraper(airline)[15]
        return {j:list(fleet[1])[1:][i] for i,j in enumerate(list(fleet[0])[1:])}

        #function to return the average age per TYPE of aircraft
        #Input: Airline name: Example: Air Canada
        #Return: {aircraft type 1 => avg age, airtype type 2 => avg age}
    def search_avg_age_per_type_aircraft(self, airline):
        fleet = self.scraper(airline)[15]
        return {j:list(fleet[2])[1:][i] for i,j in enumerate(list(fleet[0])[1:])}

        #function to determine the supply chain proportions
        #this counts the amount of 'boeing' and 'airbus' and 'other' made planes returns dict:
        #Input: Airline name: Example: Air Canada
        #Returns: {boeing:0.4, airbus:0.4, other:0.2}
    def search_supply_chain_proportions(self, airline):

        fleet = self.scraper(airline)[15]
        boeing_counter = 0
        airbus_counter = 0
        for i,j in enumerate(fleet[list(fleet.index)[0]][1:][:-1]):
            if 'boeing' in j.lower():
                boeing_counter+=1
            elif 'airbus' in j.lower():
                airbus_counter+=1
        return {'Boeing':boeing_counter / len(fleet[list(fleet.index)[0]][1:]), 'Airbus':
                 airbus_counter / len(fleet[list(fleet.index)[0]][1:]), 'Other':(len(fleet[list
                (fleet.index)[0]][1:]) - airbus_counter-boeing_counter) / len(fleet[list(fleet.index)[0]][1:])}

        #function to determine details of the company: name, hq, callsign, sqauck value
        #Input: Airline name: Example: Air Canada
        #Returns: {detail1 => x, detail2 => y, detail3 => z}
    def search_company_details(self, airline):
        # this creates a tuple of the infomration [(x,y),(z,p)] then makes it into a dictionary {x:y, z:p}
        details = self.scraper(airline)
        company_details = details[9]
        return {i[0]:i[1] for i in list(zip(list(company_details[company_details.columns[0]])[:-2],                             list(company_details[company_details.columns[1]])[:-2]))}
