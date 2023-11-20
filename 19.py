# First Solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        i, target = 0, size-n
        curr = head
        while curr:
            if i == target:
                return curr.next
            if i+1 == target:
                if curr.next is None:
                    return head
                curr.next = curr.next.next
                return head
            i += 1
            curr = curr.next
        return head

# Follow up in one pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        l, r = head, head
        while i < n:
            r = r.next
            i += 1
        while r:
            if r.next is None:
                l.next = l.next.next
                return head
            l = l.next
            r = r.next
        return head.next