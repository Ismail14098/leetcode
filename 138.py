class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        copy = Node(head.val)
        d = {}

        curr = head
        currCopy = copy
        while curr:
            d[curr] = currCopy
            if curr.next != None:
                currCopy.next = Node(curr.next.val)
            currCopy = currCopy.next
            curr = curr.next
        
        curr = head
        currCopy = copy
        while curr and currCopy:
            if curr.random != None:
                currCopy.random = d[curr.random]
            currCopy = currCopy.next
            curr = curr.next
        return copy