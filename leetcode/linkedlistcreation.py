# Define a Node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the Linked List with various operations
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

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

    def delete_head(self):
        if self.head is None:
            print("Empty Linked List")
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("List is already empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def search_and_delete(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.delete_head()
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        print("Value not found")

    def search_valueindex(self, value):
        current = self.head
        pos = 0
        while current:
            if current.data == value:
                return pos
            current = current.next
            pos += 1
        return "not found"

    def get_item(self, index):
        current = self.head
        pos = 0
        while current:
            if pos == index:
                return current.data
            current = current.next
            pos += 1
        return "Index out of range"

    def clear(self):
        self.head = None
        print("Linked list has been cleared.")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ==== USAGE ====
ll = LinkedList()

ll.insert_head(40)
ll.insert_head(30)
ll.insert_head(20)
ll.insert_head(10)
ll.insert_head(0)         # 0 -> 10 -> 20 -> 30 -> 40
ll.insert_tail(50)        # 0 -> 10 -> 20 -> 30 -> 40 -> 50
ll.insert_after(20, 25)   # 0 -> 10 -> 20 -> 25 -> 30 -> 40 -> 50

ll.delete_head()          # Delete 0
ll.delete_end()           # Delete 50
ll.search_and_delete(10)  # Delete 10

# === Get index of a value ===
print("Index of 30:", ll.search_valueindex(30))

# === Get value at index ===
print("Value at index 1:", ll.get_item(1))

# === Display final linked list ===
ll.display()
ll.clear()