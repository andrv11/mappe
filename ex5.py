name = 'Andreas Vangstad'
age = 21 # not a lie
height_inches = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = height_inches * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall, which is the same as %d centimetres" % (height_inches, height_cm)
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height_inches + weight)
