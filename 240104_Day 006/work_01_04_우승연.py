# 17.5 변수 두 개 다르게 반복하기.
i = 2
j = 5
while i<=32 or j>=1:
    print(i,j)
    i *= 2
    j -= 1

# 17.6 심사문제; 교통카드 잔액 출력하기
current = int(input())
fee = 1350
charge = current - fee
while charge > 0:
    print(charge)
    charge = charge - fee
# 18.5 연습 문제: 3으로 끝나는 숫자만 출력하기
i = 0
while True:
    if i%10!=3:
        i+=1
        continue
    if i>73:
        break
    print(i, end= ' ')
    i+=1

print( )
#18-6. 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력.
start, stop = map(int, input().split()) #start =  1~200, stop =  10~200. start<<stop.
i = start
while True:
    if i%10 == 3:
        i+=1
        continue

    elif i > stop:
        break
    print(i, end=' ')
    i+=1

#20.2 fizzbuzz

for i in range(1,101):
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else: print (i)


for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else: print (i)

for i in range(1,101):
    print('fizz'* (i%3==0)+"'buzz"*(i%5==0)+'fizzbuzz'*i%15==0 or i)

#20.7 연습문제: 2배수= fizz, 11배수 buzz, 공배수 fizzbuzz
for i in range(1,101):
    if i%22==0:
        print('fizzbuzz')
    elif i%2==0:
        print("fizz")
    elif i%11==0:
        print("buzz")
    else:
        print(i)

#20. 8 심사문제: 정수 두 개 입력(입력1= 1 - 1000, 입력2= 10 - 1000, 입력1<입력2)
#              입력1 - 입력2 출력, 5배수= fizz, 7배수 = buzz, 공배수 = fizzbuzz

a = int(input( ))
b = int(input( ))

if a<b:
    for n in range(a,b+1):
        if n%35 == 0:
            print("fizzbuzz")
        elif n%5 == 0:
            print("fizz")
        elif n%7 == 0:
            print("buzz")
        else:
            print("n")
else:
    print("stop, wrong")