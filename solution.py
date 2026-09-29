# Problem: Subtract two numbers represented as linked lists
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/subtract-two-numbers-represented-as-linked-lists/

class Solution:
    def solve(self, l1, l2):
        # Helper function to convert linked list to integer
        def to_integer(head):
            num = 0
            while head:
                num = num * 10 + head.val
                head = head.next
            return num
        
        # Convert both lists to integers
        int1 = to_integer(l1)
        int2 = to_integer(l2)
        
        # Subtract the smaller number from the larger one
        if int1 >= int2:
            result_num = int1 - int2
            l1, l2 = l2, l1  # Ensure l1 is always the longer list for simplicity in conversion back to linked list
        else:
            result_num = int2 - int1
        
        # Convert the result back to a linked list
        if l1 == None:
            return ListNode(int(str(result_num)[0]), ListNode(int(str(result_num)[1:])))
        
        dummy_head = ListNode(0)
        current = dummy_head
        for digit in str(result_num):
            current.next = ListNode(int(digit))
            current = current.next
        
        return dummy_head.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))