#리스트의 원소(요소) 데이터 변경/삭제
a = list("Merry Christmas")
print(a)
#공백을 ***로 변경
a[5] = '***'
print(a)

#리스트 요소 삭제; del(data)/del data
del a[5]
print(a)

del(a[5])
print(a)