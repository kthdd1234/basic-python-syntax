# Slice: 리스트나 문자열에서 값을 여러개 가져오는 기능
# slice 를 하면 해당하는 부분의 리스트나 문자열을 새로 만들어 준다.

# 문자열
text = 'Harry Kane'
print(text[1:5])

# 리스트
list1 = ['one', 'two', 'three', 'four', 'five']
print(list1[2:4])

# 2번째부터 끝까지 반환
list2 = list1[2:]
print(list2)

# 처음부터 2번째까지 반환
list3 = list1[:2]
print(list3)

# 처음부터 끝까지 전부 반환
lists = list1[:]
print(lists)

# slice 의 step: slice 한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능
# 문자열도 똑같이 적용됨
new_list = list(range(20))
print(new_list[5:15])

# 2칸씩 건너뜀
print(new_list[5:15:2])

# 3칸씩 건너뜀
print(new_list[5:15:3])

# 처음부터 끝까지 3칸씩 건너뜀
print(new_list[::3])

# 끝에서 처음까지 -3칸씩 건너뜀
print(new_list[::-3])

# 반대로 가져오면서 -4칸씩 건너뜀
print(new_list[17:4:-4])

# slice 로 리스트 수정하기
numbers = list(range(20))
numbers[1:3] = [50, 90]
print(numbers)

# 처음부터 3까지 삭제
del numbers[:3]
print(numbers)

# 더 많은 갯수로 변환
numbers[1:3] = [50, 90, 77, 88]
print(numbers)

# 더 적은 갯수로 변환
numbers[1:5] = [1, 2]
print(numbers)
