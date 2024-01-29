import sys

T = int(input())

numbers = list(map(int, sys.stdin.readline().split()))


print(min(numbers), max(numbers))