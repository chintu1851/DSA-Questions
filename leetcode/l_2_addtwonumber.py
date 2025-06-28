from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create linked list from list
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

class Solution:
    def reverse_and_stack(self, l: Optional[ListNode]):
        current = l
        prev = None
        stack = []
        
        # Reverse the list and push nodes into stack
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            stack.append(current.val)  # push value to stack
            current = next_node
        
        print("Stack with reversed values:", stack)
        return sum(stack)  # ✅ FIXED

# Create linked lists
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

# Use the solution
sol = Solution()
print("L1 reversed stack sum:", sol.reverse_and_stack(l1))
print("L2 reversed stack sum:", sol.reverse_and_stack(l2))
