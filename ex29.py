people = 20
cats = 30
dogs = 15

# The if statement means that: IF the statement I have is true, print the text. 
if people < cats:
    print "Too many cats! The world is doomed!"
# A colon at the end of a line is how you tell Python you are going to create a new "block" of code, 
# and then indenting four spaces tells Python what lines of code are in that block. 
if people > cats:
    print "Not many cats! The world is saved!"
elif people <= cats:
        print "There are so many cats here"
else:
        print "The cats are doomed, there are to many dogs here"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

# This adds 5 extra to the "dogs" variable.
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
elif cats > dogs:
        print "The cats will take over the world. There are way to many cats even if we got five extra dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."
