from Grid import Grid
import random
from pprint import pprint as pp

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
		i = random.randrange(len(candidates))
		adjo = candidates.pop(i) #Adjacency which is opening
		
		ln = adjo.get_low_node() #Low node
		hn = adjo.get_high_node() #High node
		
		def traceback(src_node):
			out = []
			while src_node.get_distance() > 0:
				out.append( src_node.get_low_adjacency() )
				src_node = src_node.get_low_node()
			return out
		
		ln_traceback = traceback(ln) #Adjacencys from high to origin
		hn_traceback = traceback(hn) #Adjacencys from low to origin
		
		#Traceback will match at beginning, but eventually diverge
		#At divergance point, the loop has begun
		'''
		loop_start = -1
		while abs(loop_start) < min(len(ln_traceback),len(hn_traceback)) and \
			ln_traceback[loop_start] == hn_traceback[loop_start]:
			loop_start -= 1
		loop = ln_traceback[:loop_start] + hn_traceback[:loop_start]
		'''
		loop = []
		for adj in ln_traceback:
			if adj not in hn_traceback:
				loop.append(adj)
		for adj in hn_traceback:
			if adj not in ln_traceback:
				loop.append(adj)
		
		adjc = random.choice(loop) #Adjacency which is closing
		
		adjc.set_traversable(False)
		candidates.append(adjc)
		adjo.set_traversable(True)
		#hn.set_distance(ln)
		master.get_origin().set_distance_origin()
		
	return master.printable()
		
		