def countingSort(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1
    for i in range(100):
        while count[i] > 0:
            print(i, end=" ")
            count[i] -= 1
n = int(input())
arr = list(map(int, input().split()))

countingSort(arr)
