list1 = [1, 2, 3, 4, 5]
print(list1)

# 자바스크립트의 list2.push() 와 같은 기능: 리스트에 값을 추가
list1.append(6)

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

# pop
result = list3.pop(2)
print(result)

# 전부 삭제
list1.clear()

# break: 반복문을 종료시키는 기능
lists = [1, 2, 3, 5, 7, 2, 5, 237, 55, 22]

for value in lists:
    if value % 3 == 0:
        print(value)
        break

# continue: 반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    print(i)
    print(i)
    print(i)
