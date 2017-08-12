from Grid import Grid
import random

def make_maze(xd, yd, cycles, seed):
	xd = int(xd)
	yd = int(yd)
	cy = int(cycles)
	#seed = sanitize_seed(seed)
	
	random.seed(seed)
	
	master = Grid(xd, yd)
	master.s_pattern()
	candidates = master.get_non_traversable_adjacencys()
	
	for cycle in range(cy):
		if cycle%1000 == 0:
			print cycle
			print master.printable()
			#raw_input()
		#Pick and remove an adjacency
		i = random.randrange(len(candidates))
		adjo = candidates.pop(i) #Adjacency which is opening
		
		ln = adjo.get_low_node() #Low node
		hn = adjo.get_high_node() #High node
		
		adjc = hn.get_low_node_adjacency() #Adjacency which is closing
		
		adjc.set_traversable(False)
		candidates.append(adjc)
		adjo.set_traversable(True)
		hn.set_distance(ln)
		
	return master.printable()
		
		