# [while]

# 사용자가 알고 싶어하는 단을 입력받아 해당 단의 구구단 출력하기; while 사용
stop = False
while stop:
    dan = int(input("단 입력: "))
    num =2
    print(f'{dan:-^9}')
    while num < 10:
        print(f'{dan} * {num} = {dan * num}')
        num +=1


# 2 - 9단 출력하기; while 사용

dan, unit= 2, "단"
num = 2
while dan <10:
    print(f'{dan:->4} {unit:-<4}')
    num = 1 #두 번째 while문에서 빠져나왔을 때 num값 초기화
    while num<10:
        print(f'{dan} * {num} = {dan * num}')
        num+=1
    dan+=1