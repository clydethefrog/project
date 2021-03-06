

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re

class FirmSpecificAnalysis_Naive:

#everything we initialize are going to be 'assumptions' that are made in the modelling process
# or should we not do it that way?
    def __init__(self):
        self.periods_forecasted = ['t+1','t+2','t+3','t+4']
        self.revenue_growth_assumption = 0.05
        self.cogs_to_revenue_assumption = 0.35


#function to load the income statement or balance sheet depending on which you call in flag
#later, since B only shows up in balance sheet and not in: income statement, any flag with b in it
#will point to balanace sheet
#it will then return the dataframe that the scraper function returns having scraped the link passed in
#input: what is required by program, income or balance sheet, but our algo will use both anyway...
#Returns: dataframe of the income statement or balance sheet (described in detail below)
    def load_current_data(self, flag):
        if 'b' in flag.lower():
            return self.scraper('https://ca.investing.com/equities/air-canada-balance-sheet')
        else:
            return self.scraper('https://ca.investing.com/equities/air-canada-income-statement')



    #this function parses the url below, creates a dictionary of
    #{account1: [100,421,51234,12341],account2:[4121,5322,35123,51234]} (using dict comprehension)
    #then creates and returns a dataframe using that dictionary (using the for loop at the end)
    #Input:
    #Returns: an income statement OR balance sheet that looks exactly like it would on excel
    def scraper(self, url):
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)                 Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
        data = bs(requests.get(url,headers=header).text,'lxml').find('div',{'id':'rrtable'})


        dictionary = {' '.join(re.sub(r"([A-Z])", r" \1", i.split('\n')[0]).split()):i.split('\n')[1:] if i.split('\n')[-1] != '' else i.split('\n')[1:-1] for i in ''.join(data.text.split('\n\n')[3].split(' ')).split('\n\n')}

        df = pd.DataFrame(index = list(dictionary.keys()), columns = data.text.split('\n\n')[1].split('\n')[-4:])

        for account in list(df.index):
            for index,col in enumerate(list(df.columns)): df[col][account] = dictionary[account][index]

        return df


#Function to create a dataframe for our projections. It does this for 4 time periods
    #(the amount used in a standard dcf)
    #Input: dataframe (df) which is retrieved through the load_current_IS function
    #Returns:Dataframe with all accounts of the DF which was loaded from input above
    #Each account is a row and has 4 zeros initially:
    #           t+1   t+2   t+3    t+4
    # account1  0       0     0     0
    # account2  0       0     0     0 etc...
    def create_projections_dataframe(self,og_df):
        return pd.DataFrame(index = og_df.index, columns = self.periods_forecasted).fillna(0)


#function which puts everything together, and adds a previous column
    #to the data since this is the NAIVE version of what we are doing
    #so we just keep the most recent values associated to each account is
    #the previous file
    #Input: dataframe with nothing in it
    #Returns Dataframe of all 0's for all columns EXCEPT the previous
    #column which has all of the most recent data
    #            prev  t+1   t+2   t+3    t+4
    # account1    432   0       0     0     0
    # account2    6969  0       0     0     0 etc...
    def fill_previous_IS(self, dataframe):
        new_df = self.create_projections_dataframe(dataframe)
        new_df['prev'] = pd.DataFrame(dataframe[list(dataframe.keys())[0]])
        cols = new_df.columns.tolist()
        cols.insert(0, cols.pop(cols.index('prev')))
        return new_df.reindex(columns=cols)


#function to make a simple forecase based on any account and dataframe input
#it searches for the 'previous' and makes a simple TVM calculation using the assumption input above
#Input: dataframe (WHICH MUST CONTAIN PREVIOUS), and the title of the account of interest, ex: Revenue
#returns: Dataframe with the forecast applied to the column you indicate
    def simple_forecast(self, dataframe, account, assumption): #pass in self.w/e in __init__ as assumption
        for i,j in enumerate(self.periods_forecasted):
            dataframe[j][account] = int(dataframe['prev'][account])*(1+assumption)**(i+1)
        return dataframe


#this function makes a forecast which is based on the naive assumption that your cogs and other
#accounts are just a fixed percentage of another account, so it requires an assumption,
#a target to be a fixed percentage over, and the name of the account which it corresponds
#Input: i.e. fixed percentage of which account? (target) & which (account) is equaled to the fixed percentage? and finally a dataframe (which should have been run through simple forecast cause its
#needed to do these sorts of forecasts
    def proportion_forecast(self, target, account, dataframe, assumption):
        relevant_data = list(dataframe.T[target])[1:]
        results = [assumption*i for i in relevant_data]
        for i, j in enumerate(self.periods_forecasted):
            dataframe[j][account] = results[i] * (1 + assumption) ** (i + 1)
        return dataframe









#now we do the exact same thing as above buuuuuut for the BS instead!










#HOW TO USE:
#input either income statemnt or balance sheet
#pick if you want simple forecast: (just apply growth rate over time)
#or proportion forecast: (you are just a porpotion of another forecast) for example:
#cost of goods sold is typeically 35% of revenue, so the projections for COGS would be
#that 0.35 assumption * revenue projection for each projection period

if __name__ == '__main__':
    obj = FirmSpecificAnalysis_Naive()
    og_df = obj.load_current_data('Income Statement') #loads the income statement OR balance sheet
    df = obj.fill_previous_IS(og_df) #fills the 'previous' column
    df_Simple_forecast = obj.simple_forecast(df, 'Total Revenue', obj.revenue_growth_assumption) #makes simple
    #assumption in this case on the 'total revenue' row
    df_proportion_forecast = obj.proportion_forecast('Total Revenue', 'Costof Revenue, Total',df, obj.cogs_to_revenue_assumption)


    print(df_Simple_forecast)
    print(df_proportion_forecast)

