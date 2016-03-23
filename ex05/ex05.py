#-*-coding:cp949
my_name = 'Seokhyeon Choi'
my_age = 23 # not a lie
my_height = 164.5 # cm
cm_to_inch = 1.0 / 2.54
my_height_inch = my_height *cm_to_inch
my_weight = 63 # kg
my_eyes = 'brown'
my_teeth = 'White'
my_hair = 'black'
# %g=소수점 까지%d=정수
print "Let's talk about %s." % my_name
print "He's %g cm tall." % my_height
print "He's %g inches tall." %my_height_inch
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age  + my_height + my_weight )