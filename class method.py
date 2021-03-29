# 메소드(Method): 메소드는 함수와 비슷하다, 클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수
# 인스턴스(person)에 아무런 매개변수를 넘겨주지 않았지만 잘 실행이 됨
# 그 이유는 인스턴스(person)가 eat 메서드에 자동으로 첫번째 매개변수인 self 에 자동으로 전달되기 때문이다.

class Human():
    '''인간'''

    # __init__ : 초기화 함수이며 인스턴스를 만들 때 실행되는 함수
    def __init__(self, name, food, weight):
        self.name = name
        self.food = food
        self.weight = weight

    # __str__ : 문자열화 함수이며 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
    def __str__(self):
        return "{}(몸무게 {}kg)".format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print('{}가 {}을 먹어서 {}kg이 되었습니다'.format(
            self.name, self.food, self.weight))

    def exercise(self):
        self.weight -= 0.1
        print('{}가 운동을 해서 {}kg이 되었습니다'.format(
            self.name, self.weight))

    def speak(self, message):
        print(message)


# person = Human.create_human('흥민이', '짬뽕', 60.5)
person = Human('흥민이', '짬뽕', 60.5)
person.eat()
person.exercise()
person.speak('안녕하세요.')

new_person = Human('해리 케인', '짜장면', 72.2)
print(new_person.name)
print(new_person.weight)
print(new_person)
