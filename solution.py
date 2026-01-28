# Problem: Next Permutation
# Difficulty: Medium
# Link: https://leetcode.com/problems/next-permutation/

class Solution:
    def solve(self, arr):
        def permute(nums):
            if len(nums) == 1:
                return [nums[:]]
            
            result = []
            for i in range(len(nums)):
                n = nums[i]
                rest = nums[:i] + nums[i+1:]
                perms_of_rest = permute(rest)
                for perm in perms_of_rest:
                    result.append([n] + perm)
            return result
        
        def next_permutation(nums):
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            
            if i == -1:
                return False
            
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = reversed(nums[i+1:])
            return True
        
        # Generate all permutations in lexicographic order
        perms = permute(arr)
        sorted_perms = [sorted(p) for p in perms]  # Ensure no duplicates by sorting each permutation
        final_perms = list(map(list, set(tuple(x) for x in sorted_perms)))  # Convert tuples to lists and remove duplicates
        
        # Find the next lexicographic permutation
        if not next_permutation(arr):
            return "The next lexicographic permutation is not possible."
        
        return final_perms, arr

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))