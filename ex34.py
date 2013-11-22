i = 0
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

while i < 7:
        print "At the top i is %s" % i
        animals.append(i)
        
        i = i + 1
        print "Animal now: ", animals
        print "At the bottom i is %s" % i 
        
print "The animals: "

for ani in animals:
        print ani



"""The animal at 1 is a python.
The third (3rd) animal is at 2 and is a peacock.
The first (1st) animal is at 0 and is a bear.
The animal at 3 is a kangaroo.
The fifth (5th) animal is at 4 and is a whale.
The animal at 2 is a python.
The sixth (6th) animal is at 5 and is a platypus.
The animal at 4 is a whale."""
