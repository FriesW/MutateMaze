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
		#print master.printable()
		#raw_input()
		#Pick and remove an adjacency
		i = random.randrange(len(candidates))
		adj = candidates.pop(i)
		
		ln = adj.get_low_node() #Low node
		hn = adj.get_high_node() #High node
		
		dist_range = hn.get_distance() - ln.get_distance()
		
		ba = hn.get_low_node_adjacency() #Break adjacency
		for steps in range(random.randrange(dist_range)):
			ba = ba.get_low_node().get_low_node_adjacency()
		
		ba.set_traversable(False)
		candidates.append(ba)
		adj.set_traversable(True)
		hn.set_distance(ln)
		
	return master.printable()
		
		