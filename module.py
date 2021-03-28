# 모듈은 미리 만들어진 코드를 가져와 쓰는 방법
# import <모듈이름>
# 사용: <모듈이름>.<모듈안의 구성요소>
# 검색할때는 왠만하면 python3 <module>, 공식문서 참고

import math
import random
import datetime

candidates = ['흥민', '케인', '모우라', '라멜라']

pi = math.pi
now = datetime.date.today()
person = random.choice(candidates)

print(pi)
print(now)
print(person)
