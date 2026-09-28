# Problem: Clone a linked list with next and random Pointer
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/

class Solution:
    def solve(self):
        class ListNode:
            def __init__(self, val=0, next=None, random=None):
                self.val = val
                self.next = next
                self.random = random
        
        def clone_list(head):
            if not head:
                return None
            
            node_map = {}
            
            current = head
            while current:
                node_map[current] = ListNode(current.val)
                current = current.next
            
            current = head
            while current:
                if current.next:
                    node_map[current].next = node_map[current.next]
                if current.random:
                    node_map[current].random = node_map[current.random]
                current = current.next
            
            return node_map[head]
        
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.random = head
        head.next.next = ListNode(3)
        
        cloned_head = clone_list(head)
        
        current = cloned_head
        while current:
            print(f"Cloned Node {current.val} -> Random: {current.random.val if current.random else 'null'}")
            current = current.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))