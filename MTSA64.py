n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
merged = []
i = j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1
merged.extend(arr1[i:])
merged.extend(arr2[j:])
total = len(merged)
if total % 2:
    median=(merged[total // 2])
else:
    median = (merged[(total // 2 )- 1] + merged[total // 2]) / 2
print(f"{median:.1f}")
