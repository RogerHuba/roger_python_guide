# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        values = []

        def traverse(head: ListNode):
            nonlocal values
            while head:
                values.append(head.val)
                head = head.next

        for l in lists:
            traverse(l)

        values.sort()

        dummy = curr = ListNode()

        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next