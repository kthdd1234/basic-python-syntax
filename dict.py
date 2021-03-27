# 딕셔너리 수정하기
dicts = {
    'one': 1,
    'two': 2,
    'three': 3
}
# 추가
dicts['four'] = 4

# 수정
dicts['one'] = 11

# 삭제
del(dicts['one'])
dicts.pop('two')

# 딕셔너리 반복문
goals = {'Kane': 35, 'Son': 17, 'Moura': 10}

for key in goals.keys():
    print(key)

for value in goals.values():
    print(value)

for key, value in goals.items():
    print('{}가 넣은 골수는 {}입니다.'.format(key, value))
