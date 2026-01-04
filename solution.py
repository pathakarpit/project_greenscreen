def can_finish(tasks, k, max_time):
    workers = 1
    current_time = 0

    for task in tasks:
        if current_time + task <= max_time:
            current_time += task
        else:
            workers += 1
            current_time = task
            if workers > k:
                return False

    return True


def minimum_time(tasks, k):
    left = max(tasks)
    right = sum(tasks)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if can_finish(tasks, k, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


# Example usage
tasks = [1, 2, 4, 7, 8]
k = 2

result = minimum_time(tasks, k)
print(result)
