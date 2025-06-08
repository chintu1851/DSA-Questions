# Define a Node in the linked list
class Node:
    def __init__(self, data):
        self.data = data         # Value of the node
        self.next = None         # Pointer to the next node (None by default)


# Define the Linked List with various operations
class LinkedList:
    def __init__(self):
        self.head = None         # Initially, the list is empty

    # Insert a new node at the head (beginning)
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the tail (end)
    def insert_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Insert a new node after a specific value
    def insert_after(self, after, value):
        new_node = Node(value)
        current = self.head

        while current:
            if current.data == after:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        print(f"Item {after} not found in the list.")

    # Print all the elements of the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list


# ==== USAGE ====
ll = LinkedList()

# Insert nodes at head
ll.insert_head(40)
ll.insert_head(30)
ll.insert_head(20)
ll.insert_head(10)

# Insert more nodes
ll.insert_head(0)        # Now: 0 -> 10 -> 20 -> 30 -> 40
ll.insert_tail(50)       # Now: 0 -> 10 -> 20 -> 30 -> 40 -> 50
ll.insert_after(20, 25)  # Now: 0 -> 10 -> 20 -> 25 -> 30 -> 40 -> 50

# Display the final linked list
ll.display()
