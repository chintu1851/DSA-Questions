class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Traverse and print
currentnode = node1
while currentnode is not None:
    print("current data", currentnode.data, end=' -> ')
    currentnode = currentnode.next
print("None")
