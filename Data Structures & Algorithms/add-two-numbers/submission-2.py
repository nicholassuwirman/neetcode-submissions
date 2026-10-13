# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# No need to reverse the linkedlist
# you could just take 1->2->3 into 123
# and reverse the number string! using str[::-1]

# resNum = 321 + 654 
# resNum = 975

# dummy -> 5 -> 7 -> 9
# return dummy.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        s1 = ""
        while curr1:
            s1 += str(curr1.val)
            curr1 = curr1.next
        s1Rev = s1[::-1]
        s1Num = int(s1Rev)

        curr2 = l2
        s2 = ""
        while curr2:
            s2 += str(curr2.val)
            curr2 = curr2.next
        s2Rev = s2[::-1]
        s2Num = int(s2Rev)
       

        resNum = s1Num + s2Num
        resStr = str(resNum)
        # could also use this resStrRev = resStr[::-1], then for ch in resStrRev
        dummy = ListNode(0, None)
        curr = dummy
        for ch in reversed(resStr):
            chNum = int(ch)
            nodeNum = ListNode(chNum, None)
            curr.next = nodeNum
            curr = curr.next
        
        return dummy.next
        


