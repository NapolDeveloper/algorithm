N = int(input())

result = 0
x = 2

for i in range(N):
  x = x + (x-1)

print(x * x)
