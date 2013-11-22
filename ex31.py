print "You enter a restaurant and can pick between two menus. Do you pick #1 with seafood or #2 with junkfood?"

menu = raw_input("> ")

if menu == "1":
    print "Seafood, really??? The chef is pissed of, he wants to murder you, WHAT DO YOU DO???"
    print "1. Stay with the same menu, and get in a fight with the chef."
    print "2. Don't want to argue, I can take the other menu."

    chef = raw_input("> ")

    if chef == "1":
        print "You are really stupid, you could not remember that the chef has plenty of knives"
    elif chef == "2":
        print "You are a smart person, but the chef will murder you anyway."
    else:
        print "Well, it is the same if you choose %s, the chef will murder you, even if you are good or bad." % chef

elif menu == "2":
    print "Okokok, so now you are in trouble. The chef is angry. What will you do?"
    print "1. I want to kill him"
    print "2. I want to die, I cant do this any more."
    print "3. I will survive."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "YOU DIE"
    else:
        print "You got saved by superman"

else:
    print "You stumble around and fall on the chefs knife and die.  Good job!"
