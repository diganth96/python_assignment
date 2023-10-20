def count_pairs_with_sum(arr, k):
    num_count = {}
    pair_count = 0
    for num in arr:
        complement = k - num
        if complement in num_count:
            pair_count += num_count[complement]
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    return pair_count // 2
arr = [1, 2, 3, 4, 5]
k = 6
pair_count = count_pairs_with_sum(arr, k)
print("Pair count:", pair_count)