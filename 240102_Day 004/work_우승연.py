#연습문제

x = 5
if x!=10:
    print("ok")

"""
표준 입력으로 가격(정수)과 쿠폰 이름이 각 줄에 입력됩니다.
cash3000 쿠폰은 3000원, cash5000쿠폰은 5000원을 할인합니다.'
쿠폰에 따라 할인된 가격을 출력하는 프로그램을 만드세요.
"""

cp = input("")
charge = int(input(""))

if cp == "Cash3000":
    charge = charge - 3000
    print(charge)
elif cp == "Cash5000":
    charge = charge - 5000
    print(charge)

print("-"*60)
#___________________________________________________________

kr = int(input(""))
eg = int(input(""))
mt = int(input(""))
si = int(input(""))

avg = (kr + eg + mt + si)/4

if kr and eg and mt and si<=100:
    if avg>=80:
        print("합격")
    elif avg<80:
        print("불합격")
else:
    print("잘못된 입력")

print("-"*60)
#--------------------------------------------------
#연습문제 15.3

x= int(input())
if 11<=x<=20:
    print("11~20")
elif 21<=x<=30:
    print('21~30')
else:
    print("아무것도 해당하지 않음")
"""
15.4
"""

age = int(input())
balance = 9000 #교통카드 잔액

if 7<=age <=12:
    balance = balance - 650
    print(balance)

elif 13<=age <=18:
    balance = balance - 1050
    print(balance)
elif age<=19:
    balance = balance-1250
    print(balance)