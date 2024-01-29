T = list(input().split())

for i in range(len(T)):
  # 문자열을 뒤집는 방법 (슬라이싱 사용)
  count = T[i][::-1]
  T[i] = int(count)

print(max(T))