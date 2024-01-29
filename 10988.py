arr = list(map(str, input()))
reverseArr = list(reversed(arr))

result = '1'

for i in range(len(arr)):
  if arr[i] != reverseArr[i]:
    result = '0'
    break
    
print(result)