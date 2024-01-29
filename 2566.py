table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0

col = 0
row = 0

for i in range(9):
  for j in range(9):
    if max_num < table[i][j]:
      max_num = table[i][j]
      col = i
      row = j
      
print(max_num)
print(col+1, row+1)