from sys import exit

def heaven_room():
    print "How much of the money will you take yourself??"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 5000:
        print "WHAT? You don't want to take more than that?!"
        exit(0)
    else:
        dead("Good, good. It's your money now!")


def mafia_room():
    print "There are lots of mafia here."
    print "They have plenty of guns and knives"
    print "They say they want the money you owe them"
    print "What will you do?"
    mafia_in_peace = False

    while True:
        next = raw_input("> ")

        if next == "give them money":
            dead("They discuss with each other and decides that you will live. ")
        elif next == "Take the guns and shoot" and not mafia_in_peace:
            print "The mafia is dead, you can go free."
            mafia_in_peace = True
        elif next == "Take the guns and knives" and mafia_in_peace:
            dead("The mafia gets pissed of and kill you.")
        elif next == "PAY" and mafia_in_peace:
            heaven_room()
        else:
            print "I got no idea what that means, try to write a word in this text."


def love_room():
    print "Here you see a lovely room with roses and hearts"
    print "There is one dilemma. There is also a murderer that loves RED blood, you have to get away."
    print "Do you kill yourself or do you run out"

    next = raw_input("> ")

    if "kill" in next:
        start()
    elif "run" in next:
        dead("You can't run from the murderer. He will find you....")
    else:
        love_room()


def dead(why):
    print why, "Very nice!"
    exit(0)

def start():
    print "Hello, when you enter this room you can choose between two doors."
    print "There is one black and one red, which will you take?"

    next = raw_input("> ")

    if next == "black":
        mafia_room()
    elif next == "red":
        love_room()
    else:
        dead("This door does not exist. You fall into a dark hole.")


start()
