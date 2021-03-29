# 오버라이드(Override): 같은 이름을 가진 메소드를 덮어 쓴다는 의미
class Animal():
    def greet(self):
        print('인사한다.')


class Human(Animal):
    def wave(self):
        print('손을 흔든다.')

    def greet(self):
        self.wave()


class Dog(Animal):
    def wag(self):
        print('꼬리를 흔든다.')

    def greet(self):
        self.wag()


class Cow(Animal):
    '''소'''


person = Human()
person.greet()

dog = Dog()
dog.greet()

cow = Cow()
cow.greet()
