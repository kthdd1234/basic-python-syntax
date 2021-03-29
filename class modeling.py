# 모델링(modeling): 클래스로 현실의 개념을 표현하는 것
class Human():
    '''인간'''


def create_human(name, food, weight):
    person = Human()
    person.name = name
    person.food = food
    person.weight = weight
    return person


Human.create = create_human
person = create_human('흥민이', '짬뽕', 60.5)


def eat(person):
    person.weight += 0.1
    print('{}가 {}을 먹어서 {}kg이 되었습니다'.format(
        person.name, person.food, person.weight))


def exercise(person):
    person.weight -= 0.1
    print('{}가 운동을 해서 {}kg이 되었습니다'.format(
        person.name, person.weight))


Human.eat = eat
Human.exercise = exercise

person.eat()
person.exercise()
