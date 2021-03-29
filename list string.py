# 리스트와 문자열은 유사하다.
# 서로 변환이 가능하다.
# str.split(): 문자열에서 리스트로 변환
# ' '.join(list): 리스트에서 문자열로 변환

str = 'Hello World'
str[0]
str[1]

check = 'W' in str
print(check)

idx = str.index('d')
print(idx)

characters = list('abcdef')
print(characters)

words = '손흥민과 케인은 영국 프리미어리그 토트넘 소속 팀 주전 공격수들이다.'
words_list = words.split()
print(words_list)

time_str = '10:35:27'
time_list = time_str.split(':')
print(time_list)

print(':'.join(time_list))
print(' '.join(words_list))
