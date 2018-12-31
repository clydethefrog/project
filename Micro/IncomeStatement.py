class IncomeStatement:

	"""
    Class
    ----------
    Income statement manager for the data and the IncomeStatementType properties
    """

	def __init__(self, company_income_statement, income_statement_data_set):
		self.company_income_statement = company_income_statement
		self.income_statement_data_set = income_statement_data_set

	## TODO - PARTIAL IMPLEMENTATION
	# Searches the keys we know for each compnay and return the data at that index or None
		# param: income_statement_parameter some other key in the data
		# returns: Data for the key or none
	def get_data_from_income_statement(self, income_statement_parameter):
		income_statement_data = self.income_statement_data_set # TODO- Parse to a data frame
		company_income_statement.name
		company_income_statement.column_keys #TODO - Use the column we know about to index the statement

