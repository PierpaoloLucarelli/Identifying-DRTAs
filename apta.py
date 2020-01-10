from drta import DRTA

class APTA:
	def __init__(self, SIGMA, q0):
		self.A = DRTA(SIGMA,q0)
		self.R = []

	# S is a set of timed strings
	def learn(self,S,t_min,t_max):
		print("learning")
		# iterate over each timed string (first positive, then negative)
		for type_ in S:
			timedStrings = S[type_]
			for ts in timedStrings:
				print("working with: ")
				print(ts)
				q = self.A.q0

				# iterate each tuple of timedString

				for t in ts:
					print("current String:")
					print(t)
					#check if transition existst
					transition = self.A.getTransition(q,t[0])
					q_to = None
					if(transition!=None):
						print("it exitsts")
						q_to = transition.q_to
					else:
						print("add a new transition to new state")
						q_to = len(self.A.Q)
						self.A.Q.append(q_to)
						self.A.addNewTransition(q, q_to, t[0], (t_min, t_max))
					print("New current state:", q_to)
					q = q_to
		print(self.A)





		



