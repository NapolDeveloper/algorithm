
n = []

for _ in range(10):
  a = int(input())
  b = a % 42
  n.append(b)
  
c = set(n)
print(len(c))