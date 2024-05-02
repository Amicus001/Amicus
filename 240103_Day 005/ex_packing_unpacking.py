#패킹과 언패킹

msg = "Happy new year"

#packing
msglist = msg.split()
print(msglist[0], msglist[-1])


#unpacking
m1, m2, m3 = msg.split()
print(m1,m2,m3)


#변수를 여러 개 생성하는 경우
age = 12
name = "Hong"
job = "student"

#튜플을 언패킹으로 생성가능
age1, name1, job1 = 12, "Hong", "student"

