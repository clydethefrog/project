"""
Class

IncomeStatement
----------
The class to represent an airlines Income Statement
	property: balance_sheet_statement_mode - the model representing the balance sheet
	property: balance_sheet_data_set - the parsed data from the document
"""

class BalanceSheet:

	def __init__(self, balance_sheet_statement_mode, balance_sheet_data_set):
		self.balance_sheet_statement_mode = balance_sheet_statement_mode
		self.balance_sheet_data_set = balance_sheet_data_set


	## TODO - PARTIAL IMPLEMENTATION
	# Searches the keys we know for each compnay and return the data at that index or None
		# param: income_statement_parameter some other key in the data
		# returns: Data for the key or none
	def get_data_from_balance_sheet(self, balance_sheet_parameter):
		income_statement_data = self.balance_sheet_data_set # TODO- Parse to a data frame
		company_income_statement.name
		company_income_statement.column_keys #TODO - Use the column we know about to index the statement
		return None

