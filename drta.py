import numpy as np

class DRTA:
	def __init__(self, Q, SIGMA, q0):
		self.Q = np.arange(len(Q))
		self.SIGMA = np.arange(len(SIGMA))
		self.DELTA = []
		self.q0 = q0
		self.F = []

