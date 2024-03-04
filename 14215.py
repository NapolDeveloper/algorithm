<<<<<<< HEAD
a, b, c = list(map(int, input().split()))

if a == b == c:
  print(a*3)
else:
  
=======
arr = list(map(int, input().split()))
arr.sort()

result = arr[0] + arr[1] + min(arr[2], arr[0] + arr[1] - 1)
print(result)
>>>>>>> 0042392a61f3c70bc53e8e3bdd62fc96775e31e3
