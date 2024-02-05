# 첫 번째 숫자가 두 번째 숫자의 약수
# 첫 번째 숫자가 두 번째 숫자의 배수
# 위 두 조건이 둘다 아님

while True:
  a, b = map(int, input().split())
  
  if a == 0 and b == 0:
    break
  
  if a > b and a % b == 0:
    print('multiple')
  elif b > a and b % a == 0:
    print('factor')
  else:
    print('neither')
