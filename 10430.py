n = input().split(' ')
numbers = [int(i) for i in n]
A = numbers[0]
B = numbers[1]
C = numbers[2]

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C) 
print(((A % C) * (B % C)) % C)