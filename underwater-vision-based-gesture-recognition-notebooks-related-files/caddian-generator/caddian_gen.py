#!/usr/bin/python

###############################################
#
# program: caddian_gen.py
# author: Davide Chiarella
# ROS integration: Andrea Ranieri
# version: 0.1
# date: 06 December 2019
# description: generator of CADDIAN messages
# 
###############################################

import sys, getopt
import random
from random import randrange

##################################################

def create_mosaic_num(sentence, num_1, num_2):
	#print('pre-mosaic sentence: ' + sentence)
	sentence += "mosaic " + str(num_1) + " num_delimiter " + str(num_2) + " num_delimiter "
	sentence += "20," + str(num_1) + ",12," + str(num_2) + ",12,"
	return sentence

##################################################


##################################################
def gen_sentence(idx, seed, list_of_commands):
	commands = list_of_commands
	#random.seed(seed)
	# max length of mission is 11
	#num_commands = random.random()
	#print("--Creating sentence of %d length commands" % num_commands)
	num_commands = randrange(1,3)
	sentence=''
	sentence_numbers=''
	print("Creating sentence %d composed by %d commands" % (idx, num_commands))
	for i in range(num_commands):
		sentence += "start_comm "
		sentence_numbers+="10,"
		# choose a random command
		index = randrange(0,7)
		chosen = commands[index]
		#print(index, chosen)
		if chosen == "mosaic":
			num_1 = randrange(1,4)
			num_2 = randrange(1,4)
			sentence = create_mosaic_num(sentence, num_1, num_2)
			#print('post-mosaic sentence: ' + sentence)
		elif chosen == "up":
			sentence += "up " + str(randrange(1,4)) + " num_delimiter "
			sentence_numbers += "21," + str(randrange(1,4)) + ",12,"
		elif chosen == "down":
			sentence += "down " + str(randrange(1,4)) + " num_delimiter "
			sentence_numbers += "22," + str(randrange(1,4)) + ",12,"
		elif chosen == "backwards":
			sentence += "backwards " + str(randrange(1,4)) + " num_delimiter "
			sentence_numbers += "24," + str(randrange(1,4)) + ",12,"
		elif chosen == "boat":
			sentence += "boat "
			sentence_numbers += "28,"
		elif chosen == "carry":
			sentence += "carry "
			sentence_numbers += "26,"
		elif chosen == "photo":
			sentence += "photo "
			sentence_numbers += "25,"
		elif chosen == "here":
			sentence += "here "
			sentence_numbers += "27,"
	sentence += "end_comm"
	sentence_numbers += "11"
	print(sentence)
	print(sentence_numbers)

##################################################
def main(argv):
	seed = 42
	if len(sys.argv) == 1:
		print ('caddian_gen.py -n <number_of_sentences> -s <seed>')
		sys.exit()
	try:
	   opts, args = getopt.getopt(argv,'hn:s:')
	except getopt.GetoptError:
		print ('caddian_gen.py -n <number_of_sentences> -s <seed>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h' or len(sys.argv) < 1:
			print ('caddian_gen.py -n <number_of_sentences> -s <seed> \n seed non serve ad una cippa, ma ormai lo lascio')
			sys.exit()
		elif opt in ("-n"):
			num_sentences = int(arg)
		elif opt in ("-s"):
			seed = arg
	
	commands = ["boat", "carry", "down", "photo", "up", "mosaic", "here", "backwards"]
	
	
	print("\nCreating %d sentences in Caddian language\n" % num_sentences)
	for i in range(num_sentences):
		#print("################")
		#print("Sentence number %d" % i)
		gen_sentence(i, seed, commands)
		#print("end_comm")

if __name__ == "__main__":
   main(sys.argv[1:])
