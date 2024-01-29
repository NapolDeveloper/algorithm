import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  # 배열 슬라이싱
  temp = basket[i-1:j]
  # 배열 역순
  temp.reverse()
  # 해당 범위에 temp 배열 넣어주기
  basket[i-1:j] = temp

for i in range(N):
  print(basket[i], end=' ')