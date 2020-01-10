class Transition:
	def __init__(self, q_from, q_to, symbol, timeguard):
		self.q_form = q_from
		self.q_to = q_to
		self.symbol = symbol
		self.timeguard = timeguard
