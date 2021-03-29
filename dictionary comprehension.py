students = ['태연', '진우', '정현', '하늘', '성진']

for number, name in enumerate(students):
    print('{}번의 이름은 {}입니다.'.format(number + 1, name))

students_dict = {"{}번".format(
    number + 1): name for number, name in enumerate(students)}

print(students_dict)

scores = [89, 100, 12, 29, 90]

for x, y in zip(students, scores):
    print(x, y)


score_dict = {student: score for student, score in zip(students, scores)}
print(score_dict)
