X = []
Y = []

N = int(input())

for i in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)

print((max(X)-min(X)) * (max(Y)-min(Y)))