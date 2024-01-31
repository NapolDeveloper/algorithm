# V = 나무 높이
# A = 아침에 올라가는 높이
# B = 저녁에 내려가는 높이
# 조건 = 정상에 올라간 후에는 미끄러지지 않음

# 올라가야할 거리 = V - B
# 하루에 갈 수 있는 거리 = A - B

A, B, V = map(int, input().split())
x = (V - B)/(A - B)

if x == int(x):
  print(int(x))
else:
  print(int(x) + 1)
