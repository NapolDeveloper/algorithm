import sys

T = int(input())

number_list = list(map(int, sys.stdin.readline().split()))

v = int(input())

# list.count(v) 배열에서 v값의 개수를 반환
print(number_list.count(v))