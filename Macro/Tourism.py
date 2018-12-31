from Flight import Flight

class Tourism:

	@staticmethod
	def tourism_projection(airline):
		destinations = Flight.destinations_for_airline(airline)
		routes = Flight.routes(airline)
