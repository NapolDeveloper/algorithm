T = []

for i in range(3):
  a = int(input())
  T.append(a)

a = T[0]
b = T[1]
c = T[2]

if sum(T) == 180:
  if a == 60 and b == 60 and c == 60:
    print("Equilateral")
  elif a == b or b == c or c == a:
    print("Isosceles")
  else:
    print("Scalene")   
else:
  print("Error")

