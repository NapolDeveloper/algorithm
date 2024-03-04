# 자연수 N의 분해합 N + 각 자리수.
# 자연수 M의 분해합이 N인 경우 M을 N의 생성자


# M 245
# N 245 + 11 = 256
# M은 N의 생성자

# 216 
# 198 생성자

# 198 + 18 = 216

T = int(input())

result = 0

for i in range(1, T + 1):
  nums = list(map(int, str(i)))
  result = sum(nums) + i
  if result == T:
    print(i)
    break
  if i == T:
    print(0)


