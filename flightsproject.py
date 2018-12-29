



#works for any link in trading economics under 'indicators'

#returns dictionary of dictionary
#{'country':{'last':123, 'previous':123, 'change':0}}

import pandas as pd

def function(link):

    data = pd.read_html(link)[0]

    country_name = list(data['Country'])
    last_rate = list(data['Last '])
    previous_rate = list(data['Previous '])

    return {j: {'last': last_rate[i], 'previous': previous_rate[i],'change': float('{:.3f}'.format((last_rate[i] - previous_rate[i]) / previous_rate[i]))} for i, j in enumerate(country_name)}





#choose any link from this page >>> https://tradingeconomics.com/indicators
# pass that link in below as a string for example:
#link = 'https://tradingeconomics.com/country-list/tourist-arrivals'



link = 'https://tradingeconomics.com/country-list/tourist-arrivals'
function(link)

