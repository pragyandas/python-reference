class TreeNode():
	"""TreeNode class with all methods"""
	def __init__(self,key,val,parent=None,left=None,right=None):
		self.key=key
		self.val=val
		self.parent=parent
		self.left=left
		self.right=right

	def hasLeftChild(self):
		return self.left

	def hasRightChild(self):
		return self.right

	def isLeftChild(self):
		return self.parent and self.parent.left==self
	
	def isRightChild(self):
		return self.parent and self.parent.right=self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.left or self.right)

	def hasAnyChildren(self):
		return self.left or self.right

	def hasBothChildren(self):
		return self.left and self.right

	def replaceNodeData(self,key,val,l,r):
		self.key=key
		self.val=val
		self.left=l
		self.right=r
		# We check to allow None are l and r
		# If child is None we don't need to set parent
		# hasLeftChild or hasRightChild returns true if it is not None
		if self.hasLeftChild():
			self.left.parent=self
		if self.hasRightChild():
			self.right.parent=self