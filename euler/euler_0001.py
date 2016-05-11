#_*_coding:cp949
#10보다 작은 자연수중 3과 5의 배수의 함음
#1000보다 작은 자연수 중 3과 5의 배수의 함
n=0
for i in range(1,1000) :
    n=n+1
    if 3*n   <=1000:
        print" %s " %(3*n)
    if 5*n <= 1000:
        print"%s"%(5*n)

print "3*n+5*n"


