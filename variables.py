#!/usr/bin/env python

#Importing system function
import sys

#creating varaibles in Python
#string
init_str = "Hello World!"

#integer
init_int = 21
int_condition = 1

#boolean
init_bool = True

#tuple
init_tuple = (12,39)

#list
init_list = ["Hola!","This","is","a","List"]

#Adding spaces between each list element
#creating empty list using list() function
init_list = list()
init_list.append("Hola!")
init_list.append("This")
init_list.append("is")
init_list.append("a")
init_list.append("List")

#Creating a dictionary
init_dict = {"First Name":"Doobie", 
				"Last Name":"vs Doom",
				"Eye Colour":"Government"}

#Accessing elements and changing them
init_list[0] += "!"
init_list[0] = init_list[0] + " :)"
print(init_list[0])

print("{0} {1} has {2} eyes.".format(init_dict["First Name"], 
	init_dict["Last Name"], init_dict["Eye Colour"]))

int_condition = 0;

# if-else statement with conditional 
if int_condition < 1:
	sys.exit("***Exiting***")
else:
	print("***Continuing***")