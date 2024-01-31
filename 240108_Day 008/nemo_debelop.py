def makingsoulnumber(birthday):
      if birthday == 'E'or birthday =='e':
            birthday = "E"
            return birthday
      else:
            if birthday.isdecimal()!=True:
                  print("생년월일을 8자리 입력해 주세요.")
            else:
                  if len(birthday)==8: #입력된 생년월일이 8자리 숫자라면
                        birthday=map(int,list(birthday)) #생년월일을 한 글자씩 잘라서 정수 한 자리 8개의 리스트로 만들기
                        total = sum(birthday) # 리스트 원소 전체 더하기
                        if total>=22: #합이 22보다 크거나 같으면
                              card= total%10 #카드 값은 일의자리만 떼어 씀.
                        elif total<22: #합이 22보다 작으면
                              card = total #카드 값은 그대로.
                        return card #카드 숫자 리턴
                  else:
                        print("생년월일을 8자리 숫자로 입력하세요.")

filename = "cardnumber.txt"
with open(filename, mode='r', encoding='utf8')as f:
    line = None
    # line = f.readline()
    # a = line.split()
    # print(a)
    #
    keylist=[]
    valuelist=[]

    while line != '':
        line = f.readline()
        a = line.split( )
        if a != []:
            if a[0][1:].isdigit():
                keylist.append(a[0][1:])
            else:
                valuelist.append(a)
    cardDict = dict(zip(keylist,valuelist))
    print(cardDict)
    # while True:
    #     print ("✨✨✨✨✨✨✨Soul Number Maker✨✨✨✨✨✨✨✨")
    #     print()
    #     print()
    #     soulnumber = makingsoulnumber(input("생년월일을 8자리로 입력하세요(종료는 E): "))
    #     if soulnumber == 'E' or soulnumber=='e':
    #         really = input("🗝️🗝️정말로 종료하시겠습니까?(y/n)")
    #         if really == "y" or really=="Y":
    #             print("⌛소울 넘버 탐색기를 종료합니다.")
    #             print()
    #             break
