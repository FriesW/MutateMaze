from Maze import make_maze
from Param_Utils import *
import string
import random


def print_maze(x, y, s, seed):
	print "\n"
	print param_format(x, y, s, seed)
	print make_maze(x, y, s, seed)
	print "\n"

osr = random.SystemRandom()

while True:
	print "Options:"
	print "1 -> Quick maze"
	print "2 -> Size of maze"
	print "3 -> All parameters"
	print "4 -> By hash"
	c = raw_input("Selection: ")
	while not c.isdigit() or int(c) > 4:
		c = raw_input("Selection: ")
	c = int(c)
	
	if c == 1:
		x = osr.randrange(3, 7) + osr.randrange(3, 7)
		y = osr.randrange(3, 7) + osr.randrange(3, 7)
		s = x*y
		seed = ""
		for i in range(10):
			seed += osr.choice(string.ascii_letters + string.digits)
			
		print_maze(x, y, s, seed)
	
	elif c == 2:
		x = int( raw_input("x dimension: ") )
		y = int( raw_input("y dimension: ") )
		s = x*y
		seed = ""
		for i in range(10):
			seed += osr.choice(string.ascii_letters + string.digits)
		print_maze(x, y, s, seed)
	
	elif c == 3:
		x = int( raw_input("x dimension: ") )
		y = int( raw_input("y dimension: ") )
		s = int( raw_input("Mutations: ") )
		seed = raw_input("Seed: ")
		
		print_maze(x, y, s, seed)
	
	elif c == 4:
		hash = raw_input("Enter hash: ")
		l = decode(hash)
		print_maze(l[0], l[1], l[2], l[3])
	
