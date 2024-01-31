inputNum = input().split(' ')
numbers = [int(i) for i in inputNum]
A = numbers[0]
B = numbers[1]

if A > B:
  print('>')
elif A < B:
  print('<')
else:
  print('==')
  