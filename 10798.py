table = []
resultTable = []

max_len = 0

# 테이블 생성
for i in range(5):
  table = list(map(str, input()))
  resultTable.append(table)
  if max_len < len(table):
      max_len = len(table)

for j in range(max_len):
  for i in range(5):
    if len(resultTable[i]) > 0:
      print(resultTable[i][0], end="")
      resultTable[i].pop(0)
    else:
      continue