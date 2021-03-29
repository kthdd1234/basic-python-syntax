text = '100%'
try:
    # 에러가 발생할 가능성이 있는 코드
    number = int(text)
except ValueError:
    # 에러가 발생 했을 경우 처리할 코드
    print('{}는 숫자가 아니네요.'.format(text))


def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))
# 예외처리 대신 if else 를 사용할 수 있다.


safe_pop_print([1, 2, 3], 5)


# 예외 이름을 모르는 경우 처리 방법
try:
    # 에러가 발생할 가능성이 있는 코드
    text = 'abc'
    number = int(text)
except Exception as ex:  # 에러 종류
    print('에러가 발생 했습니다.', ex)  # ex 는 발생한 에러의 이름을 받아오는 변수
