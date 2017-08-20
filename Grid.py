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
		o.set_distance_origin()
	
	def get_non_traversable_adjacencys(self):
		out = []
		current = self.get_origin()
		line_start = current
		
		def consider(dir):
			if current.has_adjacency( dir ):
				adj = current.get_adjacency( dir )
				if not adj.is_traversable():
					out.append(adj)
		
		do = True
		while do:
			while current.has_node( Node.RIGHT ):
				consider( Node.RIGHT )
				consider( Node.BOTTOM )
				current = current.get_node( Node.RIGHT )
			consider( Node.BOTTOM )
			do = line_start.has_node( Node.BOTTOM )
			if do:
				line_start = line_start.get_node( Node.BOTTOM )
				current = line_start
		
		return out
	
	def printable(self, wall_chr = u"\u2588", node_chr = ' ', connector_chr = ' ',\
						horizontal_scale = 3, distance_debug = False):
		def clean(c):
			if type(c) != unicode:
				c = str(c)
			return c[0] * hs
		hs = int(horizontal_scale)
		wc = clean(wall_chr)
		nc = clean(node_chr)
		cc = clean(connector_chr)
		nl = "\n"
		
		out = ""
		current = self.get_origin()
		line_start = current
		
		#Top wall
		out += wc * (self.xd * 2 + 1) + nl
		#Iterate down rows
		for y in range(self.yd):
			#Iterate horizontall across nodes
			row1 = ""
			row2 = ""
			for x in range(self.xd):
				#Row - down nodes
				if distance_debug:
					row1 += str( current.get_distance() ).zfill(horizontal_scale)
				else:
					row1 += nc
				if current.has_adjacency( Node.RIGHT ) and \
					current.get_adjacency( Node.RIGHT ).is_traversable():
					row1 += cc
				else:
					row1 += wc
				
				#Row - between nodes
				if current.has_node( Node.BOTTOM ):
					row2 += wc
					if current.get_adjacency( Node.BOTTOM ).is_traversable():
						row2 += cc
					else:
						row2 += wc
				
				if current.has_node( Node.RIGHT ):
					current = current.get_node( Node.RIGHT )
			
			out += wc + row1 + nl
			
			if current.has_node( Node.BOTTOM ):
				line_start = line_start.get_node( Node.BOTTOM )
				current = line_start
				
				out += row2 + wc + nl
		
		#Bottom wall
		out += wc * (self.xd * 2 + 1)
		return out
		
		