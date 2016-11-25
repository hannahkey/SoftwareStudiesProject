from sys import exit
import winsound
import time
import os
import thread
from random import randint
import threading

os.system("mode con: cols=110 lines=50")

smarts = []
practical = []
fear = []
cruel = []
inventory = []

win = []

code = []

playername = "none"
done = "no"
clockstop = "no"
creature = 0
global creature
ran = 0
global ran
dangerlevel = "none"
#chance = 0

codeA = randint(1, 9)
codeB = randint(1, 9)
codeC = randint(1, 9)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
def clrscrn():
    os.system('cls' if os.name == 'nt' else 'clear')


##TRAIN
def playsound1(threadName, delay):
    winsound.PlaySound('trains004.wav', winsound.SND_FILENAME)
def playsound2(threadName, delay):
    winsound.PlaySound('trains012fade.wav', winsound.SND_FILENAME)
##UNLOCK
def playsound3(threadName, delay):
    winsound.PlaySound('open_door_3', winsound.SND_FILENAME)
##DOOR
def playsound4(threadName, delay):
    winsound.PlaySound('trains005', winsound.SND_FILENAME)
##CLOCKTICK
def playsound5(threadName, delay):
    winsound.PlaySound('clockticking', winsound.SND_FILENAME)
##STRINGS
def playsound6(threadName, delay):
    winsound.PlaySound('strings', winsound.SND_FILENAME)
##FIRSTCLASSENTER
def playsound7(threadName, delay):
    winsound.PlaySound('firstclass', winsound.SND_FILENAME)
##TRAINSHORT
def playsound8(threadName, delay):
    winsound.PlaySound('trains006kurz', winsound.SND_FILENAME)
##CLOCKSTOP
def playsound9(threadName, delay):
    winsound.PlaySound('clockstop', winsound.SND_FILENAME)
##FIRSTCLASS
def playsound10(threadName, delay):
    winsound.PlaySound('firstclass', winsound.SND_FILENAME)
##CLOCKWIND
def playsound11(threadName, delay):
    winsound.PlaySound('clockwinding', winsound.SND_FILENAME)
##WIND
def playsound12(threadName, delay):
    winsound.PlaySound('wind', winsound.SND_FILENAME)
##KEY
def playsound13(threadName, delay):
    winsound.PlaySound('key', winsound.SND_FILENAME)
##MACHINERY
def playsound14(threadName, delay):
    winsound.PlaySound('machines', winsound.SND_FILENAME)
##DOORSHORT
def playsound15(threadName, delay):
    winsound.PlaySound('doorSHORT', winsound.SND_FILENAME)
##WINDSHORT
def playsound16(threadName, delay):
    winsound.PlaySound('windSHORT', winsound.SND_FILENAME)
##MONSTER
def playsound17(threadName, delay):
    winsound.PlaySound('monster', winsound.SND_FILENAME)
##OVER
def playsound18(threadName, delay):
    winsound.PlaySound('scary', winsound.SND_FILENAME)
##TITLES
def playsound19(threadName, delay):
    winsound.PlaySound('titles', winsound.SND_FILENAME)

def checkinput(s):
    if "inventory" in s:
        print inventory
        next = raw_input("PRESS ENTER\n").lower()
        checkinput(next)
    elif "help" in s:
        helpmenu()
    elif "quit" in s:
        quit()
    elif "reset" in s:
        menu()
    #raw_input()
def OVER():
    clrscrn()
    try:
        thread.start_new_thread( playsound18, ("Thread-2", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(1)
    print "\n"
    print('{:^110}'.format(color.RED + "TH|S  " + color.END))
    print "\n"
    print('{:^110}'.format(color.RED + "    SHALL" + color.END))
    print "\n"
    print('{:^110}'.format(color.RED + "BE" + color.END))
    print "\n"
    print('{:^110}'.format(color.RED + "  |T" + color.END))
    time.sleep(9)
    clrscrn()
    time.sleep(1)
    menu()
def titles():
    clrscrn()
    try:
        thread.start_new_thread( playsound19, ("Thread-2", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(4)
    print "\n\n\n\n"
    print('{:^110}'.format("TIME"))
    time.sleep(3)
    clrscrn()
    time.sleep(1)
    print "\n\n\n\n"
    print('{:^110}'.format("by Hannah Keymling"))
    time.sleep(4)
    clrscrn()
    time.sleep(1)
    print "\n\n\n\n"
    print('{:^110}'.format("written in python"))
    time.sleep(3)
    clrscrn()
    time.sleep(1)
    print "\n\n\n\n"
    print('{:^110}'.format("2016"))
    time.sleep(3)
    clrscrn()
    time.sleep(1)
    print "\n\n\n\n"
    print('{:^110}'.format("Thank you for playing."))
    time.sleep(5)
    clrscrn()
    time.sleep(7)
    exit()


def menu():
    clrscrn()
    try:
        thread.start_new_thread(playsound5, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(0.25)
    print color.UNDERLINE + """\n
                                Welcome to TIME
""" + color.END
    time.sleep(1)
    print """\n
\tSTART"""
    time.sleep(0.5)
    print """
\tHELP"""
    time.sleep(0.5)
    print """
\tABOUT"""
    time.sleep(0.5)
    print """
\tQUIT

"""
    time.sleep(0.5)
    if "alice" in win:
        print "- A\n"
    if "john" in win:
        print "- J\n"
    if "conductor" in win:
        print "- C\n"
    if "alice" in win and "john" in win and "conductor" in win:
        print('{:^110}'.format("CONGRATULATIONS"))
        print('{:^110}'.format("You have completed all three endings of the game."))
        print('{:^110}'.format("As a reward you can now play a special stage!"))
        print('{:^110}'.format("Hope you enjoy!"))
        print """


\tSPECIAL\n"""
    while True:
        next = raw_input("> ").lower()
        if "start" in next or "START" in next:
            birth()
        elif "help" in next or "HELP" in next:
            helpmenu()
        elif "about" in next or "ABOUT" in next:
            about()
        elif "quit" in next:
            quit()
        elif "special" in next:
            finalbirth()
        else:
            print """
Please type out what you would like to do.
            """

def helpmenu():
    print "\n\tThis is a game made with Python"
    print "\tPlaying the game is rather simple"
    print "\tIt is a text based game"
    print "\tThat means that it is made up completely of text"
    print "\tThe story will be told to you through text"
    print "\tAnd you interact with it through text"
    print "\tIf the game needs you to type something out,"
    print "\tyou will see this symbol: > "
    print "\tUsually there will be numbered options to chose from"
    print "\tYou can also type in words to see if there are other possibilities"
    print "\tSometimes you will have to press ENTER to continue"
    print "\tThis is so you have time to read"
    print "\tTo quit the game you can use CTRL and C,"
    print "\tor type 'quit'"
    print "\tIf you want to start over, type 'reset'"
    print "\tTo check your inventory type 'inventory' and press ENTER"
    print "\tThis is all you need to know for now"
    print "\tI hope you enjoy"
    print "\n"
def about():
    print "\tTIME by Hannah Keymling."


def birth():
    del inventory[:]
    del smarts[:]
    del practical[:]
    del fear[:]
    del code[:]
    global clockstop
    clockstop = "no"
    clrscrn()
    try:
        thread.start_new_thread( playsound1, ("Thread-2", 2, ) )
    except:
        print "NO SOUND"
    print "\n"
    time.sleep(1.5)
    print color.CYAN + "\tWhere am I?" + color.END
    time.sleep(2)
    print color.CYAN + "\tHow did I get here?" + color.END
    time.sleep(2)
    print "\n\tThe last thing you remember,"
    time.sleep(1)
    print "\twhat is it?"
    time.sleep(1)
    print "\t..."
    time.sleep(1)
    print "\t..."
    time.sleep(1)
    print "\t..."
    time.sleep(2)
    print "\n\tNothing... You don't remember a thing."
    if "Alice" in win or "John" in win or "Conductor" in win:
        time.sleep(2)
        second_class()
    print "\tNot even your name."
    next = raw_input().lower()
    checkinput(next)
    print "\tYou need a name."
    time.sleep(1)
    print "\tEveryone has a name."
    next = raw_input()
    checkinput(next)
    print "\tWhat will you call yourself?"
    global playername
    playername = raw_input("> ")
    print """\n
    %s. That will do for now.\n
       """ % playername
    next = raw_input().lower()
    checkinput(next)
    awake()
def awake():
    clrscrn()
    print "\n"
    print "\tYou look around."
    time.sleep(1.5)
    print "\tRows of seats."
    time.sleep(1)
    print "\tBig black windows."
    time.sleep(1)
    print "\tThe floor is shaking ever so slightly."
    time.sleep(2)
    print "\tWhat is this place?"
    time.sleep(1)
    where = raw_input("> ").lower()
    checkinput(where)
    if "train" in where:
        print "\n\tYes. That's it."
        time.sleep(1)
        smarts.append("t")
        second_class()
    else:
        print "\n\tHm..."
        time.sleep(1)
        print "\tYou should have a look around."
        time.sleep(3)
        second_class()

def second_class():
    clrscrn()
    print "\n\tYou get up."
    time.sleep(0.5)
    print "\tThe muffled feeling in your head seems to wear off."
    time.sleep(0.5)
    print "\tYou look around."
    time.sleep(1)
    print "\n\tThis is a train car."
    time.sleep(0.5)
    print "\tYou are on a train."
    time.sleep(0.5)
    next = raw_input().lower()
    checkinput(next)
    print "\tIt doesn't look like it should still be in use though."
    time.sleep(0.5)
    print "\tIt seems dirty and run down."
    time.sleep(0.5)
    print "\tA dim lamp on the ceiling lights up the room."
    time.sleep(2)
    print "\n\tThere used to be curtains hanging in front of the windows. \n\tThe fabric of the seats must have been a really nice red color at one point."
    print "\n\tA rattling wooden door to your left seems to be leading to the next car. \n\tAnother door, a metal one at the opposite end of the room has something written on it in faded letters."
    time.sleep(2)
    choice()
def choice():
    print """\n
    1 [LOOK AT WINDOW]
    2 [LOOK AT SEATS]
    3 [WOODEN DOOR]
    4 [METAL DOOR]\n"""
    doorunlocked = False
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "window" in next:
            print "\n\tYou look out the stained window infront of you."
            time.sleep(0.5)
            print "\tAll you see is darkness. Pitch black."
            time.sleep(0.5)
            print "\tIt must be nighttime."
            time.sleep(1)
            print "\n\tThis place is so filthy. Someone even smeared on the walls."
            time.sleep(1)
            print """\n
    0 [EXAMINE WALL]"""
            choice()
        elif "2" in next or "seat" in next:
            print "\n\tThere are only few seats here."
            time.sleep(0.5)
            print "\tThere used to be more, you can see markings where they were attached to the floor."
            next = raw_input().lower()
            choice()
        elif "3" in next or "wood" in next or "wooden" in next or "left" in next:
            if "key" in inventory:
                fourthcar()
            print "\n\tThere is a little window inside the door. The glass is cracked and dirty."
            time.sleep(0.5)
            print """\n
    1 [GO THROUGH DOOR]
    2 [GO BACK]\n"""
            while True:
                next = raw_input("> ").lower()
                checkinput(next)
                if "1" in next or "through" in next:
                    fourthcar()
                elif "2" in next or "back" in next:
                    choice()
        elif "4" in next or "metal" in next or "right" in next:
            if "key" in inventory:
                thread.start_new_thread( playsound3, ("Thread-1", 2, ) )
                print "\n\tThe door is unlocked!"
                time.sleep(1)
                print """\n
    1 [GO THROUGH DOOR]
    2 [GO BACK]\n"""
                while True:
                    next = raw_input("> ").lower()
                    checkinput(next)
                    if "1" in next or "through" in next:
                        restaurant1()
                    elif "2" in next or "back" in next:
                        choice()
                    else:
                        print "\tWhat now?"
            print "\n\tAs you come closer you can make out what it says on the door:"
            time.sleep(0.5)
            print "\n\tRESTAURANT"
            time.sleep(1.5)
            print """\n
    1 [TRY DOOR]
    2 [GO BACK]\n"""
            while True:
                next = raw_input("> ").lower()
                checkinput(next)
                if "1" in next or "try" in next:
                    print "\n\tThe door seems to be locked."
                    time.sleep(0.5)
                    print "\tStrange to find a locked door on a train...\n"
                    time.sleep(1)
                elif "2" in next or "back" in next:
                    choice()
                else:
                    print "\tWhat now?"
        elif "0" in next or "wall" in next or "examine" in next:
            print('{:^110}'.format(color.RED + "THE TROUBLE IS YOU THINK YOU HAVE TIME" + color.END))
            time.sleep(1.6)
            print "\t..."
            time.sleep(0.5)
            print "\n\tWhat is this place?"
            time.sleep(1.5)
            choice()
        else:
            print "\tWhat now?"
def second_class2():
    try:
        thread.start_new_thread( playsound4, ("Thread-3", 2, ) )
    except:
        print "NO SOUND"
    clrscrn()
    print "\n"
    print "\tYou are back in the second class car where you woke up."
    next = raw_input().lower()
    checkinput(next)
    print "\tYou see the metal door ahead, the windows and seats."
    print "\tThe wooden door is where you just came from."
    time.sleep(0.5)
    choice()

def fourthcar():
    try:
        thread.start_new_thread( playsound2, ("Thread-4", 2, ) )
    except:
        print "NO SOUND"
    clrscrn()
    print "\n"
    if "key" in inventory:
        fourthcar2()
    time.sleep(2)
    print "\tYou enter the next train car."
    time.sleep(0.5)
    print "\tIt looks much like the one you just came from:"
    print "\tA few dirty seats, black windows..."
    time.sleep(0.5)
    print "\tExcept this seems to be the rearmost train car."
    time.sleep(0.5)
    print "\tOn the other side of the door across from you you can see the darkness outside."
    time.sleep(0.5)
    print """\n
    1 [GO AHEAD]
    2 [GO BACK]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        time.sleep(0.5)
        if "2" in next or "back" in next:
            second_class2()
        else:
            print "\n"
            print color.DARKCYAN + "\tHey you!" + color.END
            time.sleep(1.5)
            print "\n\tAs you start moving, you notice that someone is sitting against the wall to your left."
            time.sleep(0.5)
            print "\tPartially hidden by the sad remains of a once red passenger seat, there he is."
            time.sleep(0.5)
            print "\n\tA young man."
            next = raw_input("> ").lower()
            checkinput(next)
            if "run" in next or "leave" in next:
                print "\tYou should probably stay and talk to him."
                time.sleep(0.5)
                print "\tSo far you two seem to be the only living things around here."
                time.sleep(2)
                fear.append["l"]
                lodur1()
            elif "fight" in next or "kill" in next or "attack" in next or "punch" in next:
                print color.DARKCYAN + """What are you doing?!\n\n
    HELP! NO!
                """ + color.END
                time.sleep(2)
                print "\tHe must have been very weak."
                time.sleep(0.5)
                print "\tHe didn't stand a chance."
                time.sleep(0.5)
                print "\tYou look down at the lifeless body."
                time.sleep(2)
                cruel.append("l")
                lodurdead()
            else:
                lodur1()
def fourthcar2():
    global done
    if done is "yes":
        fourthcar3()
    try:
        thread.start_new_thread( playsound4, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    clrscrn()
    #beenhere = False
    print "\n\tThis is the rearmost train car."
    time.sleep(1)
    print "\tBut..."
    time.sleep(0.5)
    print "\tWhere is the man from earlier?"
    time.sleep(1)
    print """
    1 [GO OUTSIDE]
    2 [GO TO SECOND CLASS]"""
    next = raw_input("> ").lower()
    checkinput(next)
    while True:
        if "1" in next or "outside" in next:
            print "\n\tYou go outside."
            time.sleep(2)
            done = "yes"
            if "a" in practical:
                outside()
            alice1_5()
        elif "2" in next or "second" in next:
            print "\n\tYou go through the wooden door."
            time.sleep(2)
            done = "yes"
            second_class2()
        else:
            print "\tWhat now?"
def fourthcar3():
    try:
        thread.start_new_thread( playsound4, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    clrscrn()
    print "\n\tThis is the rearmost train car."
    time.sleep(1)
    print """
    1 [GO OUTSIDE]
    2 [GO TO SECOND CLASS]"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "outside" in next:
            print "\n\tYou go outside."
            time.sleep(2)
            outside()
        elif "2" in next or "second" in next:
            print "\n\tYou go through the wooden door."
            time.sleep(2)
            second_class2()
        else:
            print "\tWhat now?"

def lodurdead():
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "ahead" in next or "door" in next or "walk" in next or "look" in next:
            print "\tYou approach the door."
            time.sleep(1)
            print "\tIt definitely leads outside."
            print "\tYou can feel the cold of the night creeping in."
            time.sleep(1)
            next = raw_input()
            checkinput(next)
            alice1()
        else:
            print "\tWhat now?"
def lodur1():
    print color.DARKCYAN + "\n\tYes, you." + color.END
    time.sleep(1)
    print "\n\tHe looks weak."
    print "\tAs you approach him you see that his shirt is stained with old blood."
    time.sleep(0.5)
    print "\tHe looks just as filthy as everthing else around here."
    time.sleep(0.5)
    print "\tHe really fits into this place."
    time.sleep(0.5)
    print """
    1 [Who are you?]
    2 [What is this place?]
    3 [How did I get here?]
        """
    lodur2()
def lodur2():
    while True:
        if "key" in inventory:
           lodur3()
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "who" in next:
            who()
        elif "2" in next or "what" in next:
            what()
        elif "3" in next or "how" in next:
            how()
        elif "4" in next or "name" in next:
            name()
def lodur2_5():
    print """
    1 [Who are you?]
    2 [What is this place?]
    3 [How did I get here?]
    4 [What's your name?]
        """
    while True:
        if "key" in inventory:
           lodur3()
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "who" in next:
            who()
        elif "2" in next or "what" in next:
            what()
        elif "3" in next or "how" in next:
            how()
        elif "4" in next or "name" in next:
            name()
def lodur3():
    #print "\n"
    print color.DARKCYAN + "\tAlright then. Go on." + color.END
    print color.DARKCYAN + "\tI'm tired. Let me sleep." + color.END
    time.sleep(1)
    print """\n
    1 [GO AHEAD]
    2 [GO BACK]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "ahead" in next:
            alice1()
        elif "2" in next or "back" in next:
            second_class2()
        else:
            print "\tWhat are you gonna do?"

def who():
        print color.CYAN + "\n\tWho are you?" + color.END
        time.sleep(2)
        print color.DARKCYAN + "\n\tThat is a big question to ask." + color.END
        time.sleep(0.5)
        print color.DARKCYAN + "\tI can't deny that I am." + color.END
        time.sleep(0.5)
        print color.DARKCYAN + "\n\tBut that's really it I guess." + color.END
        time.sleep(1)
        lodur2_5()
def name():
    print color.DARKCYAN + "\n\tNames. Names don't mean a thing." + color.END
    time.sleep(1)
    print color.DARKCYAN + "\tThat's what I learned anyway." + color.END
    time.sleep(1)
    print color.DARKCYAN + "\tYou want to tell me yours?" + color.END
    time.sleep(1)
    print """\n
    1 [It's %s.]
    2 [I won't tell you my name!]\n""" % playername
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "2" in next or "no" in next:
            print color.DARKCYAN + "\n\tAlright. That's fine." + color.END
            time.sleep(1)
            print color.DARKCYAN + "\tNames don't mean a thing." + color.END
            time.sleep(1)
            print """
            2 [What is this place?]
            3 [How did I get here?]
                """
            lodur2()
        elif "1" in next or "yes" in next:
            print color.DARKCYAN + "\n\t%s, huh? Well, it's a name I guess." % playername + color.END
            next = raw_input().lower()
            checkinput(next)
            print """
    2 [What is this place?]
    3 [How did I get here?]
                """
            lodur2()
        else:
            print "\tWhat now?"
def what():
    print color.CYAN + "\n\tWhat is this place?" + color.END
    time.sleep(1)
    print "\n\tHe sighs. It makes him cough. He looks tired."
    time.sleep(1)
    print color.DARKCYAN + "\n\tThat's the right question to ask here." + color.END
    if "t" in smarts:
        time.sleep(0.5)
        print color.DARKCYAN + "\n\tThis, here, it's everything there is. Everything there ever will be." + color.END
        time.sleep(1)
        print "\n\tHe sighs."
        time.sleep(1)
        print "\t..."
        next = raw_input().lower()
        checkinput(next)
        print """
        1 [Who are you?]
        3 [How did I get here?]
            """
        lodur2()
    else:
        next = raw_input().lower()
        checkinput(next)
        time.sleep(0.5)
        print """
        1 [Who are you?]
        3 [How did I get here?]
            """
        lodur2()
def how():
    print color.CYAN + "\n\tHow did I get here? I don't remember a thing." + color.END
    time.sleep(1)
    print color.DARKCYAN + "\n\tHow would I know?" + color.END
    time.sleep(0.5)
    print color.DARKCYAN + "\t..." + color.END
    time.sleep(1)
    print color.DARKCYAN + "\n\tSorry, I wish I could help you more." + color.END
    time.sleep(1)
    print color.DARKCYAN + "\tI don't have all the answers." + color.END
    time.sleep(1)
    print color.DARKCYAN + "\t..." + color.END
    time.sleep(2)
    if "key" in inventory:
        next = raw_input().lower()
        checkinput(next)
        lodur2()
    else:
        print color.DARKCYAN + "\tBut there is something I do have for you! Here." + color.END
        time.sleep(1)
        print "\n\tHe gives you something."
        print "\tIt is small and made of metal."
        inventory.append("key")
        try:
            thread.start_new_thread( playsound13, ("Thread-1", 2, ) )
        except:
            print "NO SOUND"
        time.sleep(0.5)
        print "\n\tA key! You put it in your pocket.\n"
        next = raw_input().lower()
        checkinput(next)
        lodur2()

def alice1():
    try:
        thread.start_new_thread( playsound12, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    clrscrn()
    print "\n"
    print "\tIt is very cold out here."
    time.sleep(1)
    print "\tYou're standing on a small platform that extrudes from the end of the train."
    time.sleep(1)
    print "\tThough you can't see anything in the darkness ahead, \n\tyou can feel how the world keeps disappearing into nothingness right in front of you."
    time.sleep(1)
    next = raw_input().lower()
    checkinput(next)
    print color.BLUE + "\t%s." % playername + color.END
    time.sleep(2)
    print """\n
    1 [Hey! Show yourself!]
    2 [Hello..?]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "how" in next:
            print color.CYAN + "\n\tHey! How do you know my name?" + color.END
            fear.append("a")
            time.sleep(1)
            print "\n\tA smile"
            time.sleep(1)
            print color.BLUE + "\n\tCome sit with me, %s." % playername + color.END
            time.sleep(1.2)
            print "\n\tIn the sparse light creeping through the door you can barely see her.\n"
            time.sleep(2)
            print "\tShe too is wearing ripped and stained clothes."
            print "\tUnlike your friend from before she doesn't look tired though."
            time.sleep(2)
            print "\tHer face is barely visible, but from what you can tell her expression is friendly."
            print "\tHer eyes seem to be holding you in a warm embrace."
            next = raw_input().lower()
            checkinput(next)
            alice2()
        elif "2" in next or "hello" in next:
            print color.CYAN + "\n\tHello? Who's there?" + color.END
            time.sleep(1)
            print "\n\tA smile"
            time.sleep(1)
            print color.BLUE + "\n\tOh silly. It's just me!" + color.END
            time.sleep(1)
            time.sleep(1.2)
            print "\n\tIn the sparse light creeping through the door you can barely see her.\n"
            time.sleep(2)
            print "\tShe too is wearing ripped and stained clothes."
            print "\tUnlike your friend from before she doesn't look tired though."
            time.sleep(2)
            print "\tHer face is barely visible, but from what you can tell her expression is friendly."
            print "\tHer eyes seem to be holding you in a warm embrace."
            next = raw_input().lower()
            checkinput(next)
            alice2()
        else:
            print "\tWhat now?"
def alice1_5():
    try:
        thread.start_new_thread( playsound12, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    clrscrn()
    print "\n"
    print color.BLUE + "\tHello again." + color.END
    alice2()
def alice2():
    print """
    1 [Sit down]
    2 [Go back]"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "sit" in next:
            print "\n\tYou carefully sit down next to her."
            next = raw_input().lower()
            checkinput(next)
            sitwithalice1()
        elif "2" in next or "go" in next or "back" in next:
            print "\n\tYou go back inside of the train car."
            time.sleep(2)
            fourthcar2()
        else:
            print "\tWhat now?"
def sitwithalice1():
    clrscrn()
    print color.BLUE + "\n\tIt's so nice of you to join me." + color.END
    time.sleep(1)
    print "\n\tShe smiles."
    time.sleep(2)
    print "\n\tYou expected the floor to be cold."
    time.sleep(1)
    print "\tBut for some reason you feel warmer than you did inside of the train."
    time.sleep(2)
    print """\n
    1 [Who are you?]
    2 [What are you doing here?]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "who" in next or "ask" in next:
            print "\n"
            time.sleep(1)
            print color.BLUE + "\tMy name is Alice." + color.END
            time.sleep(1)
            print "\n\tShe smiles."
            time.sleep(1.5)
            sitwithalice2()
        elif "2" in next or "here" in next:
            time.sleep(1)
            sitwithalice2()
        else:
            print "\tWhat now?"
def sitwithalice2():
    clrscrn()
    print "\n"
    print color.CYAN + "\tWhat are you doing here?" + color.END
    time.sleep(2)
    print "\n"
    print color.BLUE + "\tI look at the stars." + color.END
    time.sleep(1)
    print color.BLUE + "\tThey make me happy." + color.END
    time.sleep(1)
    print "\n\tShe is still smiling."
    time.sleep(1.25)
    print "\n\tShe must be crazy... All you can see is darkness."
    time.sleep(1)
    print "\tYou sit in silence for a while."
    time.sleep(1)
    print """\n
    1 [STAY A LITTLE LONGER]
    2 [GO BACK INSIDE]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "stay" in next:
            sitwithalice3()
        elif "2" in next or "go" in next or "inside" in next:
            print "\n\tYou go back inside."
            fourthcar2()
        else:
            print "\tWhat now?"
def sitwithalice3():
    clrscrn()
    time.sleep(1)
    print "\n\tYou don't really know how much time has passed."
    time.sleep(1)
    print "\tMaybe you should get up."
    time.sleep(1)
    print """\n
    1 [GET UP]
    2 [STAY]\n"""
    print ("> ")
    time.sleep(1)
    print color.BLUE + "\n\tDo you have to go?" + color.END
    time.sleep(1)
    print color.BLUE + "\tIs there something important you have to do?" + color.END
    time.sleep(1)
    print """\n
    1 [YES, I SHOULD GO]
    2 [I GUESS NOT]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "go" in next or "yes" in next:
            print "\n"
            time.sleep(1)
            print color.BLUE + "\n\tIt was very nice sitting here with you." + color.END
            time.sleep(1)
            print "\n\tShe smiles at you once more."
            time.sleep(1)
            practical.append("a")
            fourthcar2()
        elif "2" in next or "stay" in next or "no" in next:
            print "\n"
            print color.BLUE + "\tThat's nice." + color.END
            time.sleep(1)
            print "\n\tShe smiles. You can't really see it, but you know that she is."
            time.sleep(1)
            print "\n\tYou sit in silence for a while."
            time.sleep(3)
            sitwithalice4()
def sitwithalice4():
    clrscrn()
    print "\n"
    time.sleep(1)
    print color.BLUE + "\tDon't you just love the stars?" + color.END
    time.sleep(1.25)
    print "\n\tHer voice wakes you from a deep state of nothingness."
    time.sleep(1)
    print "\tHad you fallen asleep?"
    time.sleep(1)
    print "\n"
    print color.CYAN + "\tI'm sorry, what did you say?" + color.END
    time.sleep(1.25)
    print "\n\tAnother smile"
    time.sleep(1)
    print color.BLUE + "\n\tThe stars, %s, aren't they beautiful?" % playername + color.END
    time.sleep(0.5)
    print "\n"
    next = raw_input("> ").lower()
    checkinput(next)
    if "yes" in next or "beautiful" in next or "sure" in next or "they are" in next or "indeed" in next or "agree" in next:
        print "\n"
        print "\tHow come you didn't notice them before?"
        time.sleep(1)
        print "\tBefore, you thought there was only darkness out here."
        time.sleep(1.25)
        print "\n\tBut now you see billions of white specks overhead."
        time.sleep(1)
        print color.CYAN + "\n\n\tThe stars\n." + color.END
        time.sleep(1)
        print "\n\tThey seem so calm and constant."
        print "\tYet they are undeniably beautiful."
        next = raw_input().lower()
        checkinput(next)
        bliss()
    else:
        print "\n"
        print "\tAlice turns towards you."
        time.sleep(1)
        print color.BLUE + "\n\tI think there are things you still want to do." + color.END
        time.sleep(1)
        print color.BLUE + "\tThings other than staring at the stars." + color.END
        time.sleep(1)
        print "\n\tShe is right."
        time.sleep(1)
        print "\tYou get up."
        next = raw_input().lower()
        checkinput(next)
        print "\n"
        print color.BLUE + "\tHere. Take this." + color.END
        time.sleep(1)
        print "\n\tShe takes your hand and places something inside of it."
        time.sleep(1)
        print "\tHer hands are soft but cold."
        inventory.append("glass shard")
        next = raw_input().lower()
        checkinput(next)
        print "\n"
        print color.BLUE + "\tTake care, %s." % playername + color.END
        time.sleep(1)
        print color.BLUE + "\tThere is only so much time for each of us." + color.END
        #time.sleep(3)
        next = raw_input().lower()
        checkinput(next)
        fourthcar2
def bliss():
    try:
        thread.start_new_thread( playsound6, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    clrscrn()
    print "\n"
    print color.BLUE + "\tI'm so glad that you are here with me." + color.END
    time.sleep(1.5)
    print color.BLUE + "\n\tNo one should be alone in a place like this." + color.END
    time.sleep(1.5)
    print "\n\tYou agree."
    time.sleep(1.5)
    print "\n\tYou are glad that you stayed."
    time.sleep(2)
    print "\n"
    print color.BLUE + "\n\tLet's go." + color.END
    time.sleep(1.5)
    print "\n\tShe smiles."
    time.sleep(3)
    print "\n\n"
    print('{:^110}'.format(color.BLUE + "CONGRATULATIONS" + color.END))
    print "\n\n"
    win.append("alice")
    time.sleep(1)
    print "\tPress ENTER to continue"
    next = raw_input().lower()
    checkinput(next)
    menu()
def outside():
    try:
        thread.start_new_thread( playsound12, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    clrscrn()
    print "\n"
    time.sleep(1)
    print "\tIt's very cold out here."
    time.sleep(0.5)
    print "\n\tThough you can't see anything in the darkness ahead, \n\tyou can feel how the world keeps disappearing into nothingness right in front of you."
    time.sleep(0.5)
    print """\n
    1 [GO BACK]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "back" in next:
            fourthcar3()
        else:
            print "\n\tThere is nothing else to do here."

def restaurant1():
    global done
    if done is "on":
        restaurant3()
    clrscrn()
    try:
        thread.start_new_thread( playsound1, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(1)
    print "\n"
    print "\tYou enter the restaurant car."
    time.sleep(0.5)
    print "\tIt is larger than the other compartments."
    print "\n\tThere are sitting booths along both walls."
    time.sleep(0.5)
    print "\tAt the far end you can see a bar."
    time.sleep(0.5)
    print "\tBehind it used to be a door, now it is just a big hole in the wall."
    time.sleep(0.5)
    print "\n\tThere is also another door, a shiny black one."
    time.sleep(0.5)
    print "\n\tEverything else here looks like it is slowly decaying."
    print "\tThe door seems out of place."
    time.sleep(0.75)
    print "\n\tA clock is ticking loudly."
    time.sleep(0.75)
    print "\n\tOther than that it is quiet."
    time.sleep(0.5)
    print "\n\tYou are alone."
    time.sleep(1)
    done = "on"
    restaurant2()
def restaurant2():
    print """\n
    1 [EXAMINE TABLES]
    2 [EXAMINE CLOCK]
    3 [EXAMINE BAR]
    4 [BLACK DOOR]
    5 [METAL DOOR]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "table" in next:
            print "\n\tYou have a closer look at one of the tables."
            time.sleep(0.5)
            print "\n\tIt is bolted to the floor."
            print "\tAs are the upholstered chairs on either side."
            time.sleep(0.5)
            print "\n\tBoth the table and the chairs are covered in deep scratches."
            time.sleep(0.5)
            print "\n\tYou wonder where those come from."
            time.sleep(1)
        elif "2" in next or "clock"in next:
            clock1()
        elif "3" in next or "bar" in next:
            print "\n\tYou approach the bar."
            time.sleep(0.5)
            print "\tIt is dirty."
            time.sleep(0.5)
            print"""\n
    1 [GO BACK]
    2 [CLIMB OVER BAR]\n"""
            while True:
                next = raw_input("> ").lower()
                checkinput(next)
                if "1" in next or "back" in next:
                    restaurant2()
                elif "2" in next or "climb" in next:
                    print "\n\tYou climb over the bar."
                    behindbar()
                else:
                    print "\n\tWhat now?"
        elif "4" in next or "black" in next:
            if clockstop is "yes":
                firstclass()
            print "\n\tYou walk over to the shiny door."
            time.sleep(0.5)
            print "\tIt seems to be locked."
            time.sleep(1)
            print "\n\tHey!"
            time.sleep(0.5)
            print "\tWhat's that?"
            time.sleep(1)
            print "\n"
            print('{:^110}'.format(color.RED + "TIME IS RUNNING AGAINST YOU" + color.END))
            print "\n"
        elif "5" in next or "metal" in next:
            second_class2()
def restaurant3():
    clrscrn()
    if clockstop is "yes":
        restaurant4()
    try:
        thread.start_new_thread( playsound8, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(1)
    print "\n"
    print "\tThe clock is ticking loudly."
    time.sleep(0.75)
    print "\n\tOther than that there are no sounds."
    time.sleep(0.5)
    print "\tYou are alone."
    time.sleep(1)
    restaurant2()
def restaurant4():
    clrscrn()
    time.sleep(1)
    print "\n\tYou are standing in the restaurant car."
    time.sleep(0.5)
    print "\n\tIt is eerily quiet."
    time.sleep(1)
    restaurant5()
def restaurant5():
    print """\n
    1 [EXAMINE CLOCK]
    2 [BLACK DOOR]
    3 [METAL DOOR]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "clock"in next:
            clrscrn()
            print "\n\tThe clock is silent."
            next = raw_input().lower()
            checkinput(next)
            restaurant5()
        elif "2" in next or "black" in next:
            time.sleep(0.5)
            firstclass()

        elif "3" in next or "metal" in next:
            clrscrn()
            print "\n\tThe door doesn't open."
            next = raw_input().lower()
            checkinput(next)
            restaurant5()
        else:
            print "\n\tWhat now?"
def clock1():
    global clockstop
    clrscrn()
    if clockstop is "yes":
        time.sleep(0.5)
        print "\n\tThe clock is silent."
        next = raw_input().lower()
        checkinput(next)
        restaurant5()
    try:
        thread.start_new_thread(playsound5, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    print "\n\tYou approach the large ornate clock."
    time.sleep(0.5)
    print "\tIt is ticking mercilessly."
    time.sleep(1)
    print "\n\tUnderneath the face you see three small openings with little gears behind them."
    time.sleep(0.5)
    print "\n\n"
    print('{:^110}'.format(color.YELLOW + "[-]" + color.END))
    print('{:^110}'.format(color.YELLOW + "[-]" + color.END))
    print('{:^110}'.format(color.YELLOW + "[-]" + color.END))
    print "\n\n"
    time.sleep(1)
    print "\tYou can turn each of them to display a number between 1 and 9."
    time.sleep(0.5)
    print """\n
    1 [SET FIRST NUMBER]
    2 [SET SECOND NUMBER]
    3 [SET THIRD NUMBER]
    4 [GO BACK]\n"""
    while True:
        if "A" in code and "B" in code and "C" in code:
            clockstop = "yes"
            time.sleep(0.25)
            try:
                thread.start_new_thread(playsound9, ("Thread-1", 2, ) )
            except:
                print "NO SOUND"
            time.sleep(1)
            print "\n\n\tThe clock stopped."
            time.sleep(2)
            restaurant4()
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "first" in next:
            time.sleep(0.5)
            print "\n\t\tPut in a number."
            time.sleep(0.5)
            try:
                input = int(raw_input("[ "))
                if input is codeA:
                    code.append("A")
                    try:
                        thread.start_new_thread(playsound11, ("Thread-1", 2, ) )
                    except:
                        print "NO SOUND"
                    time.sleep(1)
                    print "\n\tYou put in %d." % input
                else:
                    try:
                        thread.start_new_thread(playsound11, ("Thread-1", 2, ) )
                    except:
                        print "NO SOUND"
                    time.sleep(1)
                    print "\n\tYou put in %d." % input
            except:
                print "\tThat is not a number.\n"
        elif "2" in next or "second" in next:
            time.sleep(0.5)
            print "\n\t\tPut in a number."
            time.sleep(0.5)
            try:
                input = int(raw_input("[ "))
                if input is codeB:
                    code.append("B")
                    time.sleep(1)
                    try:
                        thread.start_new_thread(playsound11, ("Thread-1", 2, ) )
                    except:
                        print "NO SOUND"
                    print "\n\tYou put in %d." % input
                else:
                    try:
                        thread.start_new_thread(playsound11, ("Thread-1", 2, ) )
                    except:
                        print "NO SOUND"
                    time.sleep(1)
                    print "\n\tYou put in %d." % input
            except:
                print "\tThat is not a number.\n"
        elif "3" in next or "third" in next:
            time.sleep(0.5)
            print "\n\t\tPut in a number."
            time.sleep(0.5)
            try:
                input = int(raw_input("[ "))
                if input is codeC:
                    code.append("C")
                    try:
                        thread.start_new_thread(playsound11, ("Thread-1", 2, ) )
                    except:
                        print "NO SOUND"
                    time.sleep(1)
                    print "\n\tYou put in %d." % input
                else:
                    try:
                        thread.start_new_thread(playsound11, ("Thread-1", 2, ) )
                    except:
                        print "NO SOUND"
                    time.sleep(1)
                    print "\n\tYou put in %d." % input
            except:
                print "\tThat is not a number.\n"
        elif "4" in next:
            time.sleep(1)
            restaurant3()
        else:
            print "\tWhat now?\n"
def behindbar():
    clrscrn()
    time.sleep(1)
    print "\n"
    print "\tThe door behind the bar leads to a tiny kitchen."
    time.sleep(0.5)
    print "\n\tIt looks like someone was looking for something."
    time.sleep(0.5)
    print "\tThe floor is covered in broken plates and glasses."
    next = raw_input().lower()
    checkinput(next)
    time.sleep(0.25)
    print "\n"
    print "\tThe wall is covered in words."
    time.sleep(1)
    print"""\n
    1 [READ WALL]
    2 [GO BACK]\n"""
    time.sleep(0.5)
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "read" in next:
            time.sleep(0.5)
            print "\n"
            print('{:^110}'.format(color.RED + "| have %d ideas how to hold you tight" % codeA + color.END))
            print('{:^110}'.format(color.RED + "  you have %d dreams that you dream at night" % codeB + color.END))
            print('{:^110}'.format(color.RED + "we and %d dream of endless delight   " % codeC + color.END))
            print('{:^110}'.format(color.RED + "And we run run run till we see the light  " + color.END))
            print "\n"
            next = raw_input().lower()
            checkinput(next)
            restaurant3()
        elif "2" in next or "back" in next:
            restaurant3()
        else:
            print "\n\tWhat now?"

def firstclass():
    clrscrn()
    try:
        thread.start_new_thread(playsound10, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(2)
    print "\n\tYou've entered the first class compartment."
    time.sleep(0.5)
    print "\tIt couldn't be more obvious."
    time.sleep(1)
    print "\n\tAgainst the dispair, that in the rearward parts of the train was ever present,"
    time.sleep(0.5)
    print "\tthe opulence of this room seems very out of place."
    time.sleep(1)
    print "\n\tThe walls are covered in gold."
    time.sleep(0.5)
    print "\tA thick carpet covers the floor."
    time.sleep(0.5)
    print "\tThere are only a handful of seats."
    time.sleep(1.25)
    print """\n
    1 [LOOK AT WALLS]
    2 [LOOK AT SEATS]
    3 [GO AHEAD]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "wall" in next:
            time.sleep(0.5)
            print "\n\tYou examine the walls."
            time.sleep(0.5)
            print "\tWhat at first looked like expensive gold paneling under further inspection"
            print "\tturns out to be some sort of light gold painted wood."
            time.sleep(0.5)
            print "\n\tHere and there the peeling paint reveals that it is rotting."
            time.sleep(1)
        elif "2" in next or "seat" in next:
            time.sleep(0.5)
            print "\n\tThe seats are not like normal train seats."
            time.sleep(0.5)
            print "\tThey look more like those armchairs you would find in a mansion or fancy library."
            time.sleep(1)
            print "\n\tAs you look closely you find that the fabric of most of them is threadbare."
            time.sleep(0.5)
            print "\tThrough the almost transparent fabric you see the insides."
            time.sleep(0.5)
            print "\n\tThey are dark and moldy."
            time.sleep(1)
        elif "3" in next or "ahead" in next or "go" in next:
            time.sleep(0.5)
            print "\n\tYou start making your way to the other side of the room."
            time.sleep(0.5)
            print "\n\tThere is another door there."
            time.sleep(0.5)
            print "\tIt looks massive and heavy."
            time.sleep(2)
            clrscrn()
            time.sleep(1)
            print "\n"
            time.sleep(1)
            print color.PURPLE + "\tExcuse me.\n" + color.END
            time.sleep(1)
            next = raw_input().lower()
            checkinput(next)
            print "\tYou almost didn't see him."
            time.sleep(0.5)
            print "\tSitting in one of the tall armchairs turned slightly towards the window."
            time.sleep(1)
            print color.PURPLE + "\n\tI didn't want to startle you." + color.END
            time.sleep(1)
            print "\n\tHe gets up."
            time.sleep(0.5)
            print "\tHe is rather tall, his clothes simple yet of the highest quality."
            time.sleep(1)
            print "\n\tHis voice makes you shiver a little.\n"
            next = raw_input().lower()
            checkinput(next)
            print color.PURPLE + "\tNice to meet you. My name is John." + color.END
            time.sleep(0.5)
            print "\n\tHe holds out his hand, smiling warmly."
            time.sleep(0.5)
            print "\tYou shake it. It is strong and cold."
            time.sleep(1)
            print """\n
        1 [NICE TO MEET YOU TOO]
        2 [DO YOU KNOW WHERE WE ARE]
        3 [SORRY BUT... WHO ARE YOU]\n"""
            while True:
                next = raw_input("> ").lower()
                checkinput(next)
                if "1" in next or "nice" in next:
                    time.sleep(0.5)
                    print color.CYAN + "\n\tIt's nice to meet you too, John." + color.END
                    #time.sleep(0.5)
                    #print color.CYAN + "\tMy name is %s." %playername + color.END
                    time.sleep(0.5)
                    print color.CYAN + "\n\tIt's good to find another living soul on this train." + color.END
                    time.sleep(1)
                    print "\n\tHe laughs loudly."
                    time.sleep(0.5)
                    if "a" in fear:
                        print color.PURPLE + "\n\tYes, it would seem so." + color.END
                        time.sleep(1)
                        print "\tYou shiver."
                        next = raw_input().lower()
                        checkinput(next)
                        johnHARD()
                    print "\n\tYes. It's good to talk to someone."
                    next = raw_input().lower()
                    checkinput(next)
                    johnEASY()
                elif "2" in next or "where" in next:
                    time.sleep(0.5)
                    print color.CYAN + "\n\tWhere are we? Do you know?" + color.END
                    time.sleep(1)
                    print color.PURPLE + "\n\tAs far as I can tell we are on a train, wouldn't you agree?" + color.END
                    time.sleep(0.5)
                    if "a" in practical:
                        print color.PURPLE + "\n\tYou seem like the kind who would figure things out by yourself." + color.END
                        next = raw_input().lower()
                        checkinput(next)
                        johnEASY()
                    print color.PURPLE + "\tThat door that you came through has been locked the entire time I've been here." + color.END
                    time.sleep(1)
                    print """\n
        1 [YES I HAD TO FIGURE IT OUT]
        2 [REALLY? HOW LONG HAVE YOU BEEN HERE?\n]"""
                    while True:
                        next = raw_input("> ").lower()
                        checkinput(next)
                        if "1" in next or "yes" in next:
                            time.sleep(0.5)
                            print color.CYAN + "\n\tYes, it was the clock mechanism.\n\tI had to figure out how to stop it." + color.END
                            time.sleep(0.5)
                            print color.PURPLE + "\n\tReally? I'm impressed!" + color.END
                            time.sleep(0.5)
                            print color.PURPLE + "\n\tWhy don't you sit with me for a moment." + color.END
                            next = raw_input().lower()
                            checkinput(next)
                            johnHARD()
                        elif "2" in next or "really" in next:
                            time.sleep(0.5)
                            print color.CYAN + "\n\tReally? How long have you been here?" + color.END
                            time.sleep(0.5)
                            print color.PURPLE + "\n\tOh, a while. I don't really know. \n\tI do not own a watch, you know." + color.END
                            time.sleep(0.5)
                            print "\n\tHe lets his eyes wander over the room once."
                            time.sleep(0.5)
                            print color.PURPLE + "\n\tThis really is a gastly place." + color.END
                            next = raw_input().lower()
                            checkinput(next)
                            johnEASY()
                        else:
                            print "\n\tWhat now?"
                elif "3" in next or "sorry" in next or "who" in next:
                    time.sleep(0.5)
                    print color.CYAN + "\n\tI'm sorry but... Who are you?" + color.END
                    time.sleep(0.5)
                    print color.CYAN + "\tIt's just that I really want to get out of this place." + color.END
                    time.sleep(0.5)
                    print color.CYAN + "\tSo if you know anything about that, that would be great." + color.END
                    time.sleep(1)
                    print "\n\tHe smiles."
                    time.sleep(1)
                    print color.PURPLE + "\n\tYes of course." + color.PURPLE
                    time.sleep(0.5)
                    print color.PURPLE + "\tLet's sit down. I'm sure together we can figure something out." + color.END
                    next = raw_input().lower()
                    checkinput(next)
                    johnHARD()
                else:
                    print "\n\tWhat now?"

        else:
            print "\n\tWhat now?"

def johnEASY():
    clrscrn()
    time.sleep(0.5)
    print "\n"
    print "\tYou stand across from John."
    time.sleep(0.5)
    print "\tHe looks out the window."
    time.sleep(1)
    print color.PURPLE + "\n\tWhat did you say your name was?" + color.END
    time.sleep(1)
    print color.CYAN + "\n\tI didn't say anything." + color.END
    time.sleep(2)
    print "\n\tHe turns to look at you."
    time.sleep(1)
    print color.CYAN + "\n\tIt's %s." % playername + color.END
    time.sleep(0.5)
    next = raw_input().lower()
    checkinput(next)
    time.sleep(0.25)
    print color.PURPLE + "\n\tI have a riddle for you, %s." % playername + color.END
    time.sleep(1)
    print color.PURPLE + "\tWill you play?" + color.END
    time.sleep(1)
    print """\n
    1 [RIDDLE]
    2 [I'D RATHER NOT]"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "yes" in next:
            time.sleep(0.5)
            print color.CYAN + "\tSure, what's the riddle?" + color.END
            time.sleep(1)
            print "\n\tHe pauses for a moment. Then..."
            time.sleep(1)
            print "\n"
            print('{:^110}'.format(color.PURPLE + "A murderer is condemned to death. He has to choose between three rooms." + color.END))
            print('{:^110}'.format(color.PURPLE + "The first is full of raging fires, " + color.END))
            print('{:^110}'.format(color.PURPLE + "the second is full of assassins with loaded guns," + color.END))
            print('{:^110}'.format(color.PURPLE + "and the third is full of lions that haven't eaten in 3 years." + color.END))
            print "\n"
            print('{:^110}'.format(color.PURPLE + "Which room is safest for him?" + color.END))
            print "\n"
            time.sleep(1)
            while True:
                next = raw_input("> ").lower()
                checkinput(next)
                if "first" in next or "fire" in next or "1" in next:
                    time.sleep(0.5)
                    print color.PURPLE + "\n\tI'm afraid not." + color.END
                    time.sleep(3)
                    hell()
                elif "second" in next or "assassins" in next or "2" in next:
                    time.sleep(0.5)
                    print color.PURPLE + "\n\tI'm afraid not." + color.END
                    time.sleep(3)
                    hell()
                elif "third" in next or "lion" in next or "3" in next:
                    time.sleep(1)
                    print color.PURPLE + "\n\tThat... Is correct." + color.END
                    time.sleep(3)
                    locomotive()
        elif "2" in next or "back" in next:
            time.sleep(0.5)
            print color.PURPLE + "\n\tToo bad." + color.END
            time.sleep(3)
            hell()
        else:
            print "\n\tWhat now?"
def hell():
    clrscrn()
    try:
        thread.start_new_thread( playsound18, ("Thread-2", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(1)
    print "\n\tThe last thing you see is the carpet."
    time.sleep(1)
    print "\n\tIt too is rotten"
    time.sleep(1)
    print color.PURPLE + "\n\tThis whole world is rotten" + color.END
    time.sleep(3)
    print "\n\n\n"
    print('{:^110}'.format(color.PURPLE + "CONGRATULATIONS" + color.END))
    print "\n\n\n"
    win.append("john")
    time.sleep(1)
    print "\tPress ENTER to continue"
    next = raw_input().lower()
    checkinput(next)
    menu()
def johnHARD():
    clrscrn()
    time.sleep(0.5)
    print "\n"
    print "\tYou sit across from John."
    time.sleep(0.5)
    print "\tHe is looking right at you."
    time.sleep(1)
    print color.PURPLE + "\n\tWhat did you say your name was?" + color.END
    time.sleep(1)
    print color.CYAN + "\n\tI... I didn't say anything." + color.END
    time.sleep(2)
    print "\n\tA pause. He waits."
    time.sleep(1)
    print color.CYAN + "\n\tIt's %s." % playername + color.END
    time.sleep(0.5)
    next = raw_input().lower()
    checkinput(next)
    time.sleep(0.25)
    print color.PURPLE + "\n\t%s. It is so good that I met you." % playername + color.END
    time.sleep(2)
    print "\n\tHis face... There is something wrong with his face."
    time.sleep(2)
    print color.PURPLE + "\n\tDo you want to get off this train?" + color.END
    time.sleep(2)
    print color.PURPLE + "\n\tBecause I can help you with that." + color.END
    time.sleep(2)
    print color.PURPLE + "\n\tI will help you with that." + color.END
    time.sleep(2)
    print "\n\tHe pulls you out of you chair."
    time.sleep(2)
    print "\n\tHis eyes burn."
    time.sleep(3)
    print "\n\tHe pulls you into his arms..."
    time.sleep(4)
    if "glass shard" in inventory:
        clrscrn()
        time.sleep(0.5)
        print "\n\tThis is not what you wanted."
        time.sleep(1)
        print "\n\tNot how you want to go."
        time.sleep(1)
        print "\n\tYou grab the glass you got from Alice tightly."
        time.sleep(2)
        print "\n\tAnd you stab him with it."
        time.sleep(3)
        print "\n\tHis eyes are disbelieving as he slowly sinks to the ground."
        next = raw_input().lower()
        checkinput(next)
        print "\n\tYou hurry on"
        time.sleep(1)
    else:
        hell()
def locomotive():
    clrscrn()
    try:
        thread.start_new_thread(playsound14, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(0.5)
    print "\n"
    print "\tYou have entered the locomotive."
    time.sleep(0.5)
    print "\n\tBefore you you see the engine. It is enormous."
    time.sleep(0.5)
    print "\tIt takes up so much space that there is hardly any room for anything else."
    time.sleep(1)
    print "\n\tJust enough for one man."
    time.sleep(1)
    print "\n\tHe is sitting on a metal box."
    time.sleep(0.5)
    print "\tBoth his hands are working away at a console."
    time.sleep(1.5)
    print """\n
    1 [TALK TO HIM]
    2 [GO BACK]"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "talk" in next:
            time.sleep(0.5)
            conductor()
        elif "2" in next or "back" in next:
            time.sleep(0.5)
            firstclass2()
        else:
            print "\n\tWhat now?"
def firstclass2():
    try:
        thread.start_new_thread(playsound4, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(2)
    print "\n\tThe first class compartment."
    time.sleep(1)
    print """\n
    1 [LOOK AT WALLS]
    2 [LOOK AT ARMCHAIRS]
    3 [HEAVY DOOR]
    4 [BLACK DOOR]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "wall" in next:
            time.sleep(0.5)
            print "\n\tYou examine the walls."
            time.sleep(0.5)
            print "\n\tHere and there the peeling paint reveals rotting wood."
            time.sleep(1)
        elif "2" in next or "seat" in next:
            time.sleep(0.5)
            print "\n\tHeavy armchairs. The fabric is rotting."
            time.sleep(0.5)
            print "\n\tThey aren't fixed in place."
            time.sleep(1)
        elif "3" in next or "heavy" in next:
            time.sleep(1)
            locomotive()
        elif "4" in next or "black" in next:
            time.sleep(1)
            restaurant4()
def conductor():
    clrscrn()
    time.sleep(0.5)
    print color.CYAN + "\n\tExcuse me." + color.END
    time.sleep(1)
    print "\n\tHe jumps in his seat."
    time.sleep(0.5)
    print "\tHe glances over his shoulder."
    time.sleep(0.5)
    print "\tOnly for a second."
    time.sleep(1.5)
    print color.GREEN + "\n\tI have to ask you to leave. No entrance for passengers." + color.END
    time.sleep(1)
    print """\n
    1 [STAY]
    2 [GO BACK]"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "stay" in next:
            time.sleep(0.5)
            print color.CYAN + "\n\tPassenger? Are you..." + color.END
            time.sleep(1)
            print color.CYAN + "\n\tThis isn't a normal train. I know it." + color.END
            time.sleep(0.5)
            print color.GREEN + "\n\tI have to ask you to leave! \n\tNo entrance for passengers!" + color.END
            time.sleep(0.5)
            print "\n\tHe is shaking. You can see it from where you are standing."
            time.sleep(5)
            print color.CYAN + "\n\tMan, come on, what is going on here?!" + color.END
            time.sleep(2)
            print "\n\tYou cross the tiny room with two steps."
            time.sleep(2)
            print "\tYou are standing right next to him now."
            time.sleep(2)
            print "\n\tAnd now you see..."
            time.sleep(2)
            print "\n\tYou had thought his hands were working."
            time.sleep(2)
            print "\n\tBut really it is the machine that is working his hands."
            time.sleep(2)
            print color.GREEN + "\n\tI have to ask you to leave!" + color.END
            time.sleep(2)
            print "\n\tThere is panic in his voice."
            time.sleep(2)
            print color.GREEN + "\n\tNo entrance for passengers!" + color.END
            time.sleep(2)
            print "\n\tAnd then..."
            time.sleep(1)
            print "\n\tBefore you can even turn around."
            time.sleep(2)
            print "\n\tIt has you."
            time.sleep(3)
            print "\n\n\n\n"
            print('{:^110}'.format(color.RED + "YOU__________   " + color.END))
            print "\n\n\n"
            time.sleep(3)
            print "\n\n\n"
            print('{:^110}'.format(color.GREEN + "CONGRATULATIONS" + color.END))
            win.append("conductor")
            time.sleep(1)
            print "\tPress ENTER to continue"
            next = raw_input().lower()
            checkinput(next)
            menu()
        elif "2" in next or "back" in next:
            time.sleep(0.5)
            firstclass2()
        else:
            print "\n\tWhat now?"


def littlefriend():
    global chance
    chance = 0
    global creature
    global ran
    t = threading.Timer(6.0, OVER)
    dangerlevel = "low"
    if dangerlevel is "low":
        chance = randint(0, 4)
    elif dangerlevel is "high":
        chance = randint(0, 2)
    if chance is 1:
        try:
            thread.start_new_thread( playsound17, ("Thread-2", 2, ) )
        except:
            print "NO SOUND"
        time.sleep(0.25)
        print color.RED + """\n
                                        YOU____

                                            | SEE

                                     YOUUUUUUUU\n""" + color.END
        time.sleep(1.5)
        if creature is 0:
            print "\n\tA creature"
            time.sleep(0.2)
            print "\tAlmost 10 feet tall"
            time.sleep(0.2)
            print "\tIt's arms and legs are long"
            time.sleep(0.2)
            print "\tInstead of hands it has 20 claws, sharp like knives"
            time.sleep(0.5)
            print "\n\tIt starts coming towards you"
            time.sleep(1)
            t.start()
            print """\n
        1 [RUN]\n"""
            next = raw_input("> ").lower()
            checkinput(next)
            if "1" in next or "run" in next:
                time.sleep(0.25)
                t.cancel()
                ran = 1
                print "\n\tYou run."
                creature = 1
                time.sleep(0.25)
            else:
                time.sleep(1)
                over()
        elif creature is 1:
            print "\n\tThe creature"
            time.sleep(0.2)
            print "\tAlmost 10 feet tall"
            time.sleep(0.2)
            print "\tLong arms and legs"
            time.sleep(0.2)
            print "\tClaws, sharp like knives"
            time.sleep(0.5)
            print "\n\tIt starts coming towards you"
            time.sleep(1)
            t.start()
            print """\n
        1 [RUN]\n"""
            next = raw_input("> ").lower()
            checkinput(next)
            if "1" in next or "run" in next:
                time.sleep(0.25)
                t.cancel()
                ran = 1
                print "\n\tYou run."
                time.sleep(0.25)
            else:
                time.sleep(1)
                over()

def finalbirth():
    global creature
    creature = 0
    global dangerlevel
    dangerlevel = "none"
    clrscrn()
    try:
        thread.start_new_thread( playsound5, ("Thread-2", 2, ) )
    except:
        print "NO SOUND"
    print "\n"
    time.sleep(1.5)
    print color.CYAN + "\tWhere am I?" + color.END
    time.sleep(2)
    print color.CYAN + "\tHow did I get here?" + color.END
    time.sleep(2)
    print "\n\tThe last thing you remember,"
    time.sleep(1)
    print "\twhat is it?"
    time.sleep(1)
    print "\t..."
    time.sleep(0.5)
    print "\t..."
    time.sleep(0.5)
    print "\t..."
    time.sleep(1.5)
    print "\n\tNothing... "
    time.sleep(2)
    finalawake()
def finalawake():
    clrscrn()
    print "\n"
    print "\tYou look around."
    time.sleep(1.5)
    print "\tRows of seats."
    time.sleep(1)
    print "\tBig black windows."
    time.sleep(1)
    print "\tThe floor is shaking ever so slightly."
    time.sleep(2)
    finalsecond_class()
def finalsecond_class():
    clrscrn()
    print "\n\tYou get up."
    time.sleep(0.5)
    print "\tYou look around."
    time.sleep(1)
    print "\n\tThis is a train car."
    time.sleep(0.5)
    print "\tYou are on a train."
    time.sleep(0.5)
    print "\tDirty and run down."
    time.sleep(0.5)
    print "\tA dim lamp on the ceiling lights up the room."
    time.sleep(2)
    finalchoice()
def finalchoice():
    print """\n
    1 [LOOK AT WINDOW]
    2 [LOOK AT SEATS]
    3 [WOODEN DOOR]
    4 [METAL DOOR]\n"""
    doorunlocked = False
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "window" in next:
            print "\n\tYou look out the stained window infront of you."
            time.sleep(0.5)
            print "\tAll you see is darkness. Pitch black."
            time.sleep(0.5)
            print "\n\tNighttime."
            time.sleep(1)
            print """\n
    0 [EXAMINE WALL]"""
            finalchoice()
        elif "2" in next or "seat" in next:
            print "\n\tThere are only few seats here."
            time.sleep(0.5)
            finalchoice()
        elif "3" in next or "wood" in next or "wooden" in next or "left" in next:
            print "\n\tThe glass of the window is cracked and dirty."
            time.sleep(0.5)
            finalfourthcar()
        elif "4" in next or "metal" in next or "right" in next:
            time.sleep(0.5)
            finalrestaurant1()
        elif "0" in next or "examine" in next:
            time.sleep(0.25)
            print color.RED + """\n
                                        THE TROUBLE IS________""" + color.END
        else:
            print "\tWhat now?"
def finalsecond_class2():
    clrscrn()
    global ran
    dangerlevel = "low"
    littlefriend()
    if ran is 1:
        where = randint(0, 1)
        if where is 0:
            ran = 0
            finalfourthcar()
        elif where is 1:
            ran = 0
            finalrestaurant1()
    try:
        thread.start_new_thread( playsound15, ("Thread-3", 2, ) )
    except:
        print "NO SOUND"
    print "\n"
    print "\tYou are back in the second class car."
    time.sleep(0.5)
    finalchoice()
def finalfourthcar():
    clrscrn()
    global ran
    dangerlevel = "low"
    littlefriend()
    if ran is 1:
        where = randint(0, 1)
        if where is 0:
            finalsecond_class2()
        elif where is 1:
            finaloutside()
    try:
        thread.start_new_thread( playsound15, ("Thread-4", 2, ) )
    except:
        print "NO SOUND"
    print "\n"
    time.sleep(2)
    print "\tYou enter the next train car."
    time.sleep(0.5)
    print "\tA few dirty seats, black windows..."
    time.sleep(0.5)
    print "\tThe rearmost train car."
    time.sleep(0.5)
    print """\n
    1 [GO OUTSIDE]
    2 [GO BACK]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        time.sleep(0.5)
        if "2" in next or "back" in next:
            time.sleep(0.5)
            finalsecond_class2()
        elif "1" in next or "outside" in next:
            time.sleep(0.5)
            finaloutside()
def finalfourthcar2():
    clrscrn()
    global ran
    dangerlevel = "high"
    littlefriend()
    if ran is 1:
        where = randint(0, 1)
        if where is 0:
            finalsecond_class2()
        elif where is 1:
            finaloutside()
    try:
        thread.start_new_thread( playsound15, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    print "\n\tThis is the rearmost train car."
    time.sleep(1)
    print """
    1 [GO OUTSIDE]
    2 [GO TO SECOND CLASS]"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "outside" in next:
            time.sleep(1)
            finaloutside()
        elif "2" in next or "second" in next:
            time.sleep(1)
            finalsecond_class2()
        else:
            print "What now?"
def finaloutside():
    clrscrn()
    global ran
    dangerlevel = "low"
    littlefriend()
    if ran is 1 or ran is 0:
        finalfourthcar2()
    try:
        thread.start_new_thread( playsound16, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    print "\n"
    time.sleep(1)
    print "\tIt's very cold out here."
    time.sleep(0.5)
    print "\n\tYou can feel how the world disappearing into nothingness in front of you."
    time.sleep(0.5)
    print """\n
    1 [GO BACK]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "back" in next:
            finalfourthcar2()
        else:
            print "\n\tThere is nothing else to do here."
def finalrestaurant1():
    clrscrn()
    global ran
    dangerlevel = "high"
    littlefriend()
    if ran is 1:
        where = randint(0, 1)
        if where is 0:
            finalsecond_class2()
        elif where is 1:
            finalfirstclass()
    try:
        thread.start_new_thread( playsound15, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(1)
    print "\n\tThere are sitting booths along both walls."
    time.sleep(0.5)
    print "\tAt the far end you can see a bar."
    time.sleep(0.5)
    print "\tBehind it is a big hole in the wall."
    time.sleep(0.5)
    print "\n\tThere is also another door, a shiny black one."
    time.sleep(0.5)
    print "\n\tThe clock is ticking."
    time.sleep(1)
    print """\n
    1 [EXAMINE TABLES]
    2 [EXAMINE CLOCK]
    3 [EXAMINE BAR]
    4 [BLACK DOOR]
    5 [METAL DOOR]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "table" in next:
            time.sleep(0.5)
            print "\n\tThe table is bolted to the floor."
            print "\tAs are the upholstered chairs on either side."
            time.sleep(0.5)
            print "\n\tBoth the table and the chairs are covered in deep scratches."
            time.sleep(1)
        elif "2" in next or "clock"in next:
            finalclock1()
        elif "3" in next or "bar" in next:
            time.sleep(0.5)
            print"""\n
    1 [GO BACK]
    2 [CLIMB OVER BAR]\n"""
            while True:
                next = raw_input("> ").lower()
                checkinput(next)
                if "1" in next or "back" in next:
                    finalrestaurant1()
                elif "2" in next or "climb" in next:
                    print "\n\tYou climb over the bar."
                    finalbehindbar()
                else:
                    print "\n\tChose something."
        elif "4" in next or "black" in next:
            print "\n\tYou walk over to the black door."
            time.sleep(1)
            print "\n"
            print('{:^110}'.format(color.RED + "TIME IS RUNNING AGAINST YOU" + color.END))
            print "\n"
            time.sleep(1.5)
            finalfirstclass()
        elif "5" in next or "metal" in next:
            finalsecond_class2()
def finalclock1():
    clrscrn()
    try:
        thread.start_new_thread( playsound5, ("Thread-3", 2, ) )
    except:
        print "NO SOUND"
    print "\n"
    print "\tThe clock is ticking loudly."
def finalbehindbar():
    clrscrn()
    time.sleep(1)
    print "\n"
    print "\tA tiny kitchen."
    time.sleep(0.5)
    print "\tThe floor is covered in broken plates and glasses."
    time.sleep(0.25)
    print "\n"
    print "\tThe wall is smeared with words."
    time.sleep(1)
    print"""\n
    1 [READ WALL]
    2 [GO BACK]\n"""
    time.sleep(0.5)
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "read" in next:
            time.sleep(0.5)
            print "\n"
            print('{:^110}'.format(color.RED + "| have NO ideas how to hold you tight" + color.END))
            print('{:^110}'.format(color.RED + " you have NO dreams that you dream at night" + color.END))
            print('{:^110}'.format(color.RED + "we and NO dream of endless delight   " + color.END))
            print('{:^110}'.format(color.RED + "And we run run run _________              " + color.END))
            print "\n"
            next = raw_input().lower()
            checkinput(next)
            finalrestaurant1()
        elif "2" in next or "back" in next:
            finalrestaurant1()
        else:
            print "\n\tChose something."
def finalfirstclass():
    clrscrn()
    dangerlevel = "low"
    littlefriend()
    if ran is 1:
        where = randint(0, 1)
        if where is 0:
            finalrestaurant1()
        elif where is 1:
            finallocomotive()
    try:
        thread.start_new_thread(playsound15, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(2)
    print "\n\tThe first class compartment."
    time.sleep(1)
    print "\n\tThe walls are gold."
    time.sleep(0.5)
    print "\tA thick carpet covers the floor."
    time.sleep(0.5)
    print "\tA handful of big chairs."
    time.sleep(1.25)
    print """\n
    1 [LOOK AT WALLS]
    2 [LOOK AT ARMCHAIRS]
    3 [HEAVY DOOR]
    4 [BLACK DOOR]\n"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "wall" in next:
            time.sleep(0.5)
            print "\n\tYou examine the walls."
            time.sleep(0.5)
            print "\n\tHere and there the peeling paint reveals rotting wood."
            time.sleep(1)
        elif "2" in next or "seat" in next:
            time.sleep(0.5)
            print "\n\tHeavy armchairs. The fabric is rotting."
            time.sleep(0.5)
            print "\n\tThey aren't fixed in place."
            time.sleep(0.5)
            print "\n\tMaybe they could be picked up."
            time.sleep(1)
        elif "3" in next or "heavy" in next:
            time.sleep(1)
            finallocomotive()
        elif "4" in next or "black" in next:
            time.sleep(1)
            finalrestaurant1()
        elif "take" in next or "pick" in next or "get" in next or "lift" in next or "use chair" in next:
            time.sleep(0.5)
            print "\n\tYou pick up the armchair."
            time.sleep(0.5)
            print "\n\tIt is not as heavy as you thought."
            time.sleep(1)
            print """\n
    1 [USE CHAIR TO STOP THE TRAIN]\n"""
            while True:
                next = raw_input("> ").lower()
                checkinput(next)
                if "1" in next:
                    trainstop()
                else:
                    print "\tIt is time to end this."

        else:
            print "\n\tChoose something."
def finallocomotive():
    clrscrn()
    try:
        thread.start_new_thread(playsound14, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(0.5)
    print "\n"
    print "\tThe locomotive."
    time.sleep(0.5)
    print "\n\tYou see the engine. It is enormous."
    time.sleep(0.5)
    print "\n\tA monster that needs to be stopped."
    time.sleep(1.5)
    print """\n
    1 [GO BACK]"""
    while True:
        next = raw_input("> ").lower()
        checkinput(next)
        if "1" in next or "back" in next:
            finalfirstclass()
        else:
            print "\n\tThere is nothing else to do here."
def trainstop():
    clrscrn()
    try:
        thread.start_new_thread(playsound14, ("Thread-1", 2, ) )
    except:
        print "NO SOUND"
    time.sleep(1)
    print "\n"
    print "\tYou half carry half drag the huge armchair through the door that leads to the locomotive"
    time.sleep(2)
    print "\n\tYou can hear the creature approaching from behind"
    time.sleep(2)
    print "\n\tBut you don't care"
    time.sleep(2)
    print "\n\tWith all your might you swing the chair up in the air"
    time.sleep(3)
    print "\n\n\tAnd throw it at the machine..."
    time.sleep(4)
    titles()

def quit():
    print color.YELLOW + "\n\n\tThank you for playing.\n" + color.END
    time.sleep(2)
    clrscrn()
    exit(0)

menu()
