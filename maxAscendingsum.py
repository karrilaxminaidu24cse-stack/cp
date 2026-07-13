def maxAscendingSum(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_sum += arr[i]
        else:
            current_sum = arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
n = int(raw_input())
arr = map(int, raw_input().split())

print maxAscendingSum(arr)
