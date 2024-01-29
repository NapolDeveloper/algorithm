chess = [1, 1, 2, 2, 2, 8]

T = list(map(int, input().split()))

for i in range(len(T)):
  print(chess[i] - T[i], end=" ")