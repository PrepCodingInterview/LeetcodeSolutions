# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        Method: Linked List
        
        Thoughts:
        
        This is the rule where if there is a cycle the intersection point of the slow and fast pointer in said cycle is denoted as {INTERSECT}.
        Then iterating from {INTERSECT} one step at a time and a new pointer from the start of the cycle, their intersection is the start of the cycle.
        
        Proof:
        
        Denote 
        {1->3} as path from 1 to 3
        {3->7} as path from 3 to 7
        {7->3} as path from 7 to 3
        
        Have two pointers
        
        Denote C as path from 3->3 (a full cycle) 
        
        slow pointer path to interestion = {1->3} + {3->7} + X*C (X is some number of cycles)
        fast pointer path to interestion = {1->3} + {3->7} + Y*C (Y is some number of cycles)
        
        Fast path = 2 * Slow path
        
        1. {1->3} + {3->7} + Y*C = 2 * ({1->3} + {3->7} + X*C)
        2. {1->3} + {3->7} + Y*C = 2{1->3} + 2{3->7} + 2X*C
        3. Y*C = {1->3} + {3->7} + 2X*C
        4. (Y-2X)C = {1->3} + {3->7}
        5. {1->3} + {3->7} = (Y-2X)C   KEY {3->7} = C - {7->3}
        6. {1->3} + C - {7->3} = (Y-2X)C
        7. {1->3} = {7->3} + (Y-2X-1)C   NOTE (Y-2X-1)C is just some number of cycles
        8. {1->3} = {7->3} + N*C NOTE N just denotes after some number of cycles
        9. Thus {1->3} = {7->3} after some number of cycles thus there is an intersection at the start of the cycle after some number of cycles.
        
        
        
        
          1-> 2 -> 3 -> 4
                  ↗       ↘
                 8          5
                  ↖        ↙
                   {7} <- 6 
                  
                  
        
        Time: O(n)
        Space: O(1)
        '''
        
        ##create fast and slow pointers
        slow = head 
        fast = head

        ##Find the first intersection point between the fast and slow pointer
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: ##cycle detected, this is the intersection point between the fast and slow pointer
                while head != slow: ## now from the head or start of the linked list iterate one at a time until you reach a slow with slow which is also iterating one at a time
                    head=head.next
                    slow=slow.next
                ##The slow that is returned is the start of the cycle
                return slow
            
        return None
                
                
        