a = input().split(' ')
x, y, z = [int(i) for i in a]

if x == y == z:
  print(10000 + (x * 1000))
elif x != y and x != z and y != z:
  print(max([x,y,z]) * 100)
else:
  if x == y:
    print(1000 + (x) * 100)
  elif y == z:
    print(1000 + (y) * 100)
  else: 
    print(1000 + (x) * 100)

