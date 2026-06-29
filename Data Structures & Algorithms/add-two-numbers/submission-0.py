class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to easily build the new linked list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop as long as there are nodes to process OR a leftover carry
        while l1 or l2 or carry:
            # Extract values (default to 0 if we've reached the end of a list)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10  # e.g., 12 // 10 = 1
            num = total % 10     # e.g., 12 % 10 = 2
            
            # Create the new node and move our pointer forward
            current.next = ListNode(num)
            current = current.next
            
            # Move to the next nodes in the input lists if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        # The actual result starts from the node after the dummy head
        return dummy_head.next