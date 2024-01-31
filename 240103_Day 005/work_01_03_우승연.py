# hello world 100회 출력하기
for a in range(100):
    print("Hello world!" * a)

# range에서 꺼낸 숫자를 함께 출력하기
for i in range(100):
    print("hello world!", i)

# 증가폭 사용하기
for s in range(1, 12,2):
    print("hi!", s)

#숫자 감소
for l in range(10, 1):
    print("ho!", l)

#시퀀스 객체 반복
k = [10,20,30,40, 50]
for c in k:
    print(c)

#16.5 연습문제
x = [49, -17, 25, 102, 8, 62, 21]
for y in x:
    print( y* 10)

#16. 심사문제
num = int(input())
if num:
    for gugudan in range(2,10):
        print(f'{num} * {gugudan} = {num * gugudan }')


#19. 별 출력
#19-1. 사각형 별 출력
for j in range(5):
    print("*", end= '')

#19-2. 대각선 별 출력

for k in range(5):
    for m in range(5):
        if k==m:
            print("*", end= ' ')
        else:
            print(" ")

#19.5 역삼각형으로 별 출력하기
for v in range(5,1,-1):
    print('*' * v)

#19.6  산 모양으로 별 출력하기***

for a in range(1, 10,):
    print(" "* (9-a), end="")
    print("*"* (a*2-1))

#22. 3 for 반복문으로 요소 출력학

yoso = [38,21,53,62,19]
for o in yoso:
    print(o)

#22.3.2 인덱스와 요소 함께 출력하기
aa = [38, 21, 53, 62, 19]
for index, value in enumerate(aa):
    print(index, value)

#22.6 리스트에 map 사용하기
mm = list(map(str,range(10)))
print(a)

#22.9 연습문제
aaa = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b= [aaa for aaa in aaa if len(i) ==5]

#22.10 심사문제 list comprehension
#예외 조건 나중에 생각하기

first = int(input("정수 입력(1~20):"))
second = int(input("정수 입력(10~30):"))


stairs = [2 ** ff for ff in range(first, second+1) if  ff !=first+1 and ff!=second -1]
print(stairs)