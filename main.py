import math

arr = [1.0, 1.0, 6.0, 4,0]
result = 0
i = 0
while True:
    result += arr[i]
    if i >= len(arr) - 1:
        break
    i += 1

print(result)
