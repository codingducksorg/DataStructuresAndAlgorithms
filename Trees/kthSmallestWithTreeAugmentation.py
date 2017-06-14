class BSTNode(object):
	def __init__(self, x, size_of_left_tree):
		self.data = x
		self.left = None
		self.right = None
		self.left_tree_size = size_of_left_tree

def kthSmallest(root,k):
	global temp_list
	if (k < root.left_tree_size):
		kthSmallest(root.left, k)
	elif (k > root.left_tree_size):
		kthSmallest(root.right, k-root.left_tree_size)
	else:
		temp_list.append(root.data)

# Test Code
node1 = BSTNode(15, 4)
node2 = BSTNode(9, 2)
node3 = BSTNode(22, 2)
node4 = BSTNode(6, 1)
node5 = BSTNode(13, 1)
node6 = BSTNode(18, 1)
node7 = BSTNode(29, 1)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

temp_list = []
kthSmallest(node1, 2)
print temp_list.pop()
del temp_list[:]

temp_list = []
kthSmallest(node1, 5)
print temp_list.pop()
del temp_list[:]
temp_list = []

kthSmallest(node1, 7)
print temp_list.pop()
del temp_list[:]
