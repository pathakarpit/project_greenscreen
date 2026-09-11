# Problem: Delete without Head node
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/

class Solution:
    def solve(self, node):
        if not node or not node.next:
            return
        
        # Copy the data from the next node to the current node
        node.val = node.next.val
        # Bypass the next node by changing the pointer of the current node to skip the next node
        node.next = node.next.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))