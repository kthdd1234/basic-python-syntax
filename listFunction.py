# List 의 다양한 기능들
list1 = [135, 22, 11, 51, 235]

# list.index(value): 값을 이용하여 위치를 찾는 기능
idx = list1.index(11)
print(idx)

# list.extend([val1, val2, ...]): 리스트 뒤에 값을 추가
list2 = [6, 1, 2]
list1.extend(list2)
print(list1)

# list.insert(index, value): 원하는 위치에 값을 추가
list1.insert(2, 19)
print(list1)
list1.insert(-1, 120)
print(list1)

# list1.sort(): 값을 순서대로 정렬
list1.sort()
print(list1)

# list1.reverse(): 값을 역순으로 정렬
list1.reverse()
print(list1)
