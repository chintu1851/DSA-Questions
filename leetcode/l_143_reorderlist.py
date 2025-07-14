from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None    # Important to cut the list here!
        prev = None
        
        while second:
            tempnode = second.next
            second.next = prev
            prev = second
            second = tempnode
            
        first = head
        second = prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

            

    

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
middle_node = sol.reorderList(head)

print("Middle node value:", middle_node.val if middle_node else None)

print("After reorder:")
print_linked_list(head)
