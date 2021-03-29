# 지금까지 배운 내용
areas = []
for i in range(1, 11):
    if i % 2 == 0:
        areas = areas + [i * i]
print('areas', areas)

# list_comprehension
# [ 계산식 for문 ]
# [ 계산식 for문 조건문 ]
# [ 계산식 for문 for문 ]

# 길이가 1~10 인 정사각형의 넓이를 구하고 그 중에서 2의 배수를 구하는 방법
areas2 = [i*i for i in range(1, 11) if i % 2 == 0]
print('areas2', areas)

# 길이가 15 * 15 바둑판 만들기
section = [(x, y) for x in range(15) for y in range(15)]
print(section)

# 1부터 100 사이의 8의 배수를 구하는 법
list1 = [i for i in range(1, 101) if i % 8 == 0]
print(list1)
