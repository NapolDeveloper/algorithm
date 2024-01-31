Q = 25
D = 10
N = 5
P = 1

T = int(input())

for i in range(T):
  money = int(input())

  print(money//Q, end=' ')
  money = money % Q
  print(money//D, end=' ')
  money = money % D
  print(money//N, end=" ")
  money = money % N
  print(money//P)
  money = money % P

