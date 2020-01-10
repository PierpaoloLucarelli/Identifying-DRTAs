class APTA:
	def __init__(self, Q, SIGMA, q0):
		self.A = DRTA(Q,SIGMA,q0)
		self.R = []

	# S is a set of timed strings
	def learn(self,S):
		



