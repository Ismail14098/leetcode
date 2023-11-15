class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        i, j = head, head
        while i and j and i.next and i.next.next and j.next:
            i = i.next.next
            j = j.next
            if i == j:
                return True
        return False