alphaArr = ["ABC", 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

T = list(map(str, input()))

result = 0

for i in range(len(T)):
  for j in alphaArr:
    if T[i] in j: 
      result = result + alphaArr.index(j)+3

print(result)
