import numpy as np
from transition import Transition

class DRTA:
	def __init__(self, SIGMA, q0):
		self.Q = [q0]
		self.SIGMA = SIGMA.copy()
		self.DELTA = []
		self.q0 = q0
		self.F = set()


	def addNewTransition(self, q_from, q_to, symbol, timeguard):
		t = Transition(q_from,q_to,symbol,timeguard)
		self.DELTA.append(t)

	def getTransition(self, q_from, symbol):
		for i in range(len(self.DELTA)):
			transition = self.DELTA[i]
			if(transition.q_from == q_from and transition.symbol == symbol):
				return transition
		return None


	def removeTransition(self,transition):
		removeIndex = -1
		for i in range(len(self.DELTA)):
			t = self.DELTA[i]
			if(transition.equal(t)):
				removeIndex = i
		if(removeIndex >= 0):
			print("removing item at index", removeIndex)
			del self.DELTA[removeIndex]
		else:
			print("Transition not found!")


	def __str__(self):
		output = "DELTA: \n" 
		for i in range(len(self.DELTA)):
			output += str(self.DELTA[i]) + " "
		return output

