def multiply(a, b):
    result = 0
    while b > 0:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    return result
dividend = int(input())
divisor = int(input())
if dividend == -(2**31) and divisor == -1:
    print(2**31 - 1)
    exit()
negative = (dividend < 0) != (divisor < 0)
dvd = abs(dividend)
dvs = abs(divisor)
low, high = 0, dvd
ans = 0
while low <= high:
    mid = (low + high) // 2
    if multiply(mid, dvs) <= dvd:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
if negative:
    ans = -ans
print(ans)
