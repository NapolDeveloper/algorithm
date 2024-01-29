S = int(input())

for i in range(S):
  N, S = input().split()
  for j in range(len(S)):
    print(S[j]*int(N), end="")
  print("")
