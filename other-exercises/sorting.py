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
	small_list = []
	big_list = []
	
	main_counter = 0
	
	##  We run this loop to check couples, therefore it must run
	##  for half the lenght of the list
	
	half_list = len(unsorted_list)/2
	print "Input list:", unsorted_list
	
	while main_counter < half_list:
	
		##  This section of the code gets the biggest and smallest
		##  number from the given list
		#print "unsorted len:", len(unsorted_list)
		i = 0
		small = unsorted_list[i]
		big = unsorted_list[i+1]
		#print "Input list:", unsorted_list
		
		##  Here we make sure that big and small have actually the
		##  corresponding values in the couple
		
		if small < big:
			pass
		else:
			big = unsorted_list[i]
			small = unsorted_list[i+1]
			
		#print small, "<", big
		
		##  Once this is done we go throught the remaining numbers
		##  in the list (so we start counting the after the second)
		
		list_item_count = 2
		while list_item_count < len(unsorted_list):
			next_number = unsorted_list[list_item_count]
			#print(next_number)
			
			if next_number < small:
				small = next_number
			elif next_number > big:
				big = next_number
			
			list_item_count +=1
			
		#print small, "<", big
		
		##  Now we need to append numbers to the proper lists and
		##  strip them from the unsorted list
		
		small_list.append(small)
		big_list.append(big)
		unsorted_list.remove(small)
		unsorted_list.remove(big)
		
		main_counter +=1
		#print "main counter:", main_counter
	
	
	big_list.reverse()
	
	#print unsorted_list
	#print small_list
	#print big_list
	
	small_list.extend(unsorted_list)
	small_list.extend(big_list)
	
	print "Sorted list:", small_list


##  Running unit tests by making a loop that reads a list of lists
##  created at the beginning

for unsorted_list in lists_list:
	sortList(unsorted_list)
	print ""

