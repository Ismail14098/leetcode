class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return None

        # find mid
        slow, fast = head, head
        while True:
            if fast.next == None:
                break
            fast = fast.next
            if fast.next == None:
                break
            fast = fast.next
            if slow.next == None:
                break
            slow = slow.next
        
        second = slow.next
        slow.next = None

        # reverse second part
        curr = second
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # reorder
        second = prev
        first = head
        while first and second:
            firstNext = first.next
            secondNext = second.next
            first.next = second
            first = first.next
            first.next = firstNext
            first = first.next 
            second = secondNext