word = input().upper()
unique = list(set(word))
countList = []

for i in unique:
  countList.append(word.count(i))  

if countList.count(max(countList)) > 1:
  print("?")
else:
  maxIndex = countList.index(max(countList))
  print(unique[maxIndex])