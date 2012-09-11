list_0 = []
list_1 = [3]
list_2 = [35,1]
list_3 = [7,1,2]
list_4 = [1,1,1,4,4,5,6,2,3,0]
list_5 = [11,4,6,10,1,9,3,30,22,2,7]
list_6 = [33,2,4,5,5,5,1,1,2,5]

lists_list = []

## We append all this lists to another list for unit testing

for r in range(7):
	lists_list.append(eval("list_" + str(r)))
	
##  This is the function containing the sorting algorithm. At the
##  moment it does not get rid of duplicated numbers. This should
##  be maybe part of another function.

def sortList(unsorted_list):
	print "Unsorted list:", unsorted_list
	if len(unsorted_list) > 3:
		small_list = []
		big_list = []
		
		main_counter = 0
		
		i = 0
		small = unsorted_list[i]
		big = unsorted_list[i+1]
		
		if small < big:
			pass
		else:
			big = unsorted_list[i]
			small = unsorted_list[i+1]
			
		i += 2
		
		for n in range(len(unsorted_list)-2):
			number = unsorted_list[i]
			print number
			if number < small:
				small = number 
				print "hello"
			elif number > big:
				big = number 
			else:
				pass
			i += 1
		print small, big
				
		small_list.append(small)
		big_list.append(big)
		unsorted_list.remove(small)
		unsorted_list.remove(big)
			
		big_list.reverse()
		
		#print unsorted_list
		#print small_list
		#print big_list
		
		small_list.extend(unsorted_list)
		small_list.extend(big_list)
		
		print "Sorted list:", small_list
	
	else:
		pass


##  Running unit tests by making a loop that reads a list of lists
##  created at the beginning

for unsorted_list in lists_list:
	sortList(unsorted_list)
	print ""

