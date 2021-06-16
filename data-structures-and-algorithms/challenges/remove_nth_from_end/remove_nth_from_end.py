class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head:
            slow = fast = prev = head
            slow_count = fast_count = 0
            
            while fast:
                fast = fast.next
                fast_count += 1
                
                if (fast_count - slow_count) > n:
                    prev = slow
                    slow = slow.next
                    slow_count += 1
            
            if prev == slow:
                head = prev.next
            else:
                prev.next = slow.next
        
        return head