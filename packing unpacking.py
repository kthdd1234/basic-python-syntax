a, b = 1, 2
print(a)
print(b)

c = (3, 4)
print(c)

# unpacking: 패킹된 변수에서 여러개의 값을 꺼내오는 것
d, e = c
print(d)
print(e)

# packing: 하나의 변수에 여러개의 값을 넣는 것
f = d, e
print(f)

# x, y 값을 서로 변경
x = '케인'
y = '손흥민'

x, y = y, x
print(x)
print(y)

# 함수를 이용한 튜플 사용
# 함수의 리턴 값으로 여러 값을 전달 할 수 있다.


def tuple_func():
    return 1, 2


q, w = tuple_func()
print(q)
print(w)
