#-*-coding:cp949
x ="There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who konw %s and those who %s." % (binary, do_not)
# 1,4���� x���������� �ϸ鼭 �����þȿ� ���ڸ� �����ߴ�. 2,3���� �ܾ� ������
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e