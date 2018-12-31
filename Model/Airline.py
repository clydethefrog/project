"""
Class

Airline
----------
The class to represent each airline
	property: ticker - the stock ticker name
	property: airline - the actual name of the airline
	
	property: income_statement_model - the model for the income statement   see: AirlineIncomeStatement
	property: balance_sheet_model - the model for the income statement   see: BalanceSheet
"""

class Airline:

    def __init__(self, ticker, airline, income_statement_model, balance_sheet_model):
    	self.ticker = ticker
    	self.airline = airline
    	self.income_statement_model = income_statement_model
    	self.balance_sheet_model = balance_sheet_model



