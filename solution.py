def cluster_timestamps(timestamps, k):
    if not timestamps:
        return []

    clusters = []
    current_cluster = [timestamps[0]]

    for i in range(1, len(timestamps)):
        if timestamps[i] - timestamps[i - 1] <= k:
            current_cluster.append(timestamps[i])
        else:
            clusters.append(current_cluster)
            current_cluster = [timestamps[i]]

    clusters.append(current_cluster)
    return clusters


# Example usage
timestamps = [10, 15, 18, 40, 42, 90]
k = 5

result = cluster_timestamps(timestamps, k)
print(result)
