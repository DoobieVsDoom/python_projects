#!/usr/bin/env python
# User Input program: Integer based
# stores integers, uses collection in control structures

import sys 

print("Welcome. Follow the Prompts :)")
target_int = input("How Many Integers?")

# convert string input to integer
# error handling required if input not integer
try:
	target_int = int(target_int)
except ValueError:
	sys.exit("You must Enter an Integer!")

# integer list collection
int_list = list()
# counter used to keep track of number of variables
count = 0

# keep asking for integer until required quota
while count < target_int:
	new_int = input("Please Enter Integer {0}:".format(count + 1))
	# print to Check current state of list
	print("Current state: " + str(int_list))
	isint = False
	try:
		new_int = int(new_int)
	except:
		print("You Must Enter an Integer!")
	isint = True
	if isint==True:
		# add integer to collection
		int_list.append(new_int)
		#print to check current state of list
		print("State after Value Addition:" + str(int_list))
		# increment count by 1
		count += 1

# using for loop to print		
print("Using For Loop")
for i in int_list:
	print(str(i))

# Or with a While Loop:
print("Using a while loop")
# using len function
total = len(int_list)
count1 = 0
while count1 < total:
	print(str(int_list[count1]))
	count1 += 1