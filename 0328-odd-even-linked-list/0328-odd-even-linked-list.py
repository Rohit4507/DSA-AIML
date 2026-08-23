# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        fast_head = fast #stores start of even nodes to attach later

        while fast and fast.next:
            slow.next = fast.next #link current odd node to next odd node
            slow = slow.next
            fast.next = slow.next #link current even node to next even node
            fast = fast.next
        slow.next = fast_head

        return head
        