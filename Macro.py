from Tourism import Tourism

class Macro:
    sources = []
    modifiers = []

    def __init__(self, sources, modifiers):
    	self.sources = sources
    	self.modifiers = modifiers

    @staticmethod
    def perform_discount_cash_flow_analysis(airline):
    	# TODO - change this to get airline from ticker
    	tourism_impact = Tourism.tourism_projection(airline)
    	# Algorithm here
    	return 0


 