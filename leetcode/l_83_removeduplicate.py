from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # skip duplicate
            else:
                current = current.next  # move forward
            print("this is current",current.val)
        return head

# Helper function to print the list:
def printList(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print("Before:")
printList(head)

sol = Solution()
head = sol.deleteDuplicates(head)

print("After removing duplicates:")
printList(head)
