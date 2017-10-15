import numpy as np
import time
import csv
import random
from randomnum import RandNum

ur = RandNum()

inputfile = open('data/input.csv','r')
reader = csv.DictReader(inputfile, delimiter=',')
outputfile = open('data/output.csv','w')
spamwriter = csv.writer(outputfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

spamwriter.writerow(['S.No.'] + ['Customers'] + ['Iterations'] + ['AAWT'])
count = 0
for line in reader:
	customers = int(line['customers'])
	iterations = int(line['iterations'])
	
	average_awt=0
	for k in range(iterations):         #_______ run the loop for specified seconds ____#
				 						#_______ count the iterations done in that time _____#
		inter_arrival_time=[]
		service_time=[]
		#_____ to generate the random numbers_________#
		for i in range(customers):

			#r = random.random()

			#user defined random number
			r = ur.comcong()

			if r >= 0 and r < 0.125:
				inter_arrival_time.append(1)
			elif r >= 0.125 and r < 0.25:
				inter_arrival_time.append(2)
			elif r >= 0.25 and r < 0.375:
				inter_arrival_time.append(3)
			elif r >= 0.375 and r < 0.5:
				inter_arrival_time.append(4)
			elif r >= 0.5 and r < 0.625:
				inter_arrival_time.append(5)
			elif r >= 0.625 and r < 0.75:
				inter_arrival_time.append(6)
			elif r >= 0.75 and r < 0.875:
				inter_arrival_time.append(7)
			elif r >= 0.875 and r < 1:
				inter_arrival_time.append(8)

			#r = random.random()

			#user defined random number
			r = ur.comcong()

			if r >= 0 and r < 0.16:
				service_time.append(1)
			elif r >= 0.16 and r < 0.33:
				service_time.append(2)
			elif r >= 0.33 and r < 0.5:
				service_time.append(3)
			elif r >= 0.5 and r < 0.66:
				service_time.append(4)
			elif r >= 0.66 and r < 0.83:
				service_time.append(5)
			elif r >= 0.83 and r < 1:
				service_time.append(6)
			

			#Incorrect generation
			#inter_arrival_time.append(random.randint(1,8))
			#service_time.append(random.randint(1,6))


		#print inter_arrival_time,service_time
		arrival_time = np.cumsum(inter_arrival_time)		#find the cumulative sum
		waiting_time = []
		idle_time = []
		service_begin = []
		service_end = []
		time_spent = []
		# initializing all arrays to 0
		waiting_time[:customers] = [0] * customers
		idle_time[:customers] = [0] * customers
		service_begin[:customers] = [0] * customers
		service_end[:customers] = [0] * customers
		time_spent[:customers] = [0] * customers
		# simulation for the first customer
		service_begin[0] = inter_arrival_time[0]
		service_end[0] = service_begin[0] + service_time[0]
		time_spent[0] = service_end[0] - arrival_time[0]
		idle_time[0] = 0
		waiting_time[0] = service_begin[0] - arrival_time[0]
		for i in range(1,customers):
			a=service_end[i-1]
			b=arrival_time[i]
			service_begin[i]=(max(a,b))
			service_end[i] = service_begin[i] + service_time[i]
			waiting_time[i] = service_begin[i] - arrival_time[i]
			time_spent[i] = service_end[i] - arrival_time[i]
			idle_time[i] = arrival_time[i] - service_end[i-1]
		idle_time = np.asarray(idle_time)		#covert to array
		idle_time[idle_time < 0] = 0			#set negative values to 0
		'''
		print "C\tIAT\tAT\tST\tSB\tSE\tWT\tIT"
		for i in range(20):
			print str(i+1)+"\t"+str(inter_arrival_time[i])+"\t"+str(arrival_time[i])+"\t"+str(service_time[i])+"\t"+str(service_begin[i])+"\t"+str(service_end[i])+"\t"+str(waiting_time[i])+"\t"+str(idle_time[i])
		
		print "\t"+str(sum(inter_arrival_time))+"\t"+str(sum(arrival_time))+"\t"+str(sum(service_time))+"\t"+str(sum(service_begin))+"\t"+str(sum(service_end))+"\t"+str(sum(waiting_time))+"\t"+str(sum(idle_time))
		'''
		avg_wait_time=sum(waiting_time)/float(customers)
		average_awt = average_awt + avg_wait_time
	count+=1
	#print str(l)+'\t\t'+str(iterations)+'\t\t'+"{0:.4f}".format(average_awt/iterations)
	spamwriter.writerow([str(count)] + [str(customers)] + [str(iterations)] + ["{0:.6f}".format(average_awt/iterations)])
	#print inter_arrival_time
	#print service_time
