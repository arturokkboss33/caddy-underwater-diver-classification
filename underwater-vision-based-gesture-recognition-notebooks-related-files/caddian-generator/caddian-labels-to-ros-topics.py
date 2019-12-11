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

import sys
import os
import copy

import roslib
import rospy
# from std_msgs.msg import Bool
# from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import Int32MultiArray

from gestures import gestures

# rostopic pub -1 /buddy/diver/command/detected_phrase std_msgs/Int32MultiArray "{layout:{dim:[{label: '', size: 0, stride: 0}], data_offset: 0}, data: [10,25,3,3,12,11]}"

##################################################

conversion_map = {
			'1': 'one',
			'2': 'two',
			'3': 'three',
			'4': 'four',
			'5': 'five',
			'photo': 'take_photo',
			'num_delimiter': 'number_delimiter',
			'down': 'go_down',
			'up': 'go_up',
			'backwards': 'go_backward',
			'forward': 'go_forward',
		}

def main(argv):
	fn = argv[0]
	print('Opening sentences file:', fn)
	with open(fn, 'r') as fp:
		line = fp.readline()
		while line and not rospy.is_shutdown():
			print('LINE ---------', line)
			tokens   = line.split()
			sentence = Int32MultiArray()
			for tok in tokens:
				print(tok)
				if tok in conversion_map:
					print(tok, 'has been converted to:', conversion_map[tok])
					tok = conversion_map[tok]
				this_gesture = gestures[tok]
				print(this_gesture)
				sentence.data.append(this_gesture.value)
			print('Publishing sentence', sentence)
			publisher_sentence.publish(sentence)
			line = fp.readline()
			rate.sleep()


if __name__ == "__main__":
	if len(sys.argv) > 1:
		rosnode_name = "caddian_interpreter_module"
		rospy.init_node(rosnode_name)
		pub_sentence_topic = "/buddy/diver/command/detected_phrase"
		publisher_sentence = rospy.Publisher(pub_sentence_topic, Int32MultiArray, queue_size=10)
		rate = rospy.Rate(10) # 10hz
		sentence = Int32MultiArray()
		sentence.data = [1, 2, 3]
		print('Publishing fake sentence', sentence, 'because the first one is never received and I don\'t have time to find why...')
		publisher_sentence.publish(sentence)
		for i in range(50):
			rate.sleep()
		main(sys.argv[1:])
	else:
		print('Please provide a filename containing the Caddian sentences to read.')
