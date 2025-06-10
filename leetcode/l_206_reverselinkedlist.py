from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to current
            current = next_node       # Move current forward
            print(
    f"next_node: {next_node.val if next_node else None}, "
    f"prev: {prev.val if prev else None}, "
    f"current: {current.val if current else None}"
)

        return prev  # New head of reversed list

# Create linked list: 1 -> 3 -> 5 -> None
head = ListNode(1, ListNode(3, ListNode(5)))

# Reverse and print the list
sol = Solution()
reversed_head = sol.reverseList(head)

# Print reversed list
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next
print("None")
