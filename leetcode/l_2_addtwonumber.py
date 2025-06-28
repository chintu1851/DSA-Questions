from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to create a linked list from a Python list
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

# Function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Solution class
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        current = dummy_node
        carry = 0
        
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            total = value1 + value2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_node.next

# Create input linked lists
l1 = create_linked_list([2, 4, 3])  # Represents 342
l2 = create_linked_list([5, 6, 4])  # Represents 465

# Add numbers and print result
sol = Solution()
result = sol.addTwoNumbers(l1, l2)  # Should be 807 → [7 -> 0 -> 8]
print("Resulting Linked List (Sum):")
print_linked_list(result)
