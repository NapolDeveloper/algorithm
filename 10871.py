import sys

N, X = map(int, sys.stdin.readline().split())

numbers = map(int, sys.stdin.readline().split())

for i in numbers:
  if i < X:
    print(i, end=" ")