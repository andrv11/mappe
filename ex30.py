people = 100
cars = 200
buses = 300

# I think elif and else are two other statements that gets runned if the if is false. If elif is false also
# then else will run. 

# Every block of code, python runs it until it finds the first block that is true. 
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
