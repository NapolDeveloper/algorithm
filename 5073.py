while True:
  T = list(map(int, input().split()))
  a = T[0]
  b = T[1]
  c = T[2]

  # 종료 조건
  if a == 0 and b == 0 and c == 0:
    break

  # 예외 조건
  if max(T) >= sum(T)-max(T):
    print("Invalid")
  elif a == b == c:
    print("Equilateral")
  elif a != b and a != c and b != c:
    print("Scalene")
  else:
    print("Isosceles")
  
  


