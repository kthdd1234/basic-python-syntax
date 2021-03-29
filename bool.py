bool(0)  # False
bool(1)  # True
bool(-1)  # True
bool([])  # False
bool([3])  # True
bool(None)  # False
bool('')  # False
bool('hi')  # True

# 숫자 0을 제외한 모든 수 - True
# 빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 - True
# 아무 값도 없다는 의미인 None - fasle
# 빈 문자열을 제외한 모든 문자열 - True
value = input('입력해주세요>') or '아무것도 못받았어'
print('입력받은 값>', value)
