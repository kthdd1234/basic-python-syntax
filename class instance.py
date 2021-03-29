# 클래스(class): 함수나 변수들을 모아 놓은 집합체
# 인스턴스(instance): 클래스에 의해 생성된 객체, 인스턴스 각자 자신의 값을 가지고 있다.

numbers1 = []
numbers2 = list(range(10))

characters = list('Harry')
print(characters)

numbers1 == list  # 같지 않음

# 클래스 만들기
# 클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 이해하기 쉽게 포장할 수 있다.


class Human():
    """person"""


def speak(person):
    print('{}이 {}로 말을 합니다.'.format(person.name, person.language))


person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'

print(person1.language)
print(person2.language)

person1.name = '손흥민'
person2.name = 'Harry Kane'

Human.speak = speak
person1.speak()
person2.speak()
