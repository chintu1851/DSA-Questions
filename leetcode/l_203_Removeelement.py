from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Remove all nodes from the start if they have val
        # while head and head.val == val:
        #     head = head.next
        
        # current = head
        
        # while current and current.next:
        #     if current.next.val == val:
        #         current.next = current.next.next  # Skip the node with val
        #     else:
        #         current = current.next
                
        # return head
        
        prev=None
        current=head
        
        while current:
            if current.val==val:
                if prev:
                    prev.next=current.next
                else:
                    head=current.next
                current=current.next
            else:
                prev,current=current,current.next

def print_linked_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create linked list: 1 -> 6 -> 2 -> 6 -> 3 -> None
node1 = ListNode(1)
node2 = ListNode(6)
node3 = ListNode(2)
node4 = ListNode(6)
node5 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before removal:")
print_linked_list(node1)

sol = Solution()
new_head = sol.removeElements(node1, 6)

print("After removal of 6:")
print_linked_list(new_head)
