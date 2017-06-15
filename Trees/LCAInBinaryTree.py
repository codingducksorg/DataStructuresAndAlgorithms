class BTNode(object):
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

def lca(root, A, B):
	if not root: return None
	if root.data == A or root.data == B:
		return root
	left = lca(root.left, A, B)
	right = lca(root.right, A, B)
	if left and right:
		# A & B are on both sides
		return root
	else:
		# Either A/B is on one side
		# or A/B is not in Left & Right subtrees
		return left if left else right

# Test Code
root = BTNode(5)
node2 = BTNode(9)
node3 = BTNode(2)
node4 = BTNode(6)
node5 = BTNode(3)
node6 = BTNode(1)
node7 = BTNode(4)
node8 = BTNode(10)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.right = node8

l = lca(root, 3, 4)
print l.data

l = lca(root, 2, 1)
print l.data
