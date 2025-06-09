# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        print("Dummy value (should be 0):", dummy.val)    
        return dummy.next

# Creating two sample linked lists manually
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))

# Merging and printing
sol = Solution()
merged = sol.mergeTwoLists(list1, list2)

# Print merged result
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next
print("None")
