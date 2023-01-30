# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""This defines the structure of a node in a singly-linked list. Each node has a value val and a pointer next to the
next node in the list. The default value of val is 0 and the default value of next is None."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''This defines the Solution class and the addTwoNumbers method which takes two linked lists l1 and l2 as input and 
returns a linked list as output.'''


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """This creates a dummy node with value 0 and sets it as the current node cur.This dummy node is used as the
        head of the resulting linked list."""
        dummy = cur = ListNode(0)
        """This sets the carry to 0, which is used to store the carry from one digit to another during the addition."""
        carry = 0
        """ This while loop continues until all the nodes in both l1 and l2 have been processed and the carry is 0."""
        while l1 or l2 or carry:
            """If l1 is not None, add the value l1.val to the carry and move to the next node in l1."""
            if l1:
                carry += l1.val
                l1 = l1.next

                """If l2 is not None, add the value l2.val to the carry and move to the next node in l2."""
            if l2:
                carry += l2.val
                l2 = l2.next

                """Create a new node with value carry % 10 and set it as the next node of the current node cur.Move 
                cur to the newly created node."""
            cur.next = ListNode(carry % 10)
            cur = cur.next

            """Update the carry by dividing it by 10."""

            carry //= 10
            """ Return the next node of the dummy node, which is the head of the  resulting linked list."""
        return dummy.next


