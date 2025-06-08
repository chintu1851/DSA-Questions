class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to next node (default is None)

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def insert_head(self, value):
        new_node = Node(value)        # Step 1: Create a new node
        new_node.next = self.head     # Step 2: Point new node's next to current head
        self.head = new_node          # Step 3: Update head to new node

    def insert_tail(self, value):
        new_node = Node(value)
        
        # Handle empty list: if head is None, new node becomes head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the list
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node  # Attach new node at the end

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of list

# Create linked list and insert nodes
ll = LinkedList()

# Insert original nodes at head
ll.insert_head(40)
ll.insert_head(30)
ll.insert_head(20)
ll.insert_head(10)

# Add a new node at head and at tail
ll.insert_head(0)    # List becomes: 0 -> 10 -> 20 -> 30 -> 40
ll.insert_tail(50)   # List becomes: 0 -> 10 -> 20 -> 30 -> 40 -> 50

# Display the updated linked list
ll.display()
