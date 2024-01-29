import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i for i in range(1, N+1)]

temp = 0

for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  temp = basket[j-1]
  basket[j-1] = basket[i-1]
  basket[i-1] = temp

for i in range(N):
  print(basket[i], end=" ")

