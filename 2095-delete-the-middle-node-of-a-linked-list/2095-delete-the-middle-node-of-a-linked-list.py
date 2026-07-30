# Definition for singly-linked list.
# class ListNode:
#     def _l_init__(self, val=0, next=None):
#         self.val = var
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #use ai becuase my code got TLE
        if not head or not head.next:
            return None
        
        slow = head
        fast = head.next.next
        
        # Fast pointer 2 kadam chalega, Slow pointer 1 kadam
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Jab Fast end tak pahuchega, Slow middle node ke THEEK PEHLE wale node pe hoga
        # Bypass connection: Middle node ko skip kar do
        slow.next = slow.next.next
        
        return head

            