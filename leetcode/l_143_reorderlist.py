from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Your reorderList logic here
        # For now, just a placeholder that does nothing
        pass

# Helper to create linked list from Python list
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

# Helper to print linked list as list of values
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

# Example Usage:
head = create_linked_list([1, 2, 3, 4, 5])
print("Before reorder:")
print_linked_list(head)

sol = Solution()
sol.reorderList(head)

print("After reorder:")
print_linked_list(head)
