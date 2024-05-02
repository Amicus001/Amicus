#함수의 형태 2: 반환값이 없는 함수

#두 개의 정수를 덧셈 후 출력

def addtwo(x,y):
    value = x + y
    print(f'{x}+{y} = {x+y}')
#
#함수 사용(호출)

#함수 호출 시 매개변수 갯수만큼 데이터를 전달해야 한다.
addtwo(11,5)
addtwo(11,0)

#영단어를 입력받아 모두 대문자로 변환하는 기능
#함수이름: capital
#매개변수: word
#반환값 없긔. -> 일 안 함-> return 해야 함.

def capital(word):
    word = word.upper()

#시퀀스 객체의 모든 원소를 대문자로 변환하는 기능
#함수이름: capital2
#매개변수: str타입의 원소로 구성된 list
#반환값 없긔.

def capital2(wordlist):
    wlist = []
    for idx in range(len(wordlist)):
        wordlist[idx] = wordlist[idx].upper()

    #for idx,data in enumerate(wordlist):
        #datalist[idx] = data.upper

datas = ['apple', 'banana', 'orange']
for data in datas:
    print(f' before = {data}, after = {data.upper()}')

print (datas)