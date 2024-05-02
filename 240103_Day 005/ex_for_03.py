# 실습 ===========================================
# 문자열 여러개와 실수 여러개를 입력 받기 = input() 사용
# 첫번째 입력 = key
# 두번째 입력 = value
# 딕셔너리 저장
# ===============================================
# data = input("문자열과 실수 여러개 입력: \n 문자열과 실수 동일한 갯수로 ")
#
# #입력 형식 맞는지 확인
#
# if "," in data:
#     key, value = data.split(",")
#     key = data[0].split( )# 문자열
#     value = data[1].split( ) # 실수
#     datadict = {}
#     if len(key) == len(value):
#         for num in range(len(key)):
#             datadict[key[num]] = float(value[num])
#         print(f'datadict = {datadict}')
# else:
#     print("정확한 형식이 아님.")
#
#===========================================
#내장함수 zip
# ==========================================

x = [1,2,3,4,5]
y = [11,22,33,44,55]
z = [111,222,333,444,555]

result = zip(x,y,z)

print(f'result = {type(result)},{list(result)}')

#====================================================

data1 = input("문자열, 정수")
if "," in data1:
    datalist = data1.split(',')
    strdata = datalist[1]
    floatdata = datalist[2]

    datadict = dict(zip(floatdata, strdata))
    print(datadict)
else:
    print("잘못된 입력입니다.")