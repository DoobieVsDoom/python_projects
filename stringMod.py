#!/usr/bin/env python
# define function that can accept strings 
# and modify them beyond function scope

def modify_string(original):
	print("In Function Scope.")
	original += " that has been modified."
	print(original)
	print("Exiting Function Scope.")
	# only local copy of string modified

def modify_string_return(original):
	print("In Function Scope.")
	original += " that has been modified."
	print("Exiting Function Scope.")
	return original
	# return modified original beyond function scope

# testing function operations
test_string = "This is a test string"

modify_string(test_string)
# checking if global test_string is modified
print(test_string)

test_string = modify_string_return(test_string)
# checking if global test_string modified
print(test_string)