#!/usr/bin/python

# https://docs.python.org/3/library/enum.html#functional-api
# https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python

import sys
from enum import Enum

class gestures(Enum):
	#NUMBERS
	one = 1
	two = 2
	three = 3
	four = 4
	five = 5
	six = 6
	seven = 7
	eight = 8
	nine = 9
	zero = 0  # same as wait
	
	#CADDIAN DELIMITERS
	start_comm = 10
	end_comm = 11
	number_delimiter = 12
	
	#CADDIAN AGENTS
	you = 24  # same as go_backward = 24
	me = 13
	we = 14
	
	#QUANTITY
	plus = 21  # same as go_up
	minus = 22  # same as go_down
	
	#ACTIONS
	go_up = 21  # same as plus
	go_down = 22  # same as minus
	go_forward = 23
	go_backward = 24  # same as you = 24
	
	#PLACES
	here = 27
	boat = 28
	point_of_interest = 29
	
	#SET VARIABLES
	var_air = 31
	var_light = 32
	var_level = 33
	var_speed = 34
	
	#WORKS
	wait = 0  # same as zero
	mosaic = 20
	take_photo = 25
	carry = 26
	check = 35 
	turn = 36
	start_for = 37
	end_for = 38
	do = 39
	follow = 50
	take = 51
	come = 52
	
	#LEVEL
	free = 71
	const = 72
	limit = 73
	
	#FEEDBACK
	ok = 81
	no = 82
	question = 83
	# ONLY SLANG
	low = 84
	reserve = 85
	
	#EMERGENCY
	danger = 40
	out_of_air = 41
	out_of_breath = 42
	general_evacuation = 43
	problem = 44
	cold = 45
	cramp = 46
	ear = 47
	vertigo = 48
	abort_mission = 49


def main(argv):
	work  = gestures['mosaic']
	three = gestures.three
	print(work)
	print(three)
	print(gestures(work.value+three.value))

if __name__ == "__main__":
   main(sys.argv[1:])
