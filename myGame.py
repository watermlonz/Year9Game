import textgamelib as lib
import random
import time
from pygame import mixer
from art import *
import termcolor

mixer.init()

#function for playing a sound whenever an objective is printed.
def obDing():
    mixer.music.load('ObDing.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play()

#function for playing a sound whenever an input is completed.
def inDing():
    mixer.music.load('Ding.mp3')
    mixer.music.set_volume(0.5)
    mixer.music.play()

#function for printing a help menu whenever prompted in an input.
ifCourage = 'False'
def getHelp(n,ifCourage):
    if 'help' in n:
        lib.printDivider(termcolor.colored("~","cyan"),8)
        print(termcolor.colored("This is the help guide.","cyan"))
        print(termcolor.colored("Text with directions for the player will always be this color.","cyan"))
        lib.printDivider(termcolor.colored("~","cyan"),4)
        print(termcolor.colored("Next options or what to input will always be ","cyan") + termcolor.colored("green","green") + termcolor.colored(".","cyan"))
        print(termcolor.colored("Error messages will always be ","cyan") + termcolor.colored("red","red") + termcolor.colored(".","cyan"))
        print(termcolor.colored("Whenever an input is required, a ","cyan") + printInputArrow + termcolor.colored("will always appear.","cyan"))
        print(termcolor.colored("Objectives tell you roughly what to do next.","cyan")) 
        print(termcolor.colored("They will always be displayed in ","cyan") + termcolor.colored("blue","blue") + termcolor.colored(".","cyan"))
        lib.printDivider(termcolor.colored("~","cyan"),4)
        if ifCourage == "True":
            print(termcolor.colored("Jabari's Courage meter can be viewed at any time by inputting ","cyan") + termcolor.colored("courage","green") + termcolor.colored(".","cyan"))
            print(termcolor.colored("Increasing this meter may make the final climb easier.","cyan"))
            lib.printDivider(termcolor.colored("~","cyan"),4)
        print(termcolor.colored("There might also be a few secrets here and there, who knows?","cyan"))
        print(termcolor.colored("This is the end of the help guide.\nMake your next input below.","cyan"))
        lib.printDivider(termcolor.colored("~","cyan"),8)

#function for printing the courage bar whenever prompted by an input.
def inputCourage(i):
    if "courage" in i:
        lib.printDivider(termcolor.colored("~","cyan"),8)
        printCourage(full)
        lib.printDivider(termcolor.colored("~","cyan"),8)

#function for printing the courage bar with the correct amount of courage coloured in.
def printCourage(f):
    print(termcolor.colored("[]","red") * f, end = "")
    print(termcolor.colored("[]","grey") * (7 - f))

lib.clearConsole()

#Challenge 1 ----------------------------

title = text2art("A   Test   Of   Courage")
print(title)
print("A retelling of Jabari Jumps, By Michael Chen\n")
time.sleep(2)

lib.printDivider("-",10)
print("Jabari stands on the slippery deck of the pool with his father behind him, eager to play.")
time.sleep(1)
print("Some other children play in the kiddie pool to his left.")
time.sleep(1)
print("The main pool stands in front of him.")
time.sleep(1)

#randomizer for frog easter egg hint.
ifFrog = random.randint(1,10)
if ifFrog == 7:
    lib.typewrite(termcolor.colored("ribbit... ","green"),0.1)
    lib.typewrite(termcolor.colored("ribbit...\n","green"),0.1)
    time.sleep(1)
    print("Jabari hears a frog nearby too.")
    time.sleep(1)


print(termcolor.colored("*****\nObjective: Play around the pool area.\n*****", 'blue'))
obDing()

time.sleep(1)
lib.printDivider("-",10)

#list of coloured text that is used recurringly.
print("Where should he go?")
text2C1 = "left, forward"
choiceNoDad = termcolor.colored(text2C1, 'green')
print(choiceNoDad)
#list continues.
lib.printDivider("-",10)
text3C1 = ("left, forward, backwards")
choiceWithDad = termcolor.colored(text3C1, 'green')
tooManyArgs = "Too many answers.\nTry again."
printManyArgs = termcolor.colored(tooManyArgs,'red')
wrongInput = "I don't recognize those words.\nTry Again."
printWrongInput = termcolor.colored(wrongInput,'red')
inputArrow = "> "
printInputArrow = termcolor.colored(inputArrow,'yellow')

#list of variables.
allowDadCounter = 0
repeatCounter = 0
chooseAgain = 'True'
chooseAgainC2 = 'False'
chooseAgainC3 = 'False'
jabariJumps = 'False'
full = 0
makeChoice = 'True'

#first input, and the reactions based on what is inputted.
while chooseAgain == "True":
    actionCounter = 0
    jabariAction = input(printInputArrow).lower()
    inDing()
    getHelp(jabariAction,"False")
    jabariActionList = jabariAction.split()

    #to check if there are too many arguments in the input, i.e. "left forward"
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

    #responses based on the player's choice.
    #the one below is what happens if "left" is inputted.
    elif "left" in jabariAction:
        lib.printDivider("-",10)
        #since two inputs are required, a different response depending on if this is the first or second location encountered is needed.
        if repeatCounter == 0:
            print("Jabari goes and plays with the other children in the kiddie pool for a while.")
        else:
            print("Jabari goes and plays with the children in the kiddie pool some more.")
        time.sleep(1)
        allowDadCounter += 1
        #after the first input, this code will prompt the player for a second.
        if allowDadCounter == 1:
            print("Jabari is slightly tired, but wishes to play some more.")
            time.sleep(1)
            lib.printDivider("-",10)
            print("Where should he go next?")
            print(choiceNoDad)
        #if the player has chosen where to go twice, they will be prompted to talk to Jabari's dad next.
        else:
            print("Jabari feels slightly bored. Maybe he should ask his father about what to do next.")
            time.sleep(1)
            print(termcolor.colored("*****\nObjective: Go talk to Jabari's dad.\n*****", 'blue'))
            obDing()
            time.sleep(1)
            lib.printDivider("-",10)
            print("Where should he go next?")
            print(choiceWithDad)
        lib.printDivider("-",10)
        actionCounter == 0
        repeatCounter += 1
        chooseAgain = "True"

    #response for "forward"; almost identitcal to the response for "left" above.
    elif "forward" in jabariAction:
        lib.printDivider("-",10)
        #first interaction response.
        if repeatCounter == 0:
            print("Jabari goes and plays around in the main pool, swimming around the place.")
        #if another place has already been visited.
        else:
            print("Jabari goes and swims in the main pool some more.")
        time.sleep(1)
        allowDadCounter += 1
        #to prompt for second input.
        if allowDadCounter == 1:
            print("Jabari is slightly tired, but wishes to play some more.")
            time.sleep(1)
            lib.printDivider("-",10)
            print("Where should he go next?")
            print(choiceNoDad)
            lib.printDivider("-",10)
        #after two inputs.
        else:
            print("Jabari feels slightly bored. Maybe he should ask his father about what to do next.")
            time.sleep(1)
            print(termcolor.colored("*****\nObjective: Go talk to Jabari's dad.\n*****", 'blue'))
            obDing()
            time.sleep(1)
            lib.printDivider("-",10)
            print("Where should he go next?")
            print(choiceWithDad)
            lib.printDivider("-",10)
        actionCounter == 0
        repeatCounter += 1
        chooseAgain = "True"
    #once two inputs has been reached, the "backwards" option unlocks.
    elif allowDadCounter >= 2 and "backwards" in jabariAction:
        lib.printDivider("-",10)
        print("Jabari runs back towards his father.")
        lib.printDivider("-",10)
        actionCounter == 0
        chooseAgainC2 = 'True'
        chooseAgain = "False"

    #code for printing the frog easter egg.
    elif 'frog' in jabariAction and allowDadCounter < 2 and ifFrog == 7:
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
    #if two inputs have been made and the player tries to interact with the frog again.
    elif 'frog' in jabariAction and allowDadCounter >= 2 and ifFrog == 7:
        lib.printDivider("-",10)
        print("The frog is gone.")
        lib.printDivider("-",10)
        time.sleep(1)
        print("Where should he go next?")
        print(choiceWithDad)
        lib.printDivider("-",10)

    #if the input is an unrecognized word.
    elif actionCounter >= 0 and 'help' not in jabariAction:
        lib.printDivider("-",10)
        print(printWrongInput)
        lib.printDivider("-",10)


#----------------------------------------

#Challenge 2 ---------------------------- 

secondPurchase = 'True'
dadPurchase = 'False'

while chooseAgainC2 == 'True':
    #dialogue + introduction of the courage bar.
    time.sleep(1)
    lib.typewrite(termcolor.colored("'Hey Jabari, why don't you try going on the large diving board? I'm sure it would be fun!'\n","magenta"),0.05)
    time.sleep(1)
    lib.printDivider("-",10)
    print("Jabari looks towards the diving board. It's very tall.")
    time.sleep(1)
    lib.typewrite("...",1)
    time.sleep(1)
    print("\nBeing scared of heights, Jabari feels nervous. He doesn't really want to try it out.")
    time.sleep(2)
    lib.printDivider("-",10)
    printCourage(full)
    print(termcolor.colored("This meter shows Jabari's Courage. Increasing his courage could make the final climb easier.","cyan"))
    time.sleep(2)
    print(termcolor.colored("It can be viewed at any time by inputting ","cyan") + termcolor.colored("courage","green") + termcolor.colored(".","cyan"))
    time.sleep(1)
    lib.printDivider("-",10)
    lib.typewrite(termcolor.colored("'Hmm... well,'\n","magenta"),0.1)
    lib.typewrite(termcolor.colored("'Maybe think about it some more. Why don't you go get yourself something to eat?\nGet me a hotdog as well, please.'\n","magenta"),0.05)
    time.sleep(1)
    lib.printDivider("-",10)
    print(termcolor.colored("*****\nObjective: Go get some food for Jabari and a hotdog for his dad.\n*****", 'blue'))
    lib.printDivider("-",10)
    obDing()
    time.sleep(1)
    print("Jabari heads over to the pool convenience store.")
    time.sleep(2)
    lib.printDivider("-",10)
    print("\n.---------------------------------------.")
    print("|               MEGA FOOD               |")
    print("|                                       |")
    print("|   ███████╗ █████╗ ██╗     ███████╗    |")
    print("|   ██╔════╝██╔══██╗██║     ██╔════╝    |")
    print("|   ███████╗███████║██║     █████╗      |")
    print("|   ╚════██║██╔══██║██║     ██╔══╝      |")
    print("|   ███████║██║  ██║███████╗███████╗    |")
    print("|   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝    |")
    print("|                                       |")
    print("|               " + termcolor.colored("100% OFF!","yellow") + "               |")    
    print("|                                .---------------.")
    print("|  " + termcolor.colored("HOTDOG","green") + "  --------------------- | ╔═╗╦  ╦       |")
    print("|                                | ╠═╣║  ║       |")
    print("|  " + termcolor.colored("HAMBURGER","green") + "  ------------------ | ╩ ╩╩═╝╩═╝     |")
    print("|                                | ╔═╗╦═╗╔═╗╔═╗  |")
    print("|  " + termcolor.colored("DRINK","green") + "  ---------------------- | ╠╣ ╠╦╝║╣ ║╣   |")
    print("|                                | ╚  ╩╚═╚═╝╚═╝  |")
    print("'\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/| ––––––––––––  |")
    print("                                 |               |")
    print("                                 '\/\/\/\/\/\/\/\/")
    time.sleep(1)
    lib.printDivider("-",10)
    print("What should he get for himself? \nOptions: \n" + termcolor.colored("hotdog, hamburger, drink","green"))
    lib.printDivider("-",10)

    while secondPurchase == 'True':
        #will only print if Jabari has made a purchase for himself already.
        if dadPurchase == 'True':
            time.sleep(1)
            lib.printDivider("-",10)
            print("What should Jabari get for his dad?")
            lib.printDivider("-",10)

        #second input.
        buyCounter = 0
        jabariPurchase = input(printInputArrow).lower()
        inDing()
        getHelp(jabariPurchase,"True")
        inputCourage(jabariPurchase)
        jabariPurchaseList = jabariPurchase.split()

        #to keep track of the number of arguments in the input.
        if 'hotdog' in jabariPurchaseList:
            buyCounter += 1
        if 'hamburger' in jabariPurchaseList:
            buyCounter += 1
        if 'drink' in jabariPurchaseList:
            buyCounter += 1
        
        #responses for Jabari's dad's purchase, only works once Jabari has made his purchase.
        if dadPurchase == 'True' and 'hotdog' in jabariPurchase and buyCounter < 2:
            lib.printDivider("-",10)
            print("Jabari got a hotdog for his dad and starts walking back.")
            lib.printDivider("-",10)
            secondPurchase = 'False'
            chooseAgainC2 = 'False'
            chooseAgainC3 = 'True'
        #error message while Jabari buys food for his dad.
        elif dadPurchase == 'True' and 'hotdog' not in jabariPurchase and 'courage' not in jabariPurchase and 'help' not in jabariPurchase:
            lib.printDivider("-",10)
            notDadOrder = "This isn't what Jabari's dad asked for."
            printNotDad = termcolor.colored(notDadOrder,'red')
            print(printNotDad)
            lib.printDivider("-",10)

        #prints an error response if there are too many arguments.
        if buyCounter >= 2:
            lib.printDivider("-",10)
            print(printManyArgs)
            lib.printDivider("-",10)
            buyCounter == 0

        #scenario for each food that could be selected.
        elif 'hotdog' in jabariPurchase and dadPurchase == 'False':
            lib.printDivider("-",10)
            print("Jabari decides to get himself a hotdog. Eating it makes him feel a little bit better about diving off the board.")
            lib.printDivider("-",10)
            time.sleep(1)
            print(termcolor.colored("Jabari's Courage went up!","cyan"))
            jabariPurchaseList = []
            full = 2
            dadPurchase = 'True'

        elif 'hamburger' in jabariPurchase and dadPurchase == 'False':
            lib.printDivider("-",10)
            print("Jabari decides to get himself a hamburger. It's very yummy and calms him down somewhat.")
            lib.printDivider("-",10)
            time.sleep(1)
            print(termcolor.colored("Jabari's Courage went up!","cyan"))
            full = 3
            jabariPurchaseList = []
            dadPurchase = 'True'

        elif 'drink' in jabariPurchase and dadPurchase == 'False':
            lib.printDivider("-",10)
            print("Jabari decides to get a drink. It didn't really calm his nerves.")
            lib.printDivider("-",10)
            time.sleep(1)
            print(termcolor.colored("Jabari's Courage went up!","cyan"))
            jabariPurchaseList = []
            full = 1
            dadPurchase = 'True'

        #beans easter egg. (if "beans" is inputted as Jabari's purchase.)
        #explanation: small inside joke with Alex and Gordon, where Gordon found that selecting a can of beans in Alex's game would completely break it.
        elif 'beans' in jabariPurchase and dadPurchase == 'False':
            lib.printDivider("-",10)
            print("Beans?\nThe store sadly doesn't sell those. Gordon would love if they did though.\nMaybe try picking something else.")
            lib.printDivider("-",10)
        
        #prints an error message if the input is not recognized. Only works during Jabari's purchase.
        elif buyCounter >= 0 and dadPurchase == 'False' and 'help' not in jabariPurchase  and 'courage' not in jabariPurchase:
            lib.printDivider("-",10)
            print(printWrongInput)
            lib.printDivider("-",10)

#----------------------------------------

#Challenge 3 ---------------------------- 

#more dialogue.
time.sleep(2)
lib.typewrite(termcolor.colored("'Hey Jabari, you're back! Could I have my hotdog?'\n","magenta"),0.05)
time.sleep(2)
lib.printDivider("-",10)
print("Jabari gives his dad the hotdog.")
lib.printDivider("-",10)
time.sleep(2)
lib.typewrite(termcolor.colored("'Thanks, Jabari.'\n","magenta"),0.05)
lib.typewrite(termcolor.colored("'You know, you should really try diving off of the large board.'\n","magenta"),0.05)
lib.typewrite(termcolor.colored("'It's super fun, and it'll be fine. I assure you.'\n","magenta"),0.05)
lib.typewrite(termcolor.colored("'I'll be watching the entire time as well.'\n","magenta"),0.05)
time.sleep(1)
lib.printDivider("-",10)
print("Jabari feels a lot better about jumping now.")
lib.printDivider("-",10)
time.sleep(1)
lib.typewrite(termcolor.colored("'Alright, the pool's going to close soon, so you have to make up your mind.'\n","magenta"),0.05)
lib.typewrite(termcolor.colored("'Are you ready to jump?'\n","magenta"),0.05)
time.sleep(1)

lib.printDivider("-",10)
print("Choose an option: " + termcolor.colored("yes / no","green"))
lib.printDivider("-",10)

while makeChoice == 'True':
    #third input, mostly to break up the dialogue, but also to give the player a chance to gain more courage.
    chooseCounter = 0
    jabariReady = input(printInputArrow).lower()
    inDing()
    getHelp(jabariReady,"True")
    inputCourage(jabariReady)
    jabariReadyList = jabariReady.split()

    #to check if there are multiple arguments.
    if 'yes' in jabariReadyList:
        chooseCounter += 1
    if 'no' in jabariReadyList:
        chooseCounter += 1
    if chooseCounter >= 2:
        lib.printDivider("-",10)
        print(printManyArgs)
        lib.printDivider("-",10)
        chooseCounter == 0

    #repsonse for "yes" and "no" scenario.
    elif 'yes' in jabariReady:
        lib.printDivider("-",10)
        print("Jabari is finally ready to jump.")
        lib.printDivider("-",10)
        time.sleep(1)
        print(termcolor.colored("Jabari's Courage went up!","cyan"))
        full += 3
        makeChoice = 'False'

    elif 'no' in jabariReady:
        lib.printDivider("-",10)
        print("Jabari doesn't feel like he's quite ready, but decides to do it anyways.")
        time.sleep(1)
        print("Besides, what could go wrong?")
        makeChoice = 'False'

    #if the input is not recognized.
    elif chooseCounter >= 0 and 'help' not in jabariReady and 'courage' not in jabariReady:
        lib.printDivider("-",10)
        print(printWrongInput)
        lib.printDivider("-",10)
    
time.sleep(1)
lib.printDivider("-",10)
print(termcolor.colored("*****\nObjective: Find the courage to dive off of the diving board.\n*****", 'blue'))
obDing()
time.sleep(1)

failCounter = 0

while chooseAgainC3 == "True" or failCounter > 0:
    #variables to determine which loop should currently be running.
    chooseEn1 = "True"
    chooseEn2 = "False"
    chooseEn3 = "False"
    chooseEn4 = "False"
    chooseQ = "False"

    while chooseEn1 == "True":
        #bottom stage: failing returns you to this stage.
        failCounter = 0
        lib.printDivider("-",10)
        print("Jabari approaches the bottom of the ladder that leads up to the diving board.")
        time.sleep(2)
        print("He needs some encouragement to get started.")
        time.sleep(1)
        lib.printDivider("-",10)
        print("Type: " + termcolor.colored("you got this!","green"))
        lib.printDivider("-",10)
        jabariEncourage1 = input(printInputArrow).lower()
        inDing()
        getHelp(jabariEncourage1,"True")
        inputCourage(jabariEncourage1)

        #first stage: jabari starts climbing upwards.
        if 'you got this' in jabariEncourage1:
            lib.printDivider("-",10)
            print("Jabari feels encouraged, and starts climbing up the ladder.")
            time.sleep(2)
            print("After climbing for a little bit, he realizes how high up he is and starts to get slightly scared.")
            time.sleep(1)
            print("He needs some more encouragement.")
            time.sleep(1)
            chooseEn1 = "False"
            chooseEn2 = "True"
        elif 'you got this' not in jabariEncourage1 and 'help' not in jabariEncourage1 and 'courage' not in jabariEncourage1:
            lib.printDivider("-",10)
            print("Those aren't the right words.")
            failCounter += 1
            time.sleep(1)

        #second stage: Jabari continues to climb.
        while chooseEn2 == "True":
            if failCounter == 0:
                lib.printDivider("-",10)
                print("Type: " + termcolor.colored("keep going!","green"))
                lib.printDivider("-",10)
                jabariEncourage2 = input(printInputArrow).lower()
                inDing()
                getHelp(jabariEncourage2,"True")
                inputCourage(jabariEncourage2)
                if 'keep going' in jabariEncourage2 and failCounter == 0:
                    lib.printDivider("-",10)
                    print("Jabari keeps climbing up the ladder.")
                    time.sleep(2)
                    print("He starts to hesitate. He needs more encouragement to keep going.")
                    time.sleep(1)
                    if full > 3:
                        chooseEn3 = "True"
                    else:
                        chooseQ = "True"
                    chooseEn2 = "False"
                elif 'keep going' not in jabariEncourage2 and 'help' not in jabariEncourage2 and 'courage' not in jabariEncourage2:
                    lib.printDivider("-",10)
                    print("Jabari suddenly gets cold feet, and descends to the bottom of the ladder.")
                    failCounter += 1
                    chooseEn2 = "False"
                    time.sleep(1)

                #if Jabari does not have enough courage, this extra section will play, asking the player a simple math question.
                while chooseQ == "True" and full <= 3:
                    if failCounter == 0 and full <= 3:
                        lib.printDivider("-",10)
                        print("Jabari starts doubting himself a little.")
                        time.sleep(1)
                        print("How tall was this ladder again?")
                        time.sleep(1)
                        ladderHeight = random.randint(3,5)
                        questionAnswer = ladderHeight * 3
                        print("The sign below said it was " + str(ladderHeight) + " meters tall.")
                        time.sleep(1)
                        lib.printDivider("-",10)
                        print(termcolor.colored("How tall is the ladder in feet? (one meter = 3 feet).","green"))
                        lib.printDivider("-",10)
                        jabariQuestion = str(input(printInputArrow))
                        inDing()
                        getHelp(jabariQuestion,"True")
                        inputCourage(jabariQuestion)
                        if str(questionAnswer) == jabariQuestion and failCounter == 0:
                            lib.printDivider("-",10)
                            print("Jabari, with that knowledge in mind, feels more safe, and continues to climb.")
                            time.sleep(2)
                            print("However, after a while he begins to have doubts again.")
                            time.sleep(1)
                            chooseQ = "False"
                            chooseEn3 = "True"
                        elif str(questionAnswer) != jabariQuestion and 'help' not in jabariQuestion and 'courage' not in jabariQuestion:
                            lib.printDivider("-",10)
                            print("Without knowing how high he's really going, Jabari decides to climb back down to the ground for now.")
                            failCounter += 1
                            chooseQ = "False"
                            time.sleep(1)

                #with enough courage, the previous section would be skipped. However, this stage will always play out.
                #third stage: jabari makes it to the top of the ladder.
                while chooseEn3 == "True":
                    if failCounter == 0:
                        lib.printDivider("-",10)
                        print("Type: " + termcolor.colored("almost there!","green"))
                        lib.printDivider("-",10)
                        jabariEncourage3 = input(printInputArrow).lower()
                        inDing()
                        getHelp(jabariEncourage3,"True")
                        inputCourage(jabariEncourage3)
                        if 'almost there' in jabariEncourage3 and failCounter == 0:
                            lib.printDivider("-",10)
                            print("Jabari finally reaches the top of the ladder. He's at the top of the world!")
                            time.sleep(2)
                            print("He needs just a little more encouragement to finally make the jump!")
                            time.sleep(1)
                            chooseEn4 = "True"
                            chooseEn3 = "False"
                        elif 'almost there' not in jabariEncourage3 and 'help' not in jabariEncourage3 and 'courage' not in jabariEncourage3:
                            lib.printDivider("-",10)
                            print("At the last moment, Jabari gets too scared and descends back down the ladder in a hurry.")
                            failCounter += 1
                            chooseEn3 = "False"
                            time.sleep(1)

                        #final, fourth stage: jabari finally jumps off of the diving board.
                        while chooseEn4 == "True":
                            if failCounter == 0:
                                lib.printDivider("-",10)
                                print("Type: " + termcolor.colored("jump!","green"))
                                lib.printDivider("-",10)
                                jabariEncourage4 = input(printInputArrow).lower()
                                inDing()
                                getHelp(jabariEncourage4,"True")
                                inputCourage(jabariEncourage4)
                                if 'jump' in jabariEncourage4 and failCounter == 0:
                                    lib.printDivider("-",10)
                                    print("Jabari finally takes a leap of faith!")
                                    lib.printDivider("-",10)
                                    chooseAgainC3 = 'False'
                                    chooseEn4 = 'False'
                                    jabariJumps = 'True'
                                elif 'jump' not in jabariEncourage4 and 'help' not in jabariEncourage4 and 'courage' not in jabariEncourage4:
                                    lib.printDivider("-",10)
                                    print("Jabari peers over the edge of the board and gets scared at the last moment. He races down the ladder to the ground.")
                                    failCounter += 1
                                    chooseEn4 = "False"
                                    time.sleep(1)



#final ending.
if jabariJumps == 'True':
    end = text2art("END.")
    time.sleep(2)
    mixer.music.load('Splash.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    lib.typewrite(termcolor.colored("SPLASH!\n","blue"),0.2)
    time.sleep(1)
    lib.printDivider("-",10)
    print("Jabari thought that was pretty fun.")
    time.sleep(1)
    print("He might even try it again.")
    time.sleep(3)
    lib.printDivider("-",10)
    print("\n")
    print(end)
    lib.printDivider("-",10)