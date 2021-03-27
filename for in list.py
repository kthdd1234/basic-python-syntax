# for in 반복문: 순회할 리스트가 정해져 있을 때
tim = ['흥민', '케인', '모우라', '라멜라', '베르바인', '요리스', '주단테', '천서진']
for pattern in tim:
    print(pattern)

# for in range -> 필요한 만큼의 숫자를 만들어내는 유용한 기능: 순회할 횟수가 정해져 있을 때
for idx in range(5):
    print(idx)

# for in enumerate -> 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
for idx, name in enumerate(tim):
    print('{}번: {}'.format(idx + 1, name))

print(len(tim))
