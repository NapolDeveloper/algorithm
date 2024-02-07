arr = list(map(int, input().split()))
arr.sort()

result = arr[0] + arr[1] + min(arr[2], arr[0] + arr[1] - 1)
print(result)
