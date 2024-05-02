#29.7 연습문제
x = 10
y = 3

def get_quotient_remainder(a,b):
    return a//b, a%b
quotient, remainder = get_quotient_remainder(x,y)
print('몫:', quotient, '나머지:', {remainder}.format(quotient,remainder))

#30.6 연습문제
korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*args):
    return max(args)
max_score = get_max_score(korean,english, mathematics, science)
print ("높은 점수", max_score)