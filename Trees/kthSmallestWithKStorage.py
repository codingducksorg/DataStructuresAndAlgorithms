class BSTNode(object):
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

def kthSmallest(root, k):
    global temp_list
    if(not root): return
    if (root.left is not None and len(temp_list) < k):
        kthSmallest(root.left, k)
    if (len(temp_list) < k):
        temp_list.append(root.data)
    if (len(temp_list) < k and root.right is not None):
        kthSmallest(root.right, k)

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
