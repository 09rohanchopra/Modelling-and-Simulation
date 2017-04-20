import time
import xlsxwriter
import random


class RandNum:
	a = 16807
	c = 0
	m = 2147483647
	t1 = 0
	t2 = 0	

	def __init__(self):
		self.seed = int(round(time.time() * 1000))
		self.t1 = int(round(time.time() * 1000))
		self.t2 = int(round(time.time() * 1000))
	

	def setSeed(self, seed):
		self.seed = seed

	def linCong(self):
		rand = ((self.a*(self.seed) +self.c) )
		self.seed = rand
		rand = rand% self.m
		return float(rand/self.m)

	
	def setComSeed(self,s1,s2):
		self.t1 = s1
		self.t2 = s2

	def comcong(self):
		
		a1 = 40014
		a2 = 40692
		m1 = 2147483563
		m2 = 2147483399

		m = 2147483562

		x1 = (a1*self.t1)%m1
		x2 = (a2*self.t2)%m2

		self.t1 = x1
		self.t2 = x2

		x = (x1-x2)%m
		if(x==0):
			r = (m/m1)
		else:
			r = x/m1
		return r
	def storeRand(self,num):
		random.seed(self.t1)
		uniques = []
		workbook = xlsxwriter.Workbook('RandNum.xlsx')
		worksheet = workbook.add_worksheet()
		row = 0
		col = 0		    

		# Write a total using a formula.
		worksheet.write(row, col, 'User Generated Random Numbers')
		worksheet.write(row, col+1, 'In built function Random Numbers')
		row+=1


		for i in range(1,num):
			r = self.comcong()
			if r in uniques:
				print("Iteration: %d"%(i))
			uniques.append(r)
			worksheet.write(row, col,     r)
			r = random.random()
			worksheet.write(row, col+1,     r)
			row += 1
		workbook.close()