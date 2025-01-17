#return keyword:
# 함수를 호출한 곳으로 돌아가게 하는 기능: 결과값이 함께 있다면 결과값을 가지고 돌아간다.
# ------------
#def function name(variable 1,2,3, ,,)
#    condition code, return
#    code
#    code
#    return result

def factorial(x):
    if not x:
        return 1 #즉시 함수 종료 후 호출한 곳으로 반환. 값이 없으면 'none'를 가지고 돌아온다. 
    ret=1
    if x:
        for n in range(x, 0, -1):
            ret *= n
        return ret

print(f'0! = {factorial (0)}')
print(f'3! = {factorial (3)}')