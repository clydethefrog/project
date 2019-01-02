#credit cycle: if someone borrows a bunch today, that means today they can spend a lot more
#but in the future they will have to pay it back with interest and will be forced to spend less
#this is why its a cycle
#anytime any ONE person borrows, you are creating a cycle!
#only once you pay it back does that cycle stop
#so youre looking for a moment where everyone in aggregate borrows more

#i have 100k I can borrow 10k, I spend 110k. Person who receives that now
#has 110k income and can broorw 121k and spends that, and so on and so forth
#thats how the cycle grows

#eventually, short term debt cycle:
#expansion: Spending increeases and prices rise this happens becuase the increase in spending
#is fueled by credit, WHEN THE AMOUNT OF SPENDING AND INCOMES GROW FASTER THAN THE PRODUCTION OF GOODS
#PRICES RISE CAUSING INFLATION, THIS CAUSES MONETARY POLICY WITH HIGHER INTEREST RATES
#fewer people can afford to borrow money and the cost of existing debt rises (like credit interest payment goes
#up)
#becuaseepople borrow less and higher debt repayments, their spending slows, and as we saw at the beginning
#since someones spending is another persons income, their income drops and they spend less causing the
#downward cycle
#when people spend less prices drop so deflation happens
#interest rates are then lowered and back up we go
#https://www.youtube.com/watch?v=PHe0bXAIuk0 13:04

import pandas

class CompanyDetails:

    def search_ticker(self, company_name):
        data = pandas.read_csv('companies_tickers.csv')
        tickers_list = list(data['Ticker'])
        names_list = list(data['Name'])

        dataset = list(zip(tickers_list, names_list))
        dictionary = {j[1]:j[0] for i,j in enumerate(dataset)}
        temp_dict = {i:dictionary[i] for i in dictionary if '{}'.format(company_name) in str(i).lower()}

#.SW, .TO, (either .MU or .BE or TI depending on which one is real for air france)



        print(temp_dict)
        exit(0)




if __name__ == '__main__':
    obj = CompanyDetails()

    print(obj.search_ticker('wal mart'))












'''credit and business cycle
season cycle so find one online maybe for best times to fly... i.e. most profitable
for companies to be flying not for passengers. Guess those are inveserly related?'''
#start by initializing a single array of from 1,365 to represent each day
#then make 3 comolumns, each one of these will have a number ranging from -10 to 10 depending on where it is in the cycle. Lowest point of trough i s-10 highest point of peak is 10 and everything esle ranges between them depedning on where it is on the up and downward portion of the cycle.


