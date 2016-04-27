#_*_coding:cp949
from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()
# read 파일 내용 읽기

def rewind(f):
    f.seek(0)
# 파일을 처믐 위치로 되돌리기

def print_a_line(line_count, f):
    print ("%d %s" % (line_count, f.readline()))

current_file = open(input_file)

print "First let's print the whole file:굈"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
