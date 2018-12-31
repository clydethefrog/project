




import urllib.request
import pandas

class CompanyDetails:


    def scraper(self, airline):
        name = airline.lower().title().split(' ')
# makes all letters lowercase, then makes first letter of each word uppercase then makes list using split
        symbol = '%20'
        linkTail = ''.join([j+symbol for i,j in enumerate(name)])[:-3]# air canada >>becomes>> Air%20Canada
        url = 'https://www.airfleets.net/ageflotte/' + linkTail + '.htm'

        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,}
        response = urllib.request.urlopen(urllib.request.Request(url,None,headers))
        return pandas.read_html(response.read())


    def search_total_no_aircraft(self, airline):
        #returns the total number of aircraft in the fleet
        fleet = self.scraper(airline)[15]
        return {'Total':list(fleet[list(fleet.columns)[1]])[-1]}

    def search_avg_age_aircraft(self, airline):
        #returns the average age of ENTIRE FLEET (in aggregate) {fleet average age: x years}
        fleet = self.scraper(airline)[15]
        return {'Average age':list(fleet[list(fleet.columns)[2]])[-1]}

    def search_type_aircraft(self, airline):
        #returns a count of each type of aircraft
        fleet = self.scraper(airline)[15]
        return {j:list(fleet[1])[1:][i] for i,j in enumerate(list(fleet[0])[1:])}

    def search_avg_age_per_type_aircraft(self, airline):
        #returns the average age of each aircraft TYPE {aircraft type 1: avg age, airtype type 2: avg age}
        fleet = self.scraper(airline)[15]
        return {j:list(fleet[2])[1:][i] for i,j in enumerate(list(fleet[0])[1:])}

    def search_supply_chain_proportions(self, airline):
        #this counts the amount of 'boeing' and 'airbus' and 'other' made planes returns dict:
        #{boeing:0.4, airbus:0.4, other:0.2}
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

    def search_company_details(self, airline):
        # this creates a tuple of the infomration [(x,y),(z,p)] then makes it into a dictionary {x:y, z:p}
        details = self.scraper(airline)
        company_details = details[9]
        return {i[0]:i[1] for i in list(zip(list(company_details[company_details.columns[0]])[:-2],                             list(company_details[company_details.columns[1]])[:-2]))}











if __name__ == '__main__':
    obj = CompanyDetails()

    obj.search_supply_chain_proportions('air canada') #british airways, united airlines etc...








































#this function will be used to associate company names with their respective ticker
    #using a spreadsheet I downloaded which contains all of them

##########################################################################################
###################################### [in progress...] ##################################
##########################################################################################
##########################################################################################
    #this DOES NOT work properly yet, need a better way cause a lot of these comapnies
    #have similar names
    def search_ticker(self, company_name):
        data = pandas.read_csv('companies_tickers.csv')
        tickers_list = list(data['Ticker'])
        names_list = list(data['Name'])

        dataset = list(zip(tickers_list, names_list))
        dictionary = {}
        for i,j in enumerate(dataset):
            dictionary[j[1]] = j[0]

        temp_dict = {}
        for i in dictionary:
            if '{}'.format(company_name) in str(i).lower():
                temp_dict[i] = dictionary[i]

        final_dict = dict()
        possible_choices = list(temp_dict.items())
        possible_choices.sort(key=lambda x: len(x[0]), reverse=True)

        for i in possible_choices:
            final_dict.update({i[0]: i[1]})

        name = list(final_dict.keys())[-1]

        return name



#next: business and credit cycle stuff













#http://investdb.theglobeandmail.com/invest/investSQL/gx.company_search?pi_mode=INVEST&pi_pname=&pi_call_from=&pi_comp_name=microsoft&pi_search_type=CONTAINS&pi_symbol_type=ALL&pi_exchange=All&iaction=Look+it+up%21





#now that that is done, just go ahead and expand this to other airlines of interest
















