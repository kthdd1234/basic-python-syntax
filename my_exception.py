# 예외 정의
# 사용자가 직접 예외처리를 하면 코드의 직관성을 높일 수 있다.
# 파일을 하나 만들어 예외를 정의
# Exception 클래스를 상속받아 만든다.

from UnexpectedRSPValue import UnexpectedRSPValue

value = '가'
try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print('에러가 발생했습니다.')
