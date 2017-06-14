class BSTNode(object):
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

#in-order traversal and global variable to count smallest K
#Time complexity: O(n)
#Space complexity: O(1)
counter = 0
def kthSmallest(root, k):
	global counter
	if(not root): return None
	left = kthSmallest(root.left, k)
	if (left is not None):
		return left
	counter = counter + 1
	if (k == counter):
		return root.data
	return kthSmallest(root.right, k)

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
