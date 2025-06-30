# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode(0)
        dummynode.next = head
        tempnode = dummynode

        while tempnode.next and tempnode.next.next:
            right = tempnode.next
            left = right.next

            # Swapping nodes
            right.next = left.next
            left.next = right
            tempnode.next = left

            # Move tempnode to the next pair
            tempnode = right

        return dummynode.next