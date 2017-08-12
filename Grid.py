from Node import Node

class Grid:
	
	def __init__(self, xd, yd):
		self.xd = int(xd)
		self.yd = int(yd)
		if self.xd < 1 or self.yd < 1:
			raise ValueError("Grid dimensions must be one or greater.")
		
		def make_line(length):
			first = Node()
			current = first
			for x in range(length - 1):
				current.set_node( Node(), Node.RIGHT )
				current = current.get_node( Node.RIGHT )
			return first
		
		def zip_lines(top, bottom):
			while top.has_node( Node.RIGHT ) and bottom.has_node( Node.RIGHT):
				top.set_node(bottom, Node.BOTTOM)
				top = top.get_node( Node.RIGHT )
				bottom = bottom.get_node( Node.RIGHT )
			top.set_node(bottom, Node.BOTTOM)
		
		#Make grid
		self.top_left = make_line(self.xd)
		row_old = self.top_left
		for i in range(self.yd - 1):
			row_new = make_line(self.xd)
			zip_lines(row_old, row_new)
			row_old = row_new
	
	def get_origin(self):
		return self.top_left
	
	def s_pattern(self):
		current = self.get_origin()
		dir_right = True
		
		for y in range(self.yd):
			for x in range(self.xd - 1):
				if dir_right:
					current = current.get_node( Node.RIGHT )
					current.get_adjacency( Node.LEFT ).set_traversable(True)
				else:
					current = current.get_node( Node.LEFT )
					current.get_adjacency( Node.RIGHT).set_traversable(True)
			dir_right = not dir_right
			if y != self.yd - 1:
				current = current.get_node( Node.BOTTOM )
				current.get_adjacency( Node.TOP ).set_traversable(True)
		
		o = self.get_origin()
		#o.set_distance_origin()
		