import sys

# 맨 첫줄 테스트 케이스를 입력 받을때는 input()을 사용해도됨.
# 반복문으로 여러줄 입력받는 상황에서는 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않음.

n = int(input())

for i in range(n):
  a,b = map(int, sys.stdin.readline().split())
  print(a+b)