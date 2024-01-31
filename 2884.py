time = input().split(' ')
hour, min = [int(i) for i in time]


if min >= 45:
  print(hour, min - 45)
else:
  hour = hour - 1
  if hour < 0:
    hour = 23
  a = min - 45
  min = 60 + a
  print(hour, min)
