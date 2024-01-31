WIDTH = 100

# 도화지 
paper = [[0 for _ in range(WIDTH)] for _ in range(WIDTH)]

T = int(input())
result = 0

for _ in range(T):
  x, y = list(map(int, input().split()))
  for i in range(x, x+10):
    for j in range(y, y+10):
      paper[i][j] = 1

for i in range(WIDTH):
  result += paper[i].count(1)

print(result)