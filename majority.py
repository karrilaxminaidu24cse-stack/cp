def majorityElement(arr):
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    count = 0
    for num in arr:
        if num == candidate:
            count += 1
    if count > len(arr) // 2:
        return candidate
    return -1
n = int(raw_input())
arr = map(int, raw_input().split())
print majorityElement(arr)
