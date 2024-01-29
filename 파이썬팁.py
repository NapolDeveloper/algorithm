from collections import deque

# 문자열 뒤집기
string = 'Hello, World!'
print(string[::-1])

# 중복 제거하기
# set함수는 중복을 제거한다. 단 주의할 점으로 순서가 없다.
arr1 = [1, 2, 1, 3, 4, 5, 4, 2]
print(list(set(arr1)))

# 한 줄에 여러 정수(int), 실수(float) 입력받기
# arr2 = list(map(int, input().split()))
# print(arr2)

# 특정 값으로 2차원 배열(BFS, DFS에서 주로 사용) 생성하기
m = 4
n = 3
# 4 x 3 크기의 배열 만들기. 초기값은 0
visited = [[0 for _ in range(m)] for _ in range(n)]
print(visited)

# 조건문 (0 < m and m < 10)과 같이 쓰지 않아도됨
if 0 < m < 10:
  print("조건문")
  
# 두 변수 바꾸기
# temp 변수를 사용하지 않아도됨
# a, b = b, a

# 리스트의 원소들을 차례로 순회할 때, 인덱스까지 동시에 가져오기
arr3 = ['k', 'o', 'r', 'e', 'a']
for idx, value in enumerate(arr3):
  print(idx, value)
  
# Queue를 이용할 시 temp.pop(0) 대신 deque사용하기. (*필수*)
# deque는 시간복잡도가 O(1)이다. 
queue = deque([1, 2, 3, 4, 5])
print(queue.popleft())
print(list(queue))

# 길이가 같은 두 개 이상의 iterable 객체를 동시에 for문 돌리기
arr4 = [1, 3, 5]
arr5 = [2, 4, 6]
for n1, n2 in zip(arr4, arr5):
  print(n1, n2)


# 딕셔너리 정렬 (key기준, value기준)
dict_a = {'파이썬': 1, '자바': 2, '자바스크립트': 3, '씨': 4}
sorted_dict = sorted(dict_a.items())
print(sorted_dict)

# 키 값만 뽑아서 정렬
sorted_dict = sorted(dict_a)
print(sorted_dict)

