class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getLength(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def intersection(headA: ListNode, headB: ListNode):
    lenA = getLength(headA)
    lenB = getLength(headB)

    # Align the two lists
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Now move both together until they meet or reach end
    while headA != headB:
        headA = headA.next
        headB = headB.next

    return headA  # or None if no intersection
