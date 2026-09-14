# Problem: Multiply two numbers represented linked lists
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/multiply-two-numbers-represented-linked-lists/

class Solution:
    def solve(self, l1, l2):
        MOD = 10**9 + 7
        
        # Helper function to convert linked list to integer
        def ll_to_int(ll):
            num = 0
            while ll:
                num = (num * 10 + ll.val) % MOD
                ll = ll.next
            return num
        
        # Convert both linked lists to integers
        int1 = ll_to_int(l1)
        int2 = ll_to_int(l2)
        
        # Multiply the two numbers and take modulo
        result = (int1 * int2) % MOD
        
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))