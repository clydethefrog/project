"""
Class

Micro
----------
The class to represent Micro Economics on an airline
	property: airline - the airline that the calculations will be perforned on
"""

class Micro:

	def __init__(self, airline):
		self.airline = airline

	# Mehtod that perfroms the Discount Cash Flow Analysis
	# params: None
	# return None

	def discount_cash_flow(self):
		projection_step(airline)

	# Mehtod that perfroms the projection step as the first operation on the discount_cash_flow_analysis
	# params: The airline to perfrom the anslysis on
	# return Int

	def projection_step(self, airline):
		income_statement = IncomeStatement(airline.income_statement_model, "cleaned_income_statement_data_set")
		balance_sheet = BalanceSheet(airline.balance_sheet_model, "cleaned_balance_sheet_data")

		#TODO - change this to the actual algorithm
		projection_step_algorithm(income_statement,balance_sheet)

		return 0