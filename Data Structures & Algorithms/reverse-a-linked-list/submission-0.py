# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Step 1: Temporarily store the next node
            curr.next = prev       # Step 2: Reverse the current node's pointer
            prev = curr            # Step 3: Move the 'prev' pointer one step forward
            curr = next_node       # Step 4: Move the 'curr' pointer one step forward
            
        return prev  # 'prev' will be pointing to the new head of the reversed list