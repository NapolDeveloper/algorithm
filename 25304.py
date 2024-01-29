totalPrice = int(input())

itemCount = int(input())

result = 0

for i in range(itemCount):
    itemData = input().split(' ')
    itemPrice, itemC = [int(x) for x in itemData]
    result += itemPrice * itemC
    

if totalPrice == result:
    print('Yes')
else:
    print('No')