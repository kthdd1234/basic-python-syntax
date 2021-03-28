# 한번 정해진 순서를 바꿀 수 없다.
tuple1 = (1, 2, 3)
print(tuple1)

# 튜플은 값의 변경과 삭제가 불가능
list1 = [1, 2, 3]
tuple3 = tuple(list1)
print(tuple3)

# tuple1과 tuple2와 tuple3은 모두 같음
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3
list3 = [1, 2, 3]
tuple3 = tuple(list3)

if tuple1 == tuple2 == tuple3:
    print("tuple1과 tuple2와 tuple3은 모두 같습니다.")

# 튜플을 이용한 함수의 리턴값
lists = [1, 2, 3, 4, 5]
for a in enumerate(lists):
    print('{}번째 값: {}'.format(*a))

persons = {'Kane': 27, 'Son': 29, 'Moura': 30}
for a in persons.items():
    print('{}의 나이는:{}'.format(*a))
