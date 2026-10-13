# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 
# 1 -> 2 -> 3 -> Null
# Null <- 1 <- 2 <- 3
#                 prev1 curr1 nxt1
# "321" change to 321

# 4 -> 5 -> 6
# Null <- 4 <- 5 <- 6
#                  curr2
# "654" change to 654

# resNum = 321 + 654 
# resNum = 975

# dummy -> 5 -> 7 -> 9
# return dumm.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1 = None
        curr1 = l1
        while curr1:
            nxt1 = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = nxt1

        s1 = ""
        while prev1:
            s1 += str(prev1.val)
            prev1 = prev1.next
        s1Num = int(s1)

        prev2 = None
        curr2 = l2
        while curr2:
            nxt2 = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = nxt2

        s2 = ""
        while prev2:
            s2 += str(prev2.val)
            prev2 = prev2.next
        s2Num = int(s2)

        resNum = s1Num + s2Num
        resStr = str(resNum)
        dummy = ListNode(0, None)
        curr = dummy
        for ch in reversed(resStr):
            chNum = int(ch)
            nodeNum = ListNode(chNum, None)
            curr.next = nodeNum
            curr = curr.next
        
        return dummy.next
        


