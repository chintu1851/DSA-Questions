from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

# Your class with print-based dry run
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # count = 0
        # temp = head  # Add this to fix your original code
        # while temp:
        #     count += 1
        #     print(f"Node Value: {temp.val}, Count: {count}")
        #     temp = temp.next
        # newval=int(count/2)
        # return [input_list[newval:]]  # Dummy return to complete function
                # slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow
# Convert input list [1, 2, 3, 4, 5] to linked list
input_list = [1, 2, 3, 4, 5,6]
dummy = ListNode(0)
current = dummy

for val in input_list:
    current.next = ListNode(val)
    current = current.next

head = dummy.next

# Run dry run
Solution().middleNode(head)
