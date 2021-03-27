list1 = [1, 2, 3, 4, 5]
print(list1)

list1.append(6)  # list2.push() 와 같음

# list2은 그대로 두고, 새로운 리스트를 만들어 낸다.
list2 = list1 + [7]
print(list2)

list3 = list1 + list2
print(list3)

# in 연산을 이용
n = 15
ownership = n in list3
print('리스트에 n 값이 들어있는지 확인하는 방법: ', ownership)

# 리스트에서 필요 없는 값을 지우는 방법
del list1[4]
print(list1)

list3.remove(2)
print(list3)
