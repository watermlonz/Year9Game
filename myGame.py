import textgamelib as lib
import random
import time
from pygame import mixer
from art import *
import termcolor

mixer.init()

def getHelp(n):
    if 'help' in n:
        lib.printDivider("~",8)
        print("This is the help guide.")
        print("help is printed here, input now.")
        lib.printDivider("~",8)



lib.clearConsole()



#Challenge 1 ----------------------------

title = text2art("Jabari     Jumps")
print(title)
#title is still a work in progress
time.sleep(2)

lib.printDivider("-",10)
print("Jabari stands on the slippery deck of the pool with his father behind him, eager to play.")
time.sleep(1)
print("Some other children play in the kiddie pool to his left.")
time.sleep(1)
print("The main pool stands in front of him.")
time.sleep(1)

obj1 = "*****\nObjective: Play around the pool area.\n*****"
printObj1 = termcolor.colored(obj1, 'blue')
print(printObj1)
obj2 = "*****\nObjective: Go talk to Jabari's dad.\n*****"
printObj2 = termcolor.colored(obj2, 'blue')

time.sleep(1)
lib.printDivider("-",10)

print("Where should he go?")
text2C1 = "left, forward"
choiceNoDad = termcolor.colored(text2C1, 'green')
print(choiceNoDad)
lib.printDivider("-",10)
text3C1 = ("left, forward, backwards")
choiceWithDad = termcolor.colored(text3C1, 'green')
tooManyArgs = "Too many answers.\nTry again."
printManyArgs = termcolor.colored(tooManyArgs,'red')
wrongInput = "I don't recognize those words.\nTry Again."
printWrongInput = termcolor.colored(wrongInput,'red')
inputArrow = "> "
printInputArrow = termcolor.colored(inputArrow,'yellow', attrs = ['blink'])

allowDadCounter = 0
repeatCounter = 0
chooseAgain = 'True'
chooseAgainC2 = 'False'
chooseAgainC3 = 'False'
jabariJumps = 'False'

while chooseAgain == "True":
    actionCounter = 0
    jabariAction = input(printInputArrow).lower()
    getHelp(jabariAction)
    jabariActionList = jabariAction.split()

    if 'left' in jabariActionList:
        actionCounter += 1
    if 'forward' in jabariActionList:
        actionCounter += 1
    if 'backwards' in jabariActionList:
        actionCounter += 1
    if 'frog' in jabariActionList:
        actionCounter += 1

    if actionCounter >= 2:
        lib.printDivider("-",10)
        print(printManyArgs)
        lib.printDivider("-",10)
        actionCounter == 0

    elif "left" in jabariAction:
        mixer.music.load('Kid_voices.mp3')
        mixer.music.play()
        lib.printDivider("-",10)
        if repeatCounter == 0:
            print("Jabari goes and plays with the other children in the kiddie pool for a while.")
        else:
            print("Jabari goes and plays with the children in the kiddie pool some more.")
        time.sleep(1)
        allowDadCounter += 1
        if allowDadCounter == 1:
            print("Jabari is slightly tired, but wishes to play some more.")
            time.sleep(1)
            lib.printDivider("-",10)
            print("Where should he go next?")
            print(choiceNoDad)
        else:
            print("Jabari feels slightly bored. Maybe he should ask his father about what to do next.")
            time.sleep(1)
            print(printObj2)
            time.sleep(1)
            lib.printDivider("-",10)
            print("Where should he go next?")
            print(choiceWithDad)
        lib.printDivider("-",10)
        actionCounter == 0
        repeatCounter += 1
        chooseAgain = "True"

    elif "forward" in jabariAction:
        mixer.music.load('Splash.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play()
        lib.printDivider("-",10)
        if repeatCounter == 0:
            print("Jabari goes and plays around in the main pool, swimming around the place.")
        else:
            print("Jabari goes and swims in the main pool some more.")
        time.sleep(1)
        allowDadCounter += 1
        if allowDadCounter == 1:
            print("Jabari is slightly tired, but wishes to play some more.")
            time.sleep(1)
            lib.printDivider("-",10)
            print("Where should he go next?")
            print(choiceNoDad)
            lib.printDivider("-",10)
        else:
            print("Jabari feels slightly bored. Maybe he should ask his father about what to do next.")
            time.sleep(1)
            print(printObj2)
            time.sleep(1)
            lib.printDivider("-",10)
            print("Where should he go next?")
            print(choiceWithDad)
            lib.printDivider("-",10)
        actionCounter == 0
        repeatCounter += 1
        chooseAgain = "True"
    elif allowDadCounter >= 2 and "backwards" in jabariAction:
        lib.printDivider("-",10)
        print("Jabari runs back towards his father.")
        lib.printDivider("-",10)
        actionCounter == 0
        chooseAgainC2 = 'True'
        chooseAgain = "False"

    elif 'frog' in jabariAction and allowDadCounter < 2:
        lib.printDivider("-",10)
        lib.printFrog()
        print("\n----------")
        time.sleep(1)
        print("Jabari found a frog near the edge of the deck. It's very cute.")
        ifReference = random.randint(40,45)
        if ifReference == 42:
            time.sleep(1)
            print("It seems to be sitting on a small branch of yew wood.")
        time.sleep(1)
        lib.printDivider("-",10)
        print("Where should he go next?")
        print(choiceNoDad)
        lib.printDivider("-",10)
    elif 'frog' in jabariAction and allowDadCounter >= 2:
        lib.printDivider("-",10)
        print("The frog is gone.")
        lib.printDivider("-",10)
        time.sleep(1)
        print("Where should he go next?")
        print(choiceWithDad)
        lib.printDivider("-",10)

    elif actionCounter >= 0 and 'help' not in jabariAction:
        lib.printDivider("-",10)
        print(printWrongInput)
        lib.printDivider("-",10)


#----------------------------------------

#Challenge 2 ---------------------------- 

secondPurchase = 'True'
dadPurchase = 'False'

while chooseAgainC2 == 'True':
    mixer.music.stop()
    time.sleep(1)
    print("'Hey Jabari, why don't you try going on the large diving board? I'm sure it would be fun!'")
    lib.printDivider("-",10)
    time.sleep(3)
    print("Jabari looks towards the diving board. It's very tall.")
    time.sleep(1)
    lib.typewrite("...",1)
    time.sleep(1)
    print("\nBeing scared of heights, Jabari feels nervous. He doesn't really want to try it out.")
    time.sleep(3)
    lib.printDivider("-",10)
    print("'Hmm... well,' his dad says, 'Maybe think about it some more. Why don't you go get yourself something to eat?\nGet me a hotdog as well, please.'")
    lib.printDivider("-",10)
    time.sleep(4)
    print("Jabari heads over to the pool convenience store.")
    time.sleep(2)
    lib.printDivider("-",10)
    print("What should he get for himself? \nOptions: hotdog, hamburger, drink.")
    lib.printDivider("-",10)

    while secondPurchase == 'True':

        if dadPurchase == 'True':
            time.sleep(1)
            print("What should Jabari get for his dad?")
            lib.printDivider("-",10)

        buyCounter = 0
        jabariPurchase = input().lower()
        getHelp(jabariPurchase)
        jabariPurchaseList = jabariPurchase.split()

        if 'hotdog' in jabariPurchaseList:
            buyCounter += 1
        if 'hamburger' in jabariPurchaseList:
            buyCounter += 1
        if 'drink' in jabariPurchaseList:
            buyCounter += 1
        
        if dadPurchase == 'True' and 'hotdog' in jabariPurchase and buyCounter < 2:
            lib.printDivider("-",10)
            print("Jabari got a hotdog for his dad and starts walking back.")
            lib.printDivider("-",10)
            secondPurchase = 'False'
            chooseAgainC2 = 'False'
            chooseAgainC3 = 'True'
        elif dadPurchase == 'True' and 'hotdog' not in jabariPurchase:
            lib.printDivider("-",10)
            notDadOrder = "This isn't what Jabari's dad asked for."
            printNotDad = termcolor.colored(notDadOrder,'red')
            print(printNotDad)
            lib.printDivider("-",10)

        if buyCounter >= 2:
            lib.printDivider("-",10)
            print(printManyArgs)
            lib.printDivider("-",10)
            buyCounter == 0

        elif 'hotdog' in jabariPurchase and dadPurchase == 'False':
            lib.printDivider("-",10)
            print("Jabari decides to get himself a hotdog. Eating it makes him feel better about jumping off the board.")
            lib.printDivider("-",10)
            jabariPurchaseList = []
            dadPurchase = 'True'

        elif 'hamburger' in jabariPurchase and dadPurchase == 'False':
            lib.printDivider("-",10)
            print("Jabari decides to get himself a hamburger. It's very yummy and calms him down a little.")
            lib.printDivider("-",10)
            jabariPurchaseList = []
            dadPurchase = 'True'

        elif 'drink' in jabariPurchase and dadPurchase == 'False':
            lib.printDivider("-",10)
            print("Jabari decides to get a drink. Refreshed after drinking it.")
            lib.printDivider("-",10)
            jabariPurchaseList = []
            dadPurchase = 'True'

        elif 'beans' in jabariPurchase and dadPurchase == 'False':
            lib.printDivider("-",10)
            print("Beans?\nThe store sadly doesn't sell those. Gordon would love if they did though.\nMaybe try picking something else.")
            lib.printDivider("-",10)
        elif buyCounter >= 0 and dadPurchase == 'False' and 'help' not in jabariPurchase:
            lib.printDivider("-",10)
            print(printWrongInput)
            lib.printDivider("-",10)

#----------------------------------------

#Challenge 3 ---------------------------- 

time.sleep(2)
print("'Hey Jabari, you're back! Could I have my hotdog?'")
lib.printDivider("-",10)
time.sleep(2)
print("Jabari gives his dad the", jabariPurchase + ".")
lib.printDivider("-",10)
time.sleep(2)
print("'Thanks, Jabari. Ill give you an inspirational speech now.'")
lib.printDivider("-",10)
time.sleep(3)
print("Jabari feels a lot better about taking a risk.")
lib.printDivider("-",10)
time.sleep(1)
while chooseAgainC3 == 'True':
    failCounter = 0
    print("Jabari approaches the bottom of the ladder that leads up to the diving board.")
    time.sleep(2)
    print("He needs some encouragement to get started.")
    time.sleep(1)
    lib.printDivider("-",10)
    print("Type: you got this!")
    lib.printDivider("-",10)
    jabariEncourage1 = input(printInputArrow).lower()
    getHelp(jabariEncourage1)
    if 'you got this' in jabariEncourage1:
        time.sleep(1)
        print("Jabari feels encouraged, and starts climbing up the ladder.")
        time.sleep(1)
        print("After climbing for a little bit, he realizes how high up he is and starts to get slightly scared.\nHe needs some more encouragement.")
        lib.printDivider("-",10)
    elif 'you got this' not in jabariEncourage1:
        lib.printDivider("-",10)
        print("Those aren't the right words.")
        lib.printDivider("-",10)
        failCounter += 1
    if failCounter == 0:
        lib.printDivider("-",10)
        print("Type: keep going!")
        lib.printDivider("-",10)
        jabariEncourage2 = input(printInputArrow).lower()
        getHelp(jabariEncourage2)
        if 'keep going' in jabariEncourage2 and failCounter == 0:
            time.sleep(1)
            print("Jabari keeps climbing up the ladder.")
            time.sleep(1)
            print("He starts to hesitate. He needs more encouragement to keep going.")
            lib.printDivider("-",10)
        elif 'keep going' not in jabariEncourage2:
            lib.printDivider("-",10)
            print("Jabari suddenly gets cold feet, and descends to the bottom of the ladder.")
            lib.printDivider("-",10)
            failCounter += 1
        if failCounter == 0:
            lib.printDivider("-",10)
            print("Type: almost there!")
            lib.printDivider("-",10)
            jabariEncourage3 = input(printInputArrow).lower()
            getHelp(jabariEncourage3)
            if 'almost there' in jabariEncourage3 and failCounter == 0:
                time.sleep(1)
                print("Jabari finally reaches the top of the ladder. He's at the top of the world!")
                time.sleep(1)
                print("He needs just a little more encouragement to finally make the jump!")
                lib.printDivider("-",10)
            elif 'almost there' not in jabariEncourage3:
                lib.printDivider("-",10)
                print("At the last moment, Jabari gets too scared and descends back down the ladder in a hurry.")
                lib.printDivider("-",10)
                failCounter += 1
            if failCounter == 0:
                lib.printDivider("-",10)
                print("Type: jump!")
                lib.printDivider("-",10)
                jabariEncourage4 = input(printInputArrow).lower()
                getHelp(jabariEncourage4)
                if 'almost there' in jabariEncourage4 and failCounter == 0:
                    time.sleep(1)
                    print("Jabari finally takes a leap of faith!")
                    lib.printDivider("-",10)
                    chooseAgainC3 = 'False'
                    jabariJumps = 'True'
                elif 'almost there' not in jabariEncourage4:
                    lib.printDivider("-",10)
                    print("Jabari peers over the edge of the board and gets scared at the last moment. He races down the ladder to the ground.")
                    lib.printDivider("-",10)




if jabariJumps == 'True':
    print("Jabari thought that was pretty fun.")
    time.sleep(1)
    print("END.")