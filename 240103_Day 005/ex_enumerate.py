#for 요소 in 시퀀스(반복가능객체):
#   -> for index in range(len(variable))
#   => 내장함수 enumerate(): (번호, 요소) < 튜플형으로 반환

datas = ['apple', 'banana', 'orange']

#리스트 안의 요소만 데이터 추출
for data in datas:
    print(data)

#리스트 안의 요소(원소) 인덱스, 데이터 추출
for data in enumerate(datas):
    print(data)

x = ['std01', 'std02', 'std03']
y = [100, 200, 300]

mydict = {}
for data in enumerate(x):
    #(0,'std01')
    mydict[data[1]] = y[data[0]]
print(mydict)

mydict2 = {}
for idx, key in enumerate(x):
    mydict2[key] = y[idx]