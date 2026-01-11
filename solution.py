from collections import deque

def longest_stable_window(uploads, k):
    max_dq = deque()  # stores indices, values in decreasing order
    min_dq = deque()  # stores indices, values in increasing order

    left = 0
    max_length = 0

    for right in range(len(uploads)):
        # Maintain decreasing deque for max
        while max_dq and uploads[max_dq[-1]] < uploads[right]:
            max_dq.pop()
        max_dq.append(right)

        # Maintain increasing deque for min
        while min_dq and uploads[min_dq[-1]] > uploads[right]:
            min_dq.pop()
        min_dq.append(right)

        # Shrink window if condition is violated
        while uploads[max_dq[0]] - uploads[min_dq[0]] > k:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()

        max_length = max(max_length, right - left + 1)

    return max_length


# Example usage
uploads = [10, 1, 2, 4, 7, 2]
k = 5

result = longest_stable_window(uploads, k)
print(result)
