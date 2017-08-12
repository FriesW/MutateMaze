class Adjacency:
	
	def __init__(self, node1, node2):
		self.node1 = node1
		self.node2 = node2
		self.traversable = False
	
	def set_traversable(self, is_traversable):
		self.traversable = is_traversable
	
	def is_traversable(self):
		return self.traversable
	
	def get_node_1(self):
		return self.node1
	
	def get_node_2(self):
		return self.node2
	
	def get_high_node(self):
		n1d = self.node1.get_distance()
		n2d = self.node2.get_distance()
		if n1d > n2d:
			return node1
		else:
			return node2
	
	def get_low_node(self):
		n1d = self.node1.get_distance()
		n2d = self.node2.get_distance()
		if n1d < n2d:
			return node1
		else:
			return node2
	
	def get_other_node(self, node):
		if node == self.node1:
			return self.node2
		elif node == self.node2:
			return self.node1
		else:
			raise KeyError("Provided node is not in this adjacency.")