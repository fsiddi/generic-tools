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
FRAMERATE = 24

time_render_shots = []
shots_list = []

"""
Class shot (render_times.tx)
* name = str
* path = str
* average_rendertime = int
* average_memory = int
* frames_rendertime = [int]
* frames_number = len(frames_rendertime)
---
init info ()
	sets name, path, average_rendertime, average_memory


"""

class Shot(object):
	"""docstring for Shot"""

	#self.__framecount = 0
	
	def __init__(self, render_log_file):
		#super(Shot, self).__init__()
		#self.arg = arg
		render_log_file = open(render_log_file, "r").readlines()
		for i, l in enumerate(render_log_file):
			pass
		self.__framecount = i

		for line in render_log_file:
			if line.startswith('/'):
				shot_data = line.split('|')
				shot_full_path = shot_data[0].split('/')
				self.__name = shot_full_path[len(shot_full_path) - 1]
				self.__average_rendertime = timestring_to_seconds(shot_data[1])
				self.__average_memory = float(shot_data[2].strip())
				self.__total_rendertime = self.__average_rendertime * self.__framecount
			else:
				pass

	def show_infos(self):
		print (self.__framecount)
		print (self.__name)
		print (self.__average_rendertime)
		print (self.__average_memory)
		print (">> " + str(datetime.timedelta(seconds = self.__total_rendertime)))

	def get_total_rendertime(self):
		return self.__total_rendertime

	def get_framecount(self):
		return self.__framecount

def file_len(fname):
	"""Count number of lines in the files

	By counting the lines of each file (and ignoring the first line) we
	obtain the number of rendered frames for that shot.
	"""
	for i, l in enumerate(fname):
		pass
	#return i + 1
	return i

def timestring_to_seconds(render_time):
	"""Convert the time string into and integer (seconds)

	Provide to the function a value like "1h, 20min, 14.8sec" and it will
	return an integer like 3735.
	"""
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
			#print("Rendertime is " + str(timestring_to_seconds(line)) + "sec")
			average_list.append(timestring_to_seconds(line))
			
	average = sum(average_list)/len(average_list)
	
	return average	


	
def shotlist_rendertime(shots_list):
	durations = []
	framecounts = []
	for shot in shots_list:
		durations.append(shot.get_total_rendertime())
		framecounts.append(shot.get_framecount())
	one_machine_time = datetime.timedelta(seconds = sum(durations))
	render_farm_time = datetime.timedelta(seconds = sum(durations)/RENDERFAM_NODES)
	project_framecount = datetime.timedelta(seconds = sum(framecounts)/FRAMERATE)


	print("Amount of shots ................ " + str(len(durations)))
	print("Amount of movie ................ " + str(project_framecount))
	print("Total time on one machine ...... " + str(one_machine_time))
	print("Total renderfarm time .......... " + str(render_farm_time))


#render_time(logfile)
#print file_len(logfile)
#print get_average(logfile)
#get_total_time(logfile)

"""
Now we walk the filesystem and for each 'render_times.txt' we meet we
extract the total render time and add it to a list. In the end we 
will sum up everything to get all the time needed to render all the
shots in the movie
"""

for dirpath, dirnames, filenames in os.walk(FOLDER):
	for filename in filenames:
		if filename == 'render_times.txt':
			fname = os.path.join(FOLDER, filename)
			shot = Shot(fname)
			shots_list.append(shot)

shotlist_rendertime(shots_list)


		
#print KEYWORDS
#print counterline