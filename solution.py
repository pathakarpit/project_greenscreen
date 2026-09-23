# Problem: Merge K Sorted Lists
# Difficulty: Hard
# Link: https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    def solve(self, lists):
        # Define a min-heap and an initial dummy head for the merged list
        heap = []
        dummy = ListNode()
        current = dummy
        
        # Push the first element of each list into the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # While there are elements in the heap
        while heap:
            # Pop the smallest element from the heap
            val, idx, node = heapq.heappop(heap)
            # Add this node to the merged list
            current.next = ListNode(val)
            current = current.next
            # If there is a next node in the list, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        # Return the merged list starting from dummy.next
        return dummy.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))