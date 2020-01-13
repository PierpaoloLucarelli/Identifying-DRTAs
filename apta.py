from drta import DRTA

class APTA:
	def __init__(self, SIGMA, q0, verbose=False):
		self.A = DRTA(SIGMA,q0)
		self.R = set()
		self.verbose = verbose

	# S is a set of timed strings
	def learn(self,S,t_min,t_max):
		if(self.verbose):
			print("learning")
		# iterate over each timed string (first positive, then negative)
		for type_ in S:
			timedStrings = S[type_]
			for ts in timedStrings:
				if(self.verbose):
					print("working with: ")
					print(ts)
				q = self.A.q0

				# iterate each tuple of timedString
				for t in ts:
					if(self.verbose):
						print("current String:")
						print(t)
					#check if transition existst
					transition = self.A.getTransition(q,t[0])
					q_to = None
					if(transition!=None):
						if(self.verbose):
							print("it exitsts")
						q_to = transition.q_to
					else:
						if(self.verbose):
							print("add a new transition to new state")
						q_to = len(self.A.Q)
						self.A.Q.append(q_to)
						self.A.addNewTransition(q, q_to, t[0], (t_min, t_max))
					if(self.verbose):
						print("New current state:", q_to)
					q = q_to
				if(type_ == "accepted"):
					self.A.F.add(q)
				else:
					self.R.add(q)


	def split(self, transition, t, S):
		print("Removing transition:", transition)
		self.A.removeTransition(transition)


	def __str__(self):
		return str(self.A)





		



