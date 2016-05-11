#_*_coding:cp949
people = 50
cars = 40
trucks = 15
# 변수 저장

if cars > people :
    print "We should take the cars."
elif cars < people :
    print "We should not take the cars."
else:
    print"We can't decide."
# elif 갯수 제한 없음 else 한개만 가능
# if 이것에 해당되면 ㄱㄱ>  NO 일경우 이것에 해당되면 elif > 그래도 NO일 경우else
if trucks > cars  :
    print" That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."
# if 이것에 해당되면 ㄱㄱ>  NO 일경우 이것에 해당되면 elif > 그래도 NO일 경우else
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."