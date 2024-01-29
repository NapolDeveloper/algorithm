import sys

N = int(input())

arr = list(sys.stdin.readline())

result = 0
for i in range(N):
  result = result + int(arr[i])
  
  
print(result)