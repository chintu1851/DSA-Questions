from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val}"

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            print("Empty list")
            return head

        print("\n--- Starting Rotation ---")
        print("Original List:")
        print_linked_list(head)

        # Step 1: Count length and find tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        print(f"List Length: {length}")
        print(f"Tail Node Value: {tail.val}")

        # Step 2: Optimize rotations
        k = k % length
        print(f"Effective Rotations (k % length): {k}")
        if k == 0:
            print("No rotation needed.")
            return head

        # Step 3: Find new tail node
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
            print(f"Moving curr to Node {curr.val}")

        # Step 4: Set new head and rotate
        newhead = curr.next
        curr.next = None
        tail.next = head

        print(f"New Head After Rotation: {newhead.val}")
        print("Breaking link at:", curr.val)
        print("--- Rotation Complete ---\n",tail.val )
        return newhead

# Helpers
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" → ".join(map(str, result)))

# Test
head = build_linked_list([1, 2, 3, 4, 5])
rotated = Solution().rotateRight(head, 2)
print("Result Linked List:")
print_linked_list(rotated)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr=head
        prev=dummy
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next
        return dummy.next