class BSTNode(object):
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

def kthSmallest(root, k):
	if(not root): return None
	size = tree_size(root.left)
	if k == size + 1:
		return root.data
	elif k < size + 1:
		return kthSmallest(root.left, k)
	else:
		return kthSmallest(root.right, k - 1 - size)

def tree_size(root):
	if not root:
		return 0
	
	return tree_size(root.left) + tree_size(root.right) + 1

# Test Code
node1 = BSTNode(15)
node2 = BSTNode(9)
node3 = BSTNode(22)
node4 = BSTNode(6)
node5 = BSTNode(13)
node6 = BSTNode(18)
node7 = BSTNode(29)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

print kthSmallest(node1, 2)
print kthSmallest(node1, 5)
print kthSmallest(node1, 7)
