class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')
        
class Shape(Root):
	"""docstring for Shape"""
	def __init__(self,shapeName,**kwds):
		self.shapeName = shapeName
		super().__init__(**kwds)

	def draw(self):
		print ('ShapeName:',self.shapeName)
		super().draw()

class Color(Root):
	def __init__(self,color,**kwds):
		self.color = color
		super().__init__(**kwds)

	def draw(self):
		print ('Color:',self.color)
		super().draw()
		

class Triangle(Shape,Color):
	def __init__(self,sideCount,**kwds):
		self.sideCount=sideCount
		super().__init__(**kwds)

	def draw(self):
		print ('SideCount: ',self.sideCount)
		super().draw()

t=Triangle(sideCount=5,color="Green",shapeName="Triangle")
t.draw()
