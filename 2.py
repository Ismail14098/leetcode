class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        
        head = ListNode()
        curr = head
        tmp = 0
        while l1 or l2:
            result = tmp
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            tmp = 0
            if result >= 10:
                curr.next = ListNode(result-10)
                tmp = 1
            else:
                curr.next = ListNode(result)
            curr = curr.next
        if tmp == 1:
            curr.next = ListNode(1)
        return head.next