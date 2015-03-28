#!/usr/bin/env python

# for..else example

def do_for_else(foo):
    for i in foo:
	if i == 0:
    	    break
    else:
	print("i was never 0")

print ('running with no 0')
do_for_else([1,2,3,4,5,6])
print ('running with 0')
do_for_else([0,2,3,4,5,6])