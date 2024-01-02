#[실습] 임의의 숫자 데이터 7개를 저장한 데이터를 생성, 리스트의 원소를 하나씩 출력하세요.

list= [1,2,5,4,7,8,6]
print(f'{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n{list[4]}\n{list[5]}\n{list[6]}')

#[실습] 리스트의 원소를 한 줄에 하나씩 출력하시오.
datas = [[10,20],[40,50],[70,80,90]]
print(f'{datas[0][0]}\n{datas[0][1]}')
print(f'{datas[1][0]}\n{datas[1][1]} ')
print(f'{datas[2][0]}\n{datas[2][1]}\n{datas[2][2]}')

#실습 좋아하는 계절과 월(month)입력, 각각 변수에 저장
default = input("좋아하는 계절과 월을 입력하시오: ")
default =default.split()
season = default[0]
month = default[1]

#[실습] 1-20으로 구성된 정수 리스트 생성
#               ->3의 배수 인덱스에 해당하는 정수 출력
#               ->3의 배수 인덱스에 해당하는 정수의 합 출력

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
three = num[::3]
all = three[0]+three[1]+three[2]+three[3]+three[4]+three[5]+three[6]

print(three)
print(all)