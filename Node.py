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
	
	#Alternate approach: continue recursion until distance is correct/what it would be set to
	#This approach would work with non-standard mazes and prevent runaway recursion
	def set_distance(self, src):
		self.distance = src.get_distance() + 1
		for adj in self.get_all_adjacencys():
			if adj.is_traversable():
				other = adj.get_other_node(self)
				if other != src:
					other.set_distance(self)
	
	def set_distance_origin(self):
		self.distance = 0
		for adj in self.get_all_adjacencys():
			if adj.is_traversable():
				adj.get_other_node(self).set_distance(self)
	
	def set_node(self, node, dir):
		adj = Adjacency(self, node)
		self.adjacencys[dir] = adj
		node.adjacencys[self.__inverse[dir]] = adj
	
	def has_adjacency(self, dir):
		return self.adjacencys[dir] != None
	
	def has_node(self, dir):
		return self.has_adjacency(dir)
	
	def get_all_adjacencys(self):
		out = []
		for adj in self.adjacencys:
			if adj != None:
				out.append(adj)
		return out
	
	def get_adjacency(self, dir):
		if not self.has_adjacency(dir):
			raise IndexError("Adjacency doesn't exist.")
		return self.adjacencys[dir]
	
	def get_node(self, dir):
		if not self.has_node(dir):
			raise IndexError("Node doesn't exist.")
		return self.adjacencys[dir].get_other_node(self)
	
	def get_low_adjacency(self):
		for adj in self.adjacencys:
			if adj != None and adj.is_traversable():
				if adj.get_low_node() != self:
					return adj
		raise IndexError("No node smaller than this one! Distance is " + str(self.get_distance()))
	
	def get_low_node(self):
		return self.get_low_adjacency().get_low_node()
	
	def print_x_y(self):
		tx = self
		x = 0
		ty = self
		y = 0
		while tx.has_node( Node.LEFT ):
			tx = tx.get_node( Node.LEFT )
			x += 1
		while ty.has_node( Node.TOP ):
			ty = ty.get_node( Node.TOP )
			y += 1
		print x, ",", y