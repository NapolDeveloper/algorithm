N = int(input())

longCount = N // 4

result = ''

for i in range(longCount):
  result += 'long '


print(result + 'int')