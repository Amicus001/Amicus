#반복 횟수가 명확하지 않은 반복 while문 쓰기
#사용자가 'x'입력 전까지 입력받은 데이터 저장하기: 무한 반복


mylist = []
T = False
while T:
    insert = input("insert(x = end): ")
    mylist.append(insert)
    if insert in ('X', 'x'):
        break# < if 조건문이 만족하면 냅다 while문을 나가버림. 버릇없는새끼. 즉시 중단.
    print(mylist)

# 사용자로부터 x(X) 입력 전까지 정수를 입력함. 입력받은 정수만큼 알파벳 출력



# while True:
#     num = input("출력을 원하는 알파벳 수 입력: ")
#     #입력 무한 반복 종료 조건:
#     if num in("x", "X"):
#         break
#
#     num = int(num)
#     codea =
#     while
#
A = False
while A:
    cnt = input("출력할 알파벳 수: ")

    if cnt in ('x', "X"):
        print("종료")
        break

    if cnt.isdecimal():
        cnt = int(cnt)
        acode = ord('a')
        for a in range(cnt):
            a += acode
            print(f'a = {a}, {chr(a)}')
            if a ==ord('z'): break
    else:
        print("wrong data")

#====================================================

isEnd = False
for n in range(100):
    print(f'out ->{n}')
    if isEnd:
        print("종료")
        break
    for n2 in range(100):
        if n2>10:
            isEnd = True
            break
        print(f'in ->{n2}==>{n}번째')


number = 1
isEnd = False


while number<=100:
    #종료조건 검사
    if isEnd:
        print("종료")
        break
    print(f'number = {number}')
    break
    #내부(중첩)while
    number2 += 1
    while number2<=100:
        if number2>10:
            print("종료")
            break
        print(f'number2 => {number}==> {number}번째')
    number2+1