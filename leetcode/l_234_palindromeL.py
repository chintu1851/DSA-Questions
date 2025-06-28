# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLink(self, head: ListNode) -> ListNode:
        prev = None
        curr = head  # ✅ fixed from "Head"

        while curr:
            next_node = curr.next  # ✅ renamed for clarity
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Use two-pointer to find the middle
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse second half
        rev = self.reverseLink(slow)

        # Step 3: Compare both halves
        firsthalf = head
        secondhalf = rev
        while secondhalf:
            if firsthalf.val != secondhalf.val:
                return False
            firsthalf = firsthalf.next
            secondhalf = secondhalf.next

        return True
