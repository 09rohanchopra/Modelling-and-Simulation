from randomnum import RandNum
import xlsxwriter
import numpy as np


ur = RandNum()


def poisson(alpha = 3.64):
	
	workbook = xlsxwriter.Workbook('poisson-rvar.xlsx')
	worksheet = workbook.add_worksheet()
	row = 0
	col = 0	


	worksheet.write(row, col, 'Random num')
	worksheet.write(row, col+1, 'P')
	worksheet.write(row, col+2, 'Poisson')

	a = list(range(10000))
	d = list(range(10000))
	n=0
	p=1
	count = 0
	flag = 0
	for i in range(10000):
		if flag==1:
			n = 0
			p = 1

		r = ur.comcong()
		p = r*p
		if p<np.exp(-alpha) :
			a[i] = r
			d[i] = p
			row+=1
			worksheet.write(row, col, str(r))
			worksheet.write(row, col+1, str(p))
			worksheet.write(row, col+2, str(n))
			flag = 1
			count+=1
		else:
			n+=1
			flag = 0
		if count == 1001:
			break

