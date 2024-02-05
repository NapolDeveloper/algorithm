a = input().split(' `')
hour, min = [int(i) for i in a]

need = int(input())

if need + min >= 60:
  hour = hour + (need + min) // 60
  min = (need + min) % 60
  if hour >= 24:
    hour = hour % 24
    print(hour, min)
  else:
    print(hour, min)
else:
  print(hour, min + need)