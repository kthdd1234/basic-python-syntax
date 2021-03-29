def return_false():
    print('함수return_false')
    return False


def return_true():
    print('함수return_true')
    return True


print('테스트1')
a = return_false()
b = return_true()

if a and b:
    print(True)
else:
    print(False)

# vs

# 단락평가: 논리연산에서 코드의 앞만 보고 값을 정할 수 있는 경우 뒤는 보지 않고 값을 결정
# 복잡한 코드를 단순하게 하는 방식
print('테스트2')
if return_false() and return_true():
    print('True')
else:
    print(False)
