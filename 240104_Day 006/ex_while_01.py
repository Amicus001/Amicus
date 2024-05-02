#반복문: while
# 반복할 횟수가 정해지지 않은 경우 사용(정해져 있는 경우에도 사용은 가능)
# =========================================================
# 사용자로부터 좋아하는 음식명을 입력받기; '끝' 입력 전까지.(종료 시점 미정)
favfood = []
cnt = 1
while cnt<6:
    f = input("좋아하는 음식:")
    favfood.append(f)
    cnt = cnt+1

#타이머 프로그램 만들기: 다운카운팅(거꾸로 세기)
downcount = 10
while downcount>0:
    print(f' downcounting {downcount}')
    downcount = downcount-1 #downcount-=1, 복합연산자

for a in range(10,1,-1):
    print(f' downcounting {a}')



#타이머 프로그램 만들기: 업카운팅
upcount = 1
while upcount < 11:
    print(f'upcounting {upcount}')
    upcount +=1

for b in range(1,11):
    print(f'upcounting {b}')
DEBUG = False#flag 변수
if DEBUG:
    # 사용자로부터 좋아하는 음식명을 입력받기; 5개만.
    food = input("음식")
    foodlist = []
    # for f in foodlist:
    #     foodlist.append(food)
    #     print(f'top 5: {foodlist}')
    ffood = []
    for count in range(5):
        food = input((f'{count+1}번째 좋아하는 음식: '))
        ffood.append(food)

    # 출력
    print("you like", end= '')
    for food in ffood:
        print(food, end=', ' if food[-1] != food else ' ')
    foodstr = ""
    for cnt in range(5):
        food = input(f'{cnt+1}번째 좋아하는 음식: ')
        foodstr = foodstr + food +( " , " if cnt!= 5 else ' ')
    print(f'foods = {foodstr}')