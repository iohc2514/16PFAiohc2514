#_*_coding:cp949
people = 50
cars = 40
trucks = 15
# ���� ����

if cars > people :
    print "We should take the cars."
elif cars < people :
    print "We should not take the cars."
else:
    print"We can't decide."
# elif ���� ���� ���� else �Ѱ��� ����
# if �̰Ϳ� �ش�Ǹ� ����>  NO �ϰ�� �̰Ϳ� �ش�Ǹ� elif > �׷��� NO�� ���else
if trucks > cars  :
    print" That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."
# if �̰Ϳ� �ش�Ǹ� ����>  NO �ϰ�� �̰Ϳ� �ش�Ǹ� elif > �׷��� NO�� ���else
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."