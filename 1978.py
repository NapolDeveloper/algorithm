N = int(input())

result = 0

T = list(map(int, input().split()))

for i in range(0, N):
  arr = []
  for j in range (1, T[i]+1):
     if T[i] % j == 0:
       arr.append(j)
       
  if len(arr) == 2:
    result += 1
  else:
    continue
  
print(result)