#_*_coding:cp949
sum_square = 0
square_sum = 0
for a in range(1,101) :
# for문 1부터  100까지
    sum_square = sum_square + a
    square_sum = square_sum + a * a
sum_square = sum_square * sum_square
print "sum_square = ", sum_square
print "square_sum = ", square_sum
difference = sum_square - square_sum
print "sum_square - square_sum = " ,difference

 

#합들의 제곱은 25502500

#제곱들의 합은 338350

#따라서 두 값의 차는 25164150입니다.
