class Transition:
	def __init__(self, q_from, q_to, symbol, timeguard):
		self.q_from = q_from
		self.q_to = q_to
		self.symbol = symbol
		self.timeguard = timeguard


	def equal(self, other):
		if(self.q_from != other.q_from):
			return False
		if(self.q_to != other.q_to):
			return False
		if(self.symbol != other.symbol):
			return False
		if(self.timeguard[0] != other.timeguard[0]):
			return False
		if(self.timeguard[1] != other.timeguard[1]):
			return False
		return True


	def __str__(self):
		output = "from: " + str(self.q_from) + ", to: " + str(self.q_to) + ", symbol: " + str(self.symbol) + ", timeguard: (" + str(self.timeguard[0]) + ", " + str(self.timeguard[1]) + ")\n"
		return output


