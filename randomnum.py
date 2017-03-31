import time

class RandNum:
	def __init__(self):
		self.seed = int(round(time.time() * 1000))
	a = 16807
	c = 0
	m = 2147483647
		

	def setSeed(self, seed):
		self.seed = seed

	def linCong(self):
		rand = ((self.a*(self.seed) +self.c) % self.m)
		return float(rand/self.m)

	def randint(self,s,e):
		while(True):
			r = self.linCong()
			r = r*self.m
			if(r>s and r<e):
				return r