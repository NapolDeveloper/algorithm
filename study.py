print(range(10))

# 앞에 *을 붙이면 Unpacking
print(*range(10)) # 0 1 2 3 4 5 6 7 8 9

num1 = 1
# str(num1), float(num1), int(num1)과 같이 형변환 가능


# sep를 통해 문자 사이에 특정 값을 넣을 수 있다.
arr1 = range(1, 5+1)
print(*arr1, sep="\n")
# 1
# 2
# 3
# 4
# 5

# end를 통해 문자 끝마다 값을 추가할 수 있다.
arr2 = [1, 2, 3, 4, 5]
for a in arr2:
    print(a, end= " and ") # 1 and 2 and 3 and 4 and 5 and 


