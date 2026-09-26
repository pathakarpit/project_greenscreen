# Problem: Sum of two linked lists
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/sum-of-two-linked-lists/

class Solution:
    def solve(self, l1, l2):
        def add_numbers(node1, node2, carry=0):
            if not node1 and not node2:
                return ListNode(carry) if carry else None
            
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            total = val1 + val2 + carry
            result_node = ListNode(total % 10)
            result_node.next = add_numbers(node1.next if node1 else None, node2.next if node2 else None, total // 10)
            return result_node
        
        return add_numbers(l1, l2)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))