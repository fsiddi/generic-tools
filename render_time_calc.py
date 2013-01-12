"""Rendertime parser

	This script walks around the filesystem, looking for "render_times.txt"
	files, and for each one of them gets the average rendertime per frame
	and the total rendertime based on the amount of logged frames.
	It then sums up everything and tells how many days with one machine or 
	more machines.
	
"""

import datetime
import os

FOLDER = "/Users/fsiddi/Desktop"
RENDERFAM_NODES = 30

time_render_shots = []


def file_len(fname):
	"""
	"""
	for i, l in enumerate(fname):
		pass
	#return i + 1
	return i

def timestring_to_seconds(render_time):
	to_sum =[]
	render_time = render_time.split(',')
	
	for elem in render_time:
		#print elem.strip()
		if elem.endswith('h'):
			h = int(elem.strip('h'))
			hours = h * 3600
			#print hour
			to_sum.append(hours)
		else:
			hour = 0
		if elem.endswith('min'):
			m = int(elem.strip('min'))
			minutes = m * 60
			to_sum.append(minutes)
		else:
			minutes = 0
			#print minute
		if elem.endswith('sec '):
			seconds = int(elem.strip('sec ').split('.')[0])
			to_sum.append(seconds)
		else:
			seconds = 0	
	#print("Rendertime is " + str(sum(to_sum)) + "sec")
	
	return sum(to_sum)
	

def render_time(fname):
	counterline = []
	counter = 0
	average_list = []
	for line in fname:
		if line.startswith('/'):
			pass
		else:
			line = line.split('|')[1]
			#print line
			
			#print render_time
			
			#print("Rendertime is " + str(timestring_to_seconds(line)) + "sec")
			average_list.append(timestring_to_seconds(line))
			
	average = sum(average_list)/len(average_list)
	
	#print("Average rendertime: " + str(average) + "sec aka " + str(datetime.timedelta(seconds = average)))
	return average	

def get_average(fname):
	for line in fname:
		if line.startswith('/'):
			time = timestring_to_seconds(line.split('|')[1])
		else:
			pass
	return time

def get_total_time(fname):
	val = file_len(fname)*get_average(fname)
	print("Total render time is: " + str(datetime.timedelta(seconds = val)))
	return val
	

#render_time(logfile)
#print file_len(logfile)
#print get_average(logfile)
#get_total_time(logfile)

for dirpath, dirnames, filenames in os.walk(FOLDER):
	for filename in filenames:
		if filename == 'render_times.txt':
			fname = os.path.join(FOLDER, filename)
			fname = open(fname, "r").readlines()

			time_render_shots.append(get_total_time(fname))

print (datetime.timedelta(seconds = sum(time_render_shots)))


		
#print KEYWORDS
#print counterline