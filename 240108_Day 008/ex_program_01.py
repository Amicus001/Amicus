#-----------------------------------------------------
# 나의 프로그램: 계산기
# [계산기]
# 입력
# 덧셈
# 뺄셈
# 곱셈
# 나눗셈
# 종료
# ---------------------------------------------------
# -사용자 정의 함수--------------------------------------
# - 기능: 연산 결과 리스트에서 검색어에 해당하는 데이터만 출력
# - 이름: searchResult
# - 매개변수: search
# - 결과: none
#----------------------------------------------------
#계산 기록 저장용 전역 변수 선언

def searchResult(search):
    cnt = 0
    for calc in calcList:
        if search in calc:
            print(calc)
            cnt+=1
    print(f'{cnt}개의 검색 결과 발견' if cnt else '검색 결과 없음')

calcList = []

while True:
    print("==계산기==")
    print("1. 입력")
    print("2. 덧셈")
    print("3. 뺄셈")
    print("4. 곱셈")
    print("5. 나눗셈")
    print("6. 검색")
    print("7. 삭제")
    print("8. 기록 보기")
    print("9. 종료")
    choice = input("메뉴 선택")
    if choice.isdecimal():
        if choice == '1':
            data = input("2개의 정수를 입력하세요")
            n1, n2 = list(map(int, data.split()))
        elif choice == '2':
            calcList.append(f'{n1}+{n2}= {n1+n2}')
            print(f'{calcList[-1]}\n')
        elif choice == '3':
            calcList.append(f'{n1}-{n2}= {n1-n2}')
            print(f'{calcList[-1]}\n')
        elif choice == '4':
            calcList.append(f'{n1}*{n2}= {n1*n2}')
            print(f'{calcList[-1]}\n')
        elif choice == '5':
            calcList.append(f'{n1}/{n2}= {n1/n2 if n2 else "0으로 나눌 수 없음"}')
            print(f'{calcList[-1]}\n')
        elif choice == '6':
            print(f'계산 기록 출력')
            calcList.sort(reverse= True)
            for calc in calcList:
                print(calc)
        elif choice == '7':
            search = input("검색: ")
            searchResult(search)

        elif choice == '8':
            calcList.clear()
            print("모든 계산 기록이 삭제됨.")
        elif choice == '9':
            print("종료합니다.")
            break
        else:
            "1에서 6까지의 숫자를 선택하세요. "
    else:
        print("잘못된 접근입니다.")