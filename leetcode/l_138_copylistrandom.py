
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        while curr:
            newnode=Node(curr.val)
            newnode.next=curr.next
            curr.next=newnode
            curr=newnode.next
        
        curr= head
        
        while curr:
            if curr.random!=None:
                curr.next.random = curr.random.next
            curr=curr.next.next
        curr=head
        newhead=head.next
        newcurr=newhead
        
        while curr:
            curr.next=newcurr.next
            curr=curr.next
            
            if curr!=None:
                newcurr.next=curr.next
                newcurr=newcurr.next
        return newhead
        
                        