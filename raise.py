# raise: 사용자가 직접 에러를 발생시키는 기능
# raise Exception
# 먾아 사용하면 코드를 읽기 어려워진다.

def rsp(mine, yours):
    # 가위바위보 승패를 판단하는 코드
    allowed = ['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError


try:
    rsp('가위', '바')
except ValueError:
    print('잘못된 값을 넣었습니다.')


school = {'1반': [172, 185, 198, 177], '2반': [165, 177, 167, 191]}
try:
    for class_number, students in school.items():
        for student in students:
            if student > 190:
                print(class_number, '반ㅇ 190을 넘는 학생이 있습니다.')
                raise StopIteration
except StopIteration:
    print('정상종료')
