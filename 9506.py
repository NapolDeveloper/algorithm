

while True:
  n = int(input())
  arr = []
  result = 0
  if n == -1:
    break
  
  # 배열에 약수 목록 넣기
  for i in range(1, n):
    if n % i == 0:
      arr.append(i)
      
  if sum(arr) == n:
    print(n, " = ", " + ".join(str(i) for i in arr), sep="")
  else:
    print(n, "is NOT perfect.")