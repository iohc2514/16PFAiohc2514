#-*-coding:cp949
x ="There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who konw %s and those who %s." % (binary, do_not)
# 1,4열은 x에포맷팅을 하면서 포맷팅안에 숫자를 대입했다. 2,3열을 단어 포맷팅
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