# 딕셔너리 수정하기
dicts = {
    'one': 1,
    'two': 2,
    'three': 3
}

# 갯수 확인
len(dicts)

# 추가
dicts['four'] = 4

# 수정
dicts['one'] = 11

# 삭제
del(dicts['one'])
dicts.pop('two')

# pop : 인자로 넣은 key 의 value 를 반환
pop = dicts.pop('three')
print('pop:', pop)

# 딕셔너리 반복문
goals = {'Kane': 35, 'Son': 17, 'Moura': 10}

for key in goals.keys():
    print(key)

for value in goals.values():
    print(value)

for key, value in goals.items():
    print('{}가 넣은 골수는 {}입니다.'.format(key, value))

# 값 확인
check = 'Son' in goals.keys()
print(check)

# 결합
dicts.update(goals)
print(dicts)

# 전부 삭제
dicts.clear()
