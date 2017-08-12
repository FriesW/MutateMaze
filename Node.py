from Adjacency import Adjacency

class Node:
	
	TOP = 0
	RIGHT = 1
	BOTTOM = 2
	LEFT = 3
	
	__inverse = [BOTTOM, LEFT, TOP, RIGHT]
	
	def __init__(self):
		self.adjacencys = [None, None, None, None]
		self.distance = -1
	
	def get_distance(self):
		if self.distance == -1:
			raise LookupError("Distance has not yet been set.")
		return self.distance
	
	def set_distance(self, src):
		self.distance = src.get_distance() + 1
		for adj in self.adjacencys:
			other = adj.get_other_node(self)
			if other != src:
				other.set_distance(self)
	
	def set_raw_distance(self, dist):
		self.distance = dist
	
	def set_node(self, node, dir):
		adj = Adjacency(self, node)
		self.adjacencys[dir] = adj
		node.adjacencys[__inverse[dir]] = adj
	
	def has_adjacency(self, dir):
		return self.adjacencys[dir] != None
	
	def has_node(self, dir):
		return self.has_adjacency(dir)
	
	def get_adjacency(self, dir):
		if not has_adjacency(dir):
			raise IndexError("Adjacency doesn't exist.")
		return self.adjacencys[dir]
	
	def get_node(self, dir):
		if not has_node(dir):
			raise IndexError("Node doesn't exist.")
		return self.adjacencys[dir].get_other_node(self)