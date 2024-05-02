#[실습] 알고 싶은 구구단 단을 입력받고 해당 단을 출력하기
#input()
#특정 단의 구구단 출력

# num = int(input("출력한 단을 입력하시오: "))
# if num:
#     for x in range(1,10):
#         print(f'{num} * {x} = {num*x}')
# else:
#     print("잘못된 데이터")
#
# num = int(input("출력한 단을 입력하시오: "))
# if num:
#     for x in range(9,0,-1):
#         print(f'{num} * {x} = {num*x}')
# else:
#     print("잘못된 데이터")
#
# # ===========================================
# #[실습2] 2-9단까지, 반복문
# # ===========================================
#
# for x in range(2,10):
#     for y in range(2,10):
#         print(f'{x} * {y} = {x*y}')
#
# print("="*60)

for y in range(1, 10):
    for x in range(2, 10):
            print(f'{x} * {y} = {x * y:<2}', end="\n"if x==9 else '   ')
    print("")




