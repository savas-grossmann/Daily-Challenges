# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #   slow and ugly
    #    num1, num2 = "", ""
    #    while(True):
    #        if l1 is None and l2 is None:
    #            break
    #        if l1 is not None:
    #            num1 += str(l1.val)
    #            l1 = l1.next
    #        if l2 is not None:
    #            num2 += str(l2.val)
    #            l2 = l2.next
    #    num1, num2 = int(num1[::-1]), int(num2[::-1])
    #    result = num1 + num2
    #    result = list(map(int, str(result)))
    #    result.reverse()
    #    first = True
    #    res = ListNode()
    #    for i in result:
    #        if first:
    #            res = ListNode(i)
    #            curr = res
    #            first = False
    #        else:
    #            curr.next = ListNode(i)
    #            curr = curr.next
    #    return(res)
        res = ListNode()
        curr = res
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return res.next            
